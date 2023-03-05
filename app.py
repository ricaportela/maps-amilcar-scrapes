from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager # by ricaportela
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException # by ricaportela
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
from parsel import Selector
from time import sleep
import pandas as pd
import json


def driver_open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--incognito') 
    #options.add_argument('user-agent=User-Agent:Chrome/98.0.4758.102') #Chrome/98.0.4758.102
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"+"AppleWebKit/537.36 (KHTML, like Gecko)"+"Chrome/87.0.4280.141 Safari/537.36")
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) # by ricaportela
    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
    driver.set_window_size(1920,1080)
    driver.set_window_position(0,0)
    sleep(2)
    return driver


def page_down(driver):
    actions = ActionChains(driver)
    actions.pause(0.3)
    actions.send_keys(Keys.PAGE_DOWN)
    actions.perform()


def page_up(driver):
    actions = ActionChains(driver)
    actions.pause(0.3)
    actions.send_keys(Keys.PAGE_UP)
    actions.perform()


def get_results():
    results = []

    while True:
        page_content = driver.page_source
        response = Selector(page_content)
        if response.xpath('//*/text()[contains(., "Você chegou ao final da lista.")]'):
            page_content = driver.page_source
            response = Selector(page_content)
            divs = response.xpath(
                '//div[contains(@aria-label, "Resultados")]/div/div[./a]'
            )
            for div in divs:
                results.append({"Descricao": div.xpath("./a/@aria-label").get()})

            break
        else:
            page_down(driver)

    return results


driver = driver_open_browser()
url = "https://www.google.com/maps/search/barbearia+em+Joinville+-+SC/@-26.291605,-48.8471082,13z"

driver.get(url)

results = get_results()

json_string = json.dumps(results)
df = pd.read_json(json_string)

df.to_json("dados.json", orient="records")
# obj_json = json.loads(json_string)

# # grava o objeto JSON em um arquivo
# with open('dados.json', 'w') as f:
#     json.dump(obj_json, f)

#print(results)
