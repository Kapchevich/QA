from selenium import webdriver
import time
driver = webdriver.Chrome()
q = 0
try:
    driver.get("https://lenta.com/npl/authentication/login/")
    driver.find_element_by_css_selector(".store-tooltiping-popup__tooltip-close-icon").click()
    a = driver.find_element_by_css_selector(".input-field__control").send_keys("*********")

    driver.find_element_by_xpath("//input [@type='password']").send_keys("********")

    driver.find_element_by_xpath("//button [@type='submit']").click()
    time.sleep(5)
    driver.get("https://lenta.com/lk/profile/bonus-history/")
    a = driver.find_element_by_css_selector(".receipt-history-item").click()
    time.sleep(3)
    b = driver.find_element_by_css_selector(".receipt-details__products-list")
    v = b.text
    for i in v:
        if q == 3:
            q = 0
        if i == "\n":
            q = q + 1
        if q == 0:
            print(i, end="")
finally:
    time.sleep(1)
    driver.quit()