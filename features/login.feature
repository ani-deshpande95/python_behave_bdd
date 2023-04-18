# Created by Anirudha at 15-03-2023
Feature: Login verification through UI and API

  #@UI
  #Scenario: Verify login through UI
    #Given user is on "qaenvironment"
    #When user enters username "qatestusername"
    #When user enters password "qauserpassword"
    #When user clicks on login button
    #Then welcome text should be displayed

  #@API
  #Scenario: Verify login through API
    #Given user setup the login api data
    #When user request the post login API to "parasoftbank"
    #Then user should be able to login successfully with status code "200"

  @API
  Scenario: Verify user is able to read GCS file
    Given user provides the "test_for_python" bucket name
    When user provides the "Sample_csv.csv" file name
    #When user read the file
    #Then file content should be printed to console