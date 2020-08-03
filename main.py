#!/usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def OpenBrowser():
    nav = webdriver.Firefox(executable_path='./geckodriver')
    nav.get("https://coco.fr")
    return nav

def ConnexionChat(driver, Departement, Age, Pseudo):
    driver.find_element_by_id("zipo").send_keys(Departement)
    driver.find_element_by_id("ageu").send_keys(Age)
    driver.find_element_by_id("nicko").send_keys(Pseudo)
    driver.find_element_by_id("femme").click()
    driver.find_element_by_id("tchater").click()

def ChatExist(driver, id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def CheckNewChat(driver):
    chat = "ondiv"
    i = 1
    MSG = "coucou, ca va ?"
    while (1):
        if ChatExist(driver, chat+str(i)):
            print("-> chat with ", chat+str(i))
            driver.find_element_by_id(chat+i).click()
            driver.find_element_by_id("cocoa").send_keys(MSG)
            driver.find_element_by_id("cocoa").send_keys(Keys.RETURN)
        else:
            print("No conversation found...")
            sleep(30)
        i = i + 1

def CloseBrowser(driver):
    driver.close()

if __name__ == "__main__":
    driver = OpenBrowser()
    ConnexionChat(driver, "22000", 22, "SexyLapine22")
    CheckNewChat(driver)
    CloseBrowser(driver)