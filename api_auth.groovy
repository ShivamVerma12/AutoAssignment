@Library('jenkins-shared-library') _

pipeline {
    agent any
    stages {
        stage('Create Token and upload report'){
            steps{
                script{
                   def bearer = """
import subprocess
import requests
response = requests.post('https://xray.cloud.getxray.app/api/v2/authenticate',
                             data={'client_id': '5E4F5179DFC2445086DA4CAAC85A6D5D',
                                   'client_secret': '71beabdad7d16921a226666b815d4200fb74e07d12bb04832d194a2edbf707eb'})
parsed_auth = response.json()
token = f'Bearer {parsed_auth}'
curl_cmd = f"curl -H "Content-Type: test/xml" -X POST -H "Authorization:{token}" --data @resultsAB.xml  https://xray.cloud.getxray.app/api/v2/import/execution/junit?projectKey=KAN

                    """
                    // Write the Python script to a file
                    writeFile(file: 'collections.py', text: bearer)
                }
            }
        }
                
        
    }
}
