*** Settings ***
Documentation    Example of testing login functionality
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       Edge
${URL}           https://profile.w3schools.com/
${USERNAME}      shubhamshedge810@gmail.com
${PASSWORD}      AdminShubham@123

*** Test Cases ***
Login With Valid Credentials
    Open Browser  ${URL}  ${BROWSER}
    loginToW3School
    Close Browser

*** Keywords ***
loginToW3School
    Input Text    id=modalusername    ${USERNAME}
    Input Text    id=current-password    ${PASSWORD}
    Click Button  xpath=//button[@class='Button_button__URNp+ Button_primary__d2Jt3 Button_fullwidth__0HLEu']
