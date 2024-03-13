*** Settings ***
Suite Setup  log to console     open browser
Suite Teardown  log to console      close browser


Test Setup  log to console      login to application
Test Teardown  log to console   log out to application



*** Test Cases ***
TC_01_View_Profile
    log to console      profile viewed

TC_01_Edit_Profile
    log to console      profile Edited

TC_01_Delete_Profile
    log to console      profile Deleted

