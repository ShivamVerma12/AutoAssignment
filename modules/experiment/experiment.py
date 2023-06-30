import time
from selenium.webdriver.support import expected_conditions as EC

from cnvrgv2.errors import CnvrgHttpError
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from helper.helper import browser
from azure.storage.blob import BlobServiceClient

global slug


def create_project(cnvrg, project_name):
    # myproj = cnvrg.projects.create(project_name)
    try:
        # myproj = cnvrg.projects.get(project_name)
        if cnvrg.projects.get(project_name):
            print("Already present")
            return
    except CnvrgHttpError:
        myproj = cnvrg.projects.create(project_name)
        print(myproj)

    # except Exception as e:
    #     myproj = cnvrg.projects.create(project_name)
    #     print(myproj)
    #     print(e)


def upload_file(cnvrg, file_name, project_name):
    myproj = cnvrg.projects.get(project_name)
    myproj.put_files(paths=[file_name])


def create_experiment(cnvrg, project_name, experiment_name):
    myproj = cnvrg.projects.get(project_name)
    print(myproj)
    experiment = myproj.experiments.create(title=experiment_name,
                                           template_names=["small"],
                                           command="ruby experiment.rb",
                                           sync_before=False)
    while experiment.status != "success":
        experiment.reload()
        time.sleep(2)
    global slug
    slug = experiment.slug


def verify_status(cnvrg, project_name):
    myproj = cnvrg.projects.get(project_name)
    experiment = myproj.experiments.get(slug)

    if experiment.status == "success":
        return True
    else:
        return False
