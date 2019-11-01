#!/usr/bin/env python

from selenium import webdriver
import time


def dep_calc_ul():
    driver = webdriver.Firefox()
    driver.get('https://www.otpbank.ru/business/sme/depoziti')
    time.sleep(3)

    amount_field = driver.find_element_by_name("amount")
    amount_field.clear()
    amount_field.send_keys("30000")

    duration_field = driver.find_element_by_name("duration")
    duration_field.clear()
    duration_field.send_keys("12")

    refill_checkbox = driver.find_element_by_class_name("deposit-calc__checkbox-label")
    refill_checkbox.click()

    radio_withdrawal = driver.find_element_by_xpath("//div[@class='deposit-chooser']/div[3]/div[@class='radiobutton-set']/label[3]")
    radio_withdrawal.click()

    name_company_field = driver.find_element_by_name("company")
    name_company_field.send_keys("ООО 'Клевер'")

    city_name_field = driver.find_element_by_name("city")
    city_name_field.send_keys("Москва")

    contact_name_field = driver.find_element_by_name("contact_name")
    contact_name_field.send_keys("Иванов И.И.")
    
    phone_field = driver.find_element_by_name("phone")
    phone_field.send_keys("9119990000")

    comment_field = driver.find_element_by_name("comment")
    comment_field.send_keys("Тест")

    agr_checkbox = driver.find_element_by_css_selector("p.form-anketa__agree input")
    try:
        agr_checkbox.click()
    except:
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(agr_checkbox, 3, 3)
        action.click()
        action.perform()
    
    button = driver.find_element_by_xpath("//div[@class='form-anketa__submit-wrap']/button")
    button.click()
    time.sleep(3)

    result = driver.find_element_by_id("resultPlace").text
    driver.quit()

    if result == "Заявка успешно отправлена.":
        return True
    else:
        return False



if __name__ == '__main__':
    dep_calc_ul()