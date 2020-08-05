#!/usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def ChatExist(driver, id):
    print("TEST ID ->", id)
    if driver.find_element_by_id(id):
        return True
    else:
        return False

def ConnexionChat(Departement, Age, Pseudo):
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get("https://coco.fr")
    window_before = driver.window_handles[0]
    driver.find_element_by_id('zipo').send_keys(Departement)
    driver.find_element_by_id("ageu").send_keys(Age)
    driver.find_element_by_id("nicko").send_keys(Pseudo)
    driver.find_element_by_id("femme").click()
    driver.find_element_by_id("tchater").click()
    driver.switch_to_window(window_before)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    print("wait 1 min ...")
    sleep(60)
    print("LETS GO")
    i = 1
    MSG = "coucou, ca va ?"
    talk = chat + str(i)
    print(talk)
    while True:
        #print("-> chat with ", chat+str(i))
        driver.find_element_by_id("ongdiv"+str(i)).click()
        sleep(2)
        driver.find_element_by_id("cocoa").send_keys(MSG)
        driver.find_element_by_id("cocoa").send_keys(Keys.RETURN)
#        else:
#            print("No conversation found...")
#            sleep(30)
        i = i + 1
    driver.close()


if __name__ == "__main__":
    ConnexionChat("92000", 24, "SexyLapine92")
