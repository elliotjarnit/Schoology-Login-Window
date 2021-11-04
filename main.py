from sys import platform
import os
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common
# Start of editable settings

# The subdomain to the schoology domain. Write False if not applicable. Example: usdc.schoology.com would be usdc
subdomain = "klschools"

# End of editable settings

if platform == "darwin":
    pass
else:
    print("Unsupported platform")
    time.sleep(5)
    exit()

try:
    driver = webdriver.Chrome()
except selenium.common.exceptions.WebDriverException:
    print("Need to install chrome web driver. Type \"Y\" to continue or \"N\" to cancel")
    a = input("> ")
    if a.lower() == "y":
        print("Starting install of chrome web driver")
        os.system("brew install chromedriver")
        print("\n\n\n\nInstalled Driver. Continuing")
        time.sleep(3)
        driver = webdriver.Chrome()
    elif a.lower() == "n":
        print("Aborting...")
        exit()
    else:
        print("Not a valid answer. Aborting...")
        exit()
except ConnectionError:
    print("Please update google chrome to latest version")
    time.sleep(5)
    exit()

if not subdomain:
    domain = "https://schoology.com"
else:
    domain = "https://" + subdomain + ".schoology.com"

driver.get(domain + "/api")

try:
    WebDriverWait(driver, 120).until(EC.url_matches((domain + "/api") or (domain + "/api#")))
except:
    print("Took too long")
    time.sleep(5)
    exit()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "edit-current-key")))
publicKey = driver.find_element_by_id("edit-current-key").get_attribute("value")
secretKey = driver.find_element_by_id("edit-current-secret").get_attribute("value")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._1SIMq._2kpZl._3OAXJ._13cCs._3_bfp._2M5aC._24avl._3v0y7._2s0LQ._3ghFm._3LeCL._31GLY._9GDcm._1D8fw.util-height-six-3PHnk.util-pds-icon-default-2kZM7.StandardHeader-header-button-active-state-V0d6c.StandardHeader-header-button-1562K.Z_KgC.fjQuT.uQOmx")))
button1 = driver.find_element_by_css_selector("._1SIMq._2kpZl._3OAXJ._13cCs._3_bfp._2M5aC._24avl._3v0y7._2s0LQ._3ghFm._3LeCL._31GLY._9GDcm._1D8fw.util-height-six-3PHnk.util-pds-icon-default-2kZM7.StandardHeader-header-button-active-state-V0d6c.StandardHeader-header-button-1562K.Z_KgC.fjQuT.uQOmx")
button1.click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Your Profile']")))
prof_button = driver.find_element_by_xpath("//a[normalize-space()='Your Profile']")
user_id = prof_button.get_attribute("href")
userID = str(user_id).replace((domain + "/user/"), "").replace("/info", "")
driver.quit()
print("User ID: " + userID)
print("User Secret Key: " + secretKey)
print("User Public Key: " + publicKey)
