*** Settings ***
Documentation    Example of drop_down
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       Edge
${URL}           https://chercher.tech/practice/practice-dropdowns-selenium-webdriver


*** Test Cases ***
handle drop down using robot framework
    open browser  ${URL}  ${BROWSER}
    maximize browser window
    sleep   5
#    select from list by label     first   Google
    select from list by value     first   Apple













