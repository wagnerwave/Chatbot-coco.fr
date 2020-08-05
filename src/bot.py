#!/usr/bin/env python3

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

Website = "https://coco.fr"
DriverPath = "./geckodriver"

class Bot:
    def __init__(self, PostalCode, Years, Username):
        self._PostalCode = PostalCode
        self._Years = Years
        self._Pseudo = Username
        self._driver = webdriver.Firefox(executable_path=DriverPath)

    def ConnexionChat(self):
        self._driver.get(Website)
        window_before = self._driver.window_handles[0]
        self._driver.find_element_by_id('zipo').send_keys(self._PostalCode)
        self._driver.find_element_by_id("ageu").send_keys(self._Years)
        self._driver.find_element_by_id("nicko").send_keys(self._Pseudo)
        self._driver.find_element_by_id("femme").click()
        self._driver.find_element_by_id("tchater").click()
        self._driver.switch_to_window(window_before)
        self._driver.close()
        self._driver.switch_to_window(self._driver.window_handles[0])

    def Speak(self):
        sleep(60)
        i = 1
        message = "coucou, ca va ?"
        while True:
            self._driver.find_element_by_id("ongdiv"+str(i)).click()
            sleep(2)
            self._driver.find_element_by_id("cocoa").send_keys(message)
            self._driver.find_element_by_id("cocoa").send_keys(Keys.RETURN)

    def Start(self):
        self.ConnexionChat()
        self.Speak()

    def Finish(self):
        self._driver.quit()

