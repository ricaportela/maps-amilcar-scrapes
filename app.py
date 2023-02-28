from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from parsel import Selector
from time import sleep
import pandas as pd
import json


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


driver = webdriver.Chrome()
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

print(results)
