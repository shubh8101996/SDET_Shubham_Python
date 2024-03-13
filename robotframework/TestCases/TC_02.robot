*** Settings ***
Documentation    Example of validating input box i.e visiable or enable or not
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       Edge
${URL}           https://profile.w3schools.com/
${USERNAME}      shubhamshedge810@gmail.com
${PASSWORD}      AdminShubham@123

*** Test Cases ***
Checking input box visiblity and enabled or not
    open browser  ${URL}  ${BROWSER}
    maximize browser window
    title should be     Log in - W3Schools
    ${email_txt}    set variable    id=modalusername
    ${password_txt}    set variable    id=current-password
    element should be visible   ${email_txt}
    sleep   5
    element should be visible   ${password_txt}
    sleep   5
    close browser






