Feature: Test Dataset
#  Scenario: User create dataset and verify title name
#    Given User login with login credentials email "test@mailinator.com" nad password "123456"
#    When User create dataset with name "MyDataset"
#    Then User verify title name of dataset "MyDataset"
#
#  Scenario: User upload file in dataset
#    When User upload file "requirements.txt" in dataset "MyDataset"
#    Then User verify file name uploaded in dataset "requirements.txt"

#  Scenario: User inputs invalid commands
#    When User uploads a file but enters empty strings instead of entering path of file in dataset "MyDataset"
#    Then User verify the exception raised

#  Scenario: User uploads 2 files in dataset
#    When User uploads 2 files "test.py" and "demo.txt" in dataset "MyDataset"
#    Then User verifies by file count in dataset "MyDataset"

#  Scenario: User Removes a file
#    When User removes a file "requirements.txt" from dataset "MyDataset"
#    Then User Verifies by file name "requirements.txt" is present or not

  Scenario: User Uploads 2 files in dataset in wrong format
    When User uploads 2 files "test.py" and "demo.txt" in dataset "MyDataset" n wrong format
    Then User verifies by the exception raised