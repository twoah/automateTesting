from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time, requests, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

global results, driver

def setting(device_name): 
    devices = requests.get("http://127.0.0.1:8000/get/device/" + device_name).json()
    device = devices[0]
    desired_caps = {
        'platformName': device['device_os'],
        'platformVersion': device['platform_version'],
        'deviceName': device_name,
        'app': '/Users/ah/Desktop/django/ATA/Ktmembership_210701.apk',
        'autoGrantPermissions': 'true',
        'automationName': 'UiAutomator2',
        'ignoreHiddenApiPolicyError': 'true',
        'appActivity': device['app_activity']
    }
    return desired_caps

def run() : 
    desired_caps = setting("R3CN606LM4J")
    driver =  webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.switch_to.context('NATIVE_APP')
    appium(driver, "KT멤버십")
    driver.quit()
    mail()


def appium(driver, app_name):
    scenarioList = requests.get("http://127.0.0.1:8000/get/scenario/" + app_name).json()
    for scenario in scenarioList : 
        scenario_id = scenario['id']

        case_result = []
        cases = requests.get("http://127.0.0.1:8000/get/case/" + scenario_id).json()
        for case in cases : 
            if case['gubun'] == "click" : 
                chk = findElementByID(driver, case['element_id'])
            elif case['gubun'] == "xpath" : 
                chk = findElementByXPath(driver, case['element_id'])
            elif case['gubun'] == "input":
                chk = findElementByInput(driver, case['element_id'], case['element_value'])
            else :
                chk = driverBack(driver)

            if chk is True:
                temp = [case['element_id'], "성공"]
                case_result.append(temp)
            else : 
                temp = [case['element_id'], "실패"]
                case_result.append(temp)
        results.append([scenario['title'], case_result])

def driverBack(driver): 
    try : 
        driver.back()
        return True
    except Exception as e:
        print(e)
        return False

def findElementByID(driver, input):
    try:
        driver.find_element_by_id(input).click()
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False

def findElementByXPath(driver, input):
    try:
        driver.find_element_by_id(input).click()
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False

def findElementByInput(driver, element, input):
    try:
        driver.find_element_by_id(element).send_keys(input)
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False

def mail():

    send_email = "ataproject21@gmail.com"
    send_pw = "new!1234new"

    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(send_email, send_pw)
    receive_emails = ['ahhyeon.lee@kt.com']

    for receive in receive_emails:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "[공유] 테스트 자동화 결과 내용 공유"
        msg['From'] = send_email
        msg['To'] = receive
        part1 = MIMEText(makeHTML(results), 'html')
        msg.attach(part1)
        s.sendmail(send_email, receive, msg.as_string())
        s.quit()

def makeHTML(results):
    str = ""
    for result in results : 
        str += """<p style="padding:5px 0 0 0;">▷ 테스트 케이스명 : """ + result[0] + """</p>
         <table style="margin: 10px 0 10px 0;" border="1" cellpadding="0" cellspacing="0" width="40%"> 
            <tr>
                <td style="padding: 10px;" align="center">케이스</td>
                <td style="padding: 10px;" align="center">결과</td>
            </tr>"""
        for case in result[1] : 
            str += """<tr> <td style="padding: 10px;" align="center">""" + case[0] + """</td> <td style="padding: 10px;" align="center">""" + case[1] + """</td></tr>"""
        str += """</table>"""

    html = """\
   <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>테스트 자동화 결과 메일</title>
    </head>
    <body>
        <h4>테스트 자동화 결과 내용 공유</h4>
        <p style="padding:5px 0 0 0;">안녕하세요. 테스트 자동화 수행 내용 공유드립니다.</p>
        """ + str + """
    </body>
    </html>
    """
    return html
        
if __name__ == '__main__':
    results = []
    run()



    
# def startApp(driver):
#     findElementByID(driver, "com.olleh.android.oc2:id/guide_start")
#     findElementByID(driver, "com.olleh.android.oc2:id/dsp_tv_close")

# def login(driver):
#     findElementByID(driver, "com.olleh.android.oc2:id/button_menu")
#     findElementByID(driver, "com.olleh.android.oc2.dev:id/Leftnavi_login")
#     findElementByID_sendKey(driver, "com.olleh.android.oc2.dev:id/spl_edit_id", "ahzzng")
#     findElementByID_sendKey(driver, "com.olleh.android.oc2.dev:id/spl_edit_pwd","zpdlxl12!!")
#     findElementByID("com.olleh.android.oc2.dev:id/spl_btn_login")
#     driver.back()
#     driver.back()

# def mainCard(driver):
#     findElementByID(driver, "com.olleh.android.oc2.dev:id/main_card")
#     driver.back()

# def hotBanner(driver):
#     findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                  ".FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget"
#                                  ".FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout["
#                                  "2]/android.widget.LinearLayout[2]")
#     findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                  ".FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget"
#                                  ".FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout["
#                                  "2]/android.widget.LinearLayout[3]")
#     findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
#                                  ".FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget"
#                                  ".FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout["
#                                  "2]/android.widget.LinearLayout[4]")

# def affiliate(driver):
#     findElementByID("com.olleh.android.oc2.dev:id/button_menu")  # lnb
#     findElementByID("com.olleh.android.oc2.dev:id/lblListItem")
#     findElementByID("com.olleh.android.oc2.dev:id/down_back")
#     driver.back()