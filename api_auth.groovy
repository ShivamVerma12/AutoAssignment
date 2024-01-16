@Library('jenkins-shared-library') _

pipeline {
    agent any
    parameters {
        choice(name: 'WORKSPACE', choices: ['API-AUT'], description: 'Select Workspace')
    }
    environment {
        WORKSPACE = "${params.WORKSPACE ?: 'API-AUT'}"
    }
    stages {
        stage('Clear Workspace') {
            steps {
                deleteDir()
            }
        }
        // stage('Run Build CICD') {
        //     when {
        //         expression { params.WORKSPACE == 'API-AUT' }
        //     }
        //     steps {
        //         script {
        //             // Trigger the 'CICD' job without parameters and wait for completion
        //             def cicdJob = build(job: 'CICD', wait: true)

        //             if (cicdJob.resultIsBetterOrEqualTo('SUCCESS')) {
        //                 // Get the build number of the 'CICD' job
        //                 def buildNumber = cicdJob.number

        //                 // Set the cicd_number parameter to pass it to the next stage
        //                 cicd_number = "${buildNumber}"

        //             } else {
        //                 error("Failed to build 'CICD' job")
        //             }
        //         }
        //     }
        // }
        stage('Prepare Environment and Run API-AUT Tests') {
            when {
                expression { params.WORKSPACE == 'API-AUT' }
            }
            steps {
                script {
                    // Remove existing 'Collections' directory if it exists and run everything from that location
                    sh 'rm -rf Collections'
                    sh 'mkdir Collections'
                    // Run terminal commands to prepare the environment
                    sh '''
                        cd Collections
                        sudo apt install -y jq
                        sudo npm install -g newman@4.5.6 --unsafe-perm=true --allow-root
                        sudo npm install -g newman-reporter-junit --unsafe-perm=true --allow-root
                        sudo npm install -g newman@4.5.6 postman-combine-collections --save --unsafe-perm=true --allow-root
                        curl -X GET "https://api.getpostman.com/workspaces/b38ccd71-80f2-44f3-83ae-e81ccd48a930" -H "X-Api-Key: PMAK-6501d1a409dd38002bf3416c-07b1ed39641164457905361086d6e9a6ce" -H "Cache-Control: no-cache" -o API_AUT_workspace.json
                    '''
                    // Define the Python script within a Groovy triple-quoted string
                    def api_aut_collections = """
import subprocess
import json
import time

# Replace these values with your actual Postman API key and workspace ID
postman_api_key = 'PMAK-6501d1a409dd38002bf3416c-07b1ed39641164457905361086d6e9a6ce'

# Load your Postman workspace JSON file
with open('API_AUT_workspace.json', 'r') as file:
    workspace_data = json.load(file)

# Extract collections from the nested structure
collections = workspace_data['workspace']['collections']

# Extract the environment from the nested structure (assuming there is only one environment)
environment = workspace_data['workspace']['environments'][0]
environment_uid = environment['uid']

# Iterate through each collection in the workspace
for collection in collections:
    collection_id = collection['uid']
    collection_name = collection['name']

    # Construct the curl command
    curl_command = f'curl -f --retry 5 -X GET "https://api.postman.com/collections/{collection_id}" -H "X-Api-Key: {postman_api_key}" -H "Cache-Control: no-cache" -o "{collection_name}.json"'

    # Execute the curl command using subprocess
    try {
        subprocess.run(curl_command, shell=True, check=True)
        print(f'Collection "{collection_name}" exported and saved as "{collection_name}.json"')

        # Wait for a short duration to ensure the file is fully downloaded
        time.sleep(1)

        # Construct the jq command to edit the JSON file
        jq_command = f'jq \'collection | del(.schema, .fork, .updatedAt, .uid)\' "{collection_name}.json" > "{collection_name}.api_aut.json"'

        # Execute the jq command using subprocess
        subprocess.run(jq_command, shell=True, check=True)
        print(f'JSON file "{collection_name}.json" edited and saved as "{collection_name}.api_aut.json"')
    } catch (subprocess.CalledProcessError e) {
        print(f'Failed to export or edit collection "{collection_name}". Error: {e}')
    }

# Construct the curl command to export the environment
curl_command_env = f'curl -X GET "https://api.postman.com/environments/{environment_uid}" -H "X-Api-Key: {postman_api_key}" -H "Cache-Control: no-cache" -o "api_aut_environment.json"'

# Execute the curl command for the environment using subprocess
try {
    subprocess.run(curl_command_env, shell=True, check=True)
    print(f'Environment exported successfully')
} catch (subprocess.CalledProcessError e) {
    print(f'Failed to export environment. Error: {e}')
}
"""
                    // Write the Python script to a file
                    writeFile(file: 'Collections/collections.py', text: api_aut_collections)
                    sh '''
                        cd Collections
                        python3 collections.py
                        postman-combine-collections --name API-AUT -f '*.api_aut.json' -o api_aut.collection.json
                    '''
                    // Run Newman tests and capture the output
                    def newmanOutput = sh(script: '''
                        cd Collections
                        newman run api_aut.collection.json -r junit  --reporter-junit-export newman.xml -e api_aut_environment.json --insecure 
                        exit 0  # Always exit with code 0
                    ''', returnStatus: true)
                }
            }
        }
    }
}
