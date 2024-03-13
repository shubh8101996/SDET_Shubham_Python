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
    get all links count


*** Keywords ***
get all text
    @{element_list}=  Get WebElements  xpath://a
    FOR  ${element}  IN  @{element_list}
        Log to console  ${element.text}
    END

get all links
    @{element_list}=  Get WebElements  xpath://a
    FOR  ${element}  IN  @{element_list}
        Log to console  ${element.get_attribute('href')}
    END

get all links count
    @{link_count}=  get element count  xpath://a
    Log to console  @{link_count}







