*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${BROWSER}       Chrome
${URL}           https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Get all link and return a text,count & links
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    sleep   5
    scroll element into view       xpath://div[@class='tableFixHead']/child::table
    sleep   2
    ${rows}    get element count   xpath://div[@class='tableFixHead']/child::table//tr
    ${cols}    get element count   xpath://div[@class='tableFixHead']/child::table//tr[1]/th
    ${getalldata}   get text    xpath://div[@class='tableFixHead']/child::table//td

    log to console  ${rows}
    log to console  ${cols}
    log to console  ${getalldata}














