import os
import cleverbotfree.cbfree
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

Website = "https://coco.fr"
DriverPath = "./geckodriver"
MAX_DIAL = 12
## Convert List To String
def listToString(s):
    # initialize an empty string
    str1 = ""
    # return string
    return (str1.join(s))

class Bot:
    def __init__(self, PostalCode, Years, Username):
        self._PostalCode = PostalCode
        self._Years = Years
        self._Pseudo = Username
        self._driver = webdriver.Firefox(executable_path=DriverPath)
        self._bot = cleverbotfree.cbfree.Cleverbot()

    def ConnexionChat(self):
        self._driver.get(Website)
        window_before = self._driver.window_handles[0]
        self._driver.find_element_by_id("zipo").send_keys(self._PostalCode)
        self._driver.find_element_by_id("ageu").send_keys(self._Years)
        self._driver.find_element_by_id("nicko").send_keys(self._Pseudo)
        self._driver.find_element_by_id("femme").click()
        self._driver.find_element_by_id("tchater").click()
        self._driver.switch_to_window(window_before)
        self._driver.close()
        self._driver.switch_to_window(self._driver.window_handles[0])

    def Interpretation(self, discution, username):
        discution = listToString(discution.encode("utf-8"))
        print("dial total", discution)
        user_send = discution.rsplit('\n', 1)
        print("dernier message ->", user_send)
        user_send = listToString(user_send)
        user_send = user_send.split(':')
        print("after split :", user_send)
        user_send = listToString(user_send[-1])
        print("user say ->", user_send)
        try:
            msg = self._bot.single_exchange(user_send)
        except:
            msg = "none"
        print("bot say ->", msg)
        return msg

    def SpeakWithPeople(self):
        print("Wait 1 min...")
        sleep(60)
        i = 1
        message = "Salut, cava ?"
        while True:
            if (i > MAX_DIAL):
                i = 1
            try:
                username = self._driver.find_element_by_id("ongun"+str(i)).text
                print("go speak with id ->", i, "And username ->", username)
                self._driver.find_element_by_id("ongun"+str(i)).click()
                elements = self._driver.find_elements_by_id("textum")
                for e in elements:
                    message = self.Interpretation(e.text, username)
                if (message != "none"):
                    self._driver.find_element_by_id("cocoa").send_keys(message)
                    self._driver.find_element_by_id("cocoa").send_keys(Keys.RETURN)
                    sleep(2)
            except NoSuchElementException:
                print("d = ", i)
                i = 0
                sleep(10)
            i = i + 1

    def Start(self):
        self.ConnexionChat()
        self.SpeakWithPeople()

    def Finish(self):
        self._driver.quit()