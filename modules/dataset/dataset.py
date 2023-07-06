from selenium.webdriver.common.by import By


# def login(browser, email, password):
#     browser.get(os.environ.get("URL"))
#     emailaddress_field = browser.find_element(By.NAME, "email")
#     password_field = browser.find_element(By.NAME, "password")
#     login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")

#     # Enter the login credentials
#     emailaddress_field.send_keys(email)
#     password_field.send_keys(password)

#     # Click the login button to login
#     login_button.click()


def create_dataset(cnvrg, dataset_name):
    try:
        dataset = cnvrg.datasets.create(name=dataset_name, category='general')

    except Exception as e:
        print(e)


def upload_file(cnvrg, dataset_name, file_name):
    try:
        dataset = cnvrg.datasets.get(dataset_name)
        ds = dataset.put_files(paths=[file_name])
        if ds in None:
            raise Exception

    except Exception as e:
        return e


def verify_file_name(cnvrg, file_name):
    dataset = cnvrg.datasets.get("MyDataset")
    ds = dataset.list_files()
    for i in ds:
        if i.file_name == file_name:
            return True

    return False


def upload_files(cnvrg, dataset_name, file1, file2):
    dataset = cnvrg.datasets.get(dataset_name)
    dataset.put_files(paths=[file1, file2])


def count_file(cnvrg, dataset_name):
    dataset = cnvrg.datasets.get(dataset_name)
    return dataset.num_files


def remove_file(cnvrg, filename, dataset_name):
    dataset = cnvrg.datasets.get(dataset_name)
    dataset.remove_files(paths=[filename],
                         message='This will delete everything!')


def upload_files_wrong_format(cnvrg, dataset_name, file1, file2):
    try:
        dataset = cnvrg.datasets.get(dataset_name)
        ds = dataset.put_files(paths=[file1, file2])
        if ds in None:
            raise Exception

    except Exception as e:
        return e
