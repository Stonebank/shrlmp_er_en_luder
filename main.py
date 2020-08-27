import time
import subprocess
import re

from selenium import webdriver

browser = webdriver.Safari()
browser.maximize_window()
browser.get("https://www.runescape.com/community")
time.sleep(2)

browser.find_element_by_link_text("Old School").click()
time.sleep(2)

players = re.sub('[^0-9]', '', browser.find_element_by_class_name("player-count").text)

subprocess.run(["say", f"Der er {players} på Oldschool RuneScape in my dick"])

browser.find_element_by_link_text("HiScores").click()
time.sleep(2)

browser.find_element_by_name("user1").send_keys("shrlmp")
browser.find_element_by_name("submit").click()
time.sleep(2)

subprocess.run(["say", "Jasser er en luder"])