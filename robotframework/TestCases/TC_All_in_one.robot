*** Settings ***
Library          SeleniumLibrary

*** Variables ***
${BROWSER}       Chrome
${URL}           https://rahulshettyacademy.com/AutomationPractice/
${Path}          C:/Users/HP/PycharmProjects/SDET_shubham/robotframework/screenshot/Abc.png

*** Test Cases ***
Login With Valid Credentials
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    handle alerts


*** Keywords ***
Capture Element
    Capture Element Screenshot    xpath://img[@class='logoClass']   C:/Users/HP/PycharmProjects/SDET_shubham/robotframework/screenshot/Abc.png


Capture Page
    Capture Page Screenshot     C:/Users/HP/PycharmProjects/SDET_shubham/robotframework/screenshot/Abc.png

Handle alerts
    click element   id:alertbtn
#    handle alert    accept
    alert should be present     Hello , share this practice page and share your knowledge

