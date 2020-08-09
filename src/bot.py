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

    def Interpretation(self, msg_tab)
        return 0

    def SpeakWithPeople(self):
        print("Wait 1 min...")
        sleep(60)
        i = 1
        boucle = 0
        message = "Salut, cava ?"
        while True:
            try:
                username = self._driver.find_element_by_id("ongun"+str(i)).text
                print("go speak with id ->", i, "And username ->", username)
                self._driver.find_element_by_id("ongun"+str(i)).click()
                print("LOG: ")
                elements = self._driver.find_elements_by_id("textum")
                # message = self.Interpretation(elements)
                self._driver.find_element_by_id("cocoa").send_keys(message)
                self._driver.find_element_by_id("cocoa").send_keys(Keys.RETURN)
                boucle = boucle + 1
            except NoSuchElementException:
                print("Get Exception... id = ", i)
                i = 1
                sleep(30)
            i = i + 1

    def Start(self):
        self.ConnexionChat()
        self.SpeakWithPeople()

    def Finish(self):
        self._driver.quit()

