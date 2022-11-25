# selenium - framework for acessing the browser
# pyttsx3 acessing the voices in microsoft os based


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
PathofDriver = "Driver/chromedriver.exe"
driver = webdriver.Chrome(PathofDriver,options=chrome_options)
driver.maximize_window()

Website = f'https://ttsmp3.com/text-to-speech/British%20English/'

driver.get(Website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('US English / Joanna')

def speak(Text):
    print("")
    print(f" AI :{Text}.")
    print("")
    Data = str(Text)
    xpathtec = '/html/body/div[4]/div[2]/form/textarea'
    driver.find_element(by=By.XPATH,value=xpathtec).send_keys(Data)
    driver.find_element(by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
    sleep(2)

speak('Good Evening BOSS, This is Friday. Its 2:56 P.M. The weather in Goa is 74 degrees with scattered clouds.The weather conditions are fair with waist to shoulder highlines,high tide will be at 10:52 a.m, Have a Nice day BOSS')
