# python_behave_bdd

Requirements
Python needs to be installed on your machine along with following dependencies

behave~=1.2.6
selenium~=4.8.2
requests~=2.28.2


Use below command to execute following behave BDD POC
behave -f allure_behave.formatter:AllureFormatter -o "my_report" features/login.feature

Use below command to generate Allure report
allure serve my_report
