import time
import re
import string
import random
import sys
import colorama
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint

try:
    from __constants.const import *
    from __banner.myBanner import bannerTop
    from __colors__.colors import *
except ImportError as e:
    print(f"Error importing module: {e}")
    sys.exit(1)

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

def postFix(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_phone_num_generator():
    first = str(random.choice(country_codes))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

def start_bot(start_url, email, college, collegeID):
    studentPhone = random_phone_num_generator()

    try:
        ex_split = studentAddress.split("\n")

        streetAddress = ex_split[0]

        if re.compile(',').search(ex_split[1]) is not None:
            ex_split1 = ex_split[1].split(', ')
            cityAddress = ex_split1[0]
            ex_split2 = ex_split1[1].split(' ')
            stateAddress = ex_split2[0]
            postalCode = ex_split2[1]
        else:
            ex_split3 = ex_split[1].split(' ')
            cityAddress = ex_split3[0]
            stateAddress = ex_split3[1]
            postalCode = ex_split3[2]

    except Exception as e:
        print(f"Error parsing address: {e}")
        sys.exit(1)

    random.seed()

    letters = string.ascii_uppercase
    middleName = random.choice(letters)

    try:
        with open('prefBrowser.txt', 'r') as fp:
            typex = fp.read().strip()

        # Initialize WebDriver based on preferred browser
        if typex == 'chrome':
            driver = webdriver.Chrome(executable_path='./webdriver/chromedriver')
        elif typex == 'firefox':
            driver = webdriver.Firefox(executable_path='./webdriver/geckodriver')
        else:
            print(fr + 'Error - Run setup.py first')
            sys.exit(1)
    except Exception as e:
        time.sleep(0.4)
        print('\n' + fr + 'Error - ' + str(e))
        sys.exit(1)

    driver.maximize_window()
    driver.get(start_url)

    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="portletContent_u16l1n18"]/div/div[2]/div/a[2]').click()

    time.sleep(1)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "accountFormSubmit"))
    ).click()

    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Account Progress - 1/3', end='')

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "inputFirstName"))
    ).send_keys(firstName)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "inputMiddleName"))
    ).send_keys(middleName)
    
    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "inputLastName"))
    ).send_keys(LastName)

    time.sleep(0.7)

    driver.find_element(By.XPATH, '//*[@id="hasOtherNameNo"]').click()
    driver.find_element(By.XPATH, '//*[@id="hasPreferredNameNo"]').click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'#inputBirthDateMonth option[value="{randomMonth}"]'))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'#inputBirthDateDay option[value="{randomDay}"]'))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputBirthDateYear'))
    ).send_keys(randomYear)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'#inputBirthDateMonthConfirm option[value="{randomMonth}"]'))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'#inputBirthDateDayConfirm option[value="{randomDay}"]'))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputBirthDateYearConfirm'))
    ).send_keys(randomYear)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, '-have-ssn-no'))
    ).click()

    time.sleep(4)

    element = driver.find_element(By.ID, 'accountFormSubmit')
    desired_y = (element.size['height'] / 2) + element.location['y']
    window_h = driver.execute_script('return window.innerHeight')
    window_y = driver.execute_script('return window.pageYOffset')
    current_y = (window_h / 2) + window_y
    scroll_y_by = desired_y - current_y

    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    time.sleep(1)

    element.click()

    print(fg + ' (Success)')

    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Account Progress - 2/3', end='')

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputEmail'))
    ).send_keys(email)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputEmailConfirm'))
    ).send_keys(email)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSmsPhone'))
    ).send_keys(studentPhone)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputStreetAddress1'))
    ).send_keys(streetAddress)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputCity'))
    ).send_keys(cityAddress)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, f'#inputState option[value="{stateAddress}"]'))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPostalCode'))
    ).send_keys(postalCode)

    time.sleep(2)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'accountFormSubmit'))
    ).click()

    try:
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="messageFooterLabel"]').click()

        opError = True

        while opError:
            chkInputPhone = driver.find_element(By.ID, 'inputSmsPhone')
            chkError = chkInputPhone.get_attribute('class')
            if chkError == 'portlet-form-input-field error':
                print('\n' + fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Invalid Number, Retrying....')
                chkInputPhone.clear()
                studentPhone = random_phone_num_generator()
                chkInputPhone.send_keys(studentPhone)
                time.sleep(0.4)
                WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.ID, 'inputAlternatePhone_auth_txt'))
                ).click()

                try:
                    time.sleep(2)
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="messageFooterLabel"]'))
                    ).click()
                except:
                    opError = False
            else:
                opError = False

    except Exception as e:
        print(e)
    
    time.sleep(4)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'accountFormSubmit'))
    ).click()

    try:
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'messageFooterLabel'))
        ).click()

        time.sleep(0.7)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'inputAddressValidationOverride'))
        ).click()

        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'accountFormSubmit'))
        ).click()

    except:
        pass

    print(fg + ' (Success)')

    userName = firstName + str(postFix(7))
    pwd = LastName + str(postFix(5))
    pin = postFix(4)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputUserId'))
    ).send_keys(userName)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPasswd'))
    ).send_keys(pwd)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPasswdConfirm'))
    ).send_keys(pwd)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPin'))
    ).send_keys(pin)

    time.sleep(0.7)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPinConfirm'))
    ).send_keys(pin)

    time.sleep(0.7)

    ######### Security Questions #########

    # Question 1
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion1 option[value="5"]'))
    ).click()

    time.sleep(1)

    random.seed(10)
    letters = string.ascii_lowercase

    sec_ans1 = LastName + ''.join(random.choices(letters, k=4))
    sec_ans2 = LastName + ''.join(random.choices(letters, k=4))
    sec_ans3 = LastName + ''.join(random.choices(letters, k=4))

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer1'))
    ).send_keys(sec_ans1)

    time.sleep(1)

    # Question 2
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion2 option[value="6"]'))
    ).click()

    time.sleep(1)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer2'))
    ).send_keys(sec_ans2)

    time.sleep(1)

    # Question 3
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion3 option[value="7"]'))
    ).click()
    time.sleep(1)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer3'))
    ).send_keys(sec_ans3)

    print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Please fill the captcha in webdriver to proceed further')

    solved = 0
    for d in range(1, 200):
        xx = driver.find_element(By.NAME, 'captchaResponse')
        tdt = xx.get_attribute('value')
        if tdt != '':
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Captcha Solved, Executing Further')
            solved = 1
            break
        else:
            time.sleep(2)

    if solved == 1:
        time.sleep(2)

        element = driver.find_element(By.ID, 'accountFormSubmit')
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y

        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

        time.sleep(1)

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "accountFormSubmit"))
        ).click()

        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Account Progress - 3/3' + fg + ' (Success)')
        with open('myccAcc.txt', 'a') as fp:
            birthDay = f"{randomMonth}/{randomDay}/{randomYear}"
            fp.write(f'Email - {email} Password - {pwd} UserName - {userName} First Name - {firstName} Middle Name - {middleName} Last Name - {LastName} College - {college} Birthdate - {birthDay}\n')
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Account Created Successfully, Details saved in myccAcc.txt, Filling Application Form Now')

        time.sleep(1)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="registrationSuccess"]/main/div[2]/div/div/button'))
        ).click()

        time.sleep(0.7)

        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fy + 'Details Progress - 1/8', end='')

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, 'application.termId'))
        )

        dropdown_menu = Select(driver.find_element(By.NAME, 'application.termId'))
        dropdown_menu.select_by_index(1)

        time.sleep(0.7)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#inputEduGoal option[value="B"]'))
        ).click()

        time.sleep(2)

        dropdown_menu = Select(driver.find_element(By.ID, 'inputMajorId'))
        dropdown_menu.select_by_index(random.randint(1, 7))

        time.sleep(2.5)
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.NAME, '_eventId_continue'))
        ).click()

        print(fg + ' (Success)')

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'inputAddressSame'))
        ).click()

        time.sleep(2.5)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="column2"]/div[6]/ol/li[2]/button'))
        ).click()

        # Page 2

        dropdown_menu = Select(driver.find_element(By.NAME, 'appEducation.enrollmentStatus'))
        dropdown_menu.select_by_index(1)

        time.sleep(0.7)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#inputHsEduLevel option[value="4"]'))
        ).click()

        time.sleep(0.7)

        rndPassYear = [3, 4]

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#inputHsCompMM option[value="' + str(random.choice(rndPassYear)) + '"]'))
        ).click()

        time.sleep(0.7)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#inputHsCompDD option[value="' + str(randomEduDay) + '"]'))
        ).click()

        time.sleep(0.7)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'inputHsCompYYYY'))
        ).send_keys(randomEduYear)

        time.sleep(1)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'inputCaHsGradYes'))
        ).click()

        time.sleep(1)

        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'inputCaHs3yearNo'))
        ).click
