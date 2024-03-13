*** Settings ***
Documentation    Example of radio button
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       Edge
${URL}           https://www.techlistic.com/p/selenium-practice-form.html


*** Test Cases ***
Checking input box visiblity and enabled or not
    open browser  ${URL}  ${BROWSER}
    maximize browser window
    sleep   5
    select radio button     sex     Male







