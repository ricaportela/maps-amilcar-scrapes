"""
1. Alteração:
 - foi nao usar o webdriver_manager
 
2. as alteraçoes estao com # by ricaportela 

3. executei o script agora com o chrome, dai ocorreu o erro abaixo

DeprecationWarning: scroll() has been deprecated, please use scroll_to_element(), scroll_by_amount() or scroll_from_origin().
  chain.scroll(x=0, y= 500, delta_x= 0, delta_y= 500, duration= 2, origin= "viewport").pause(3).perform()

with chat gpt help

The warning message indicates that the scroll() method is deprecated and should be replaced with one of the recommended methods: scroll_to_element(), scroll_by_amount(), or scroll_from_origin().

In this case, you can replace the scroll() method with scroll_by_amount() to achieve the same result. Here is an example:

suggestion:

chain.scroll_by_amount(0, 500).pause(3).perform()

Alternatively, if you want to use scroll_to_element() or scroll_from_origin(), you will need to provide a target element or coordinates to scroll to.

Note that the pause() method is used to add a delay between actions in the action chain, so you can keep that in your code if needed.

"""


# The Script below is designed to get details from school sites in LRV 
# Import the libraries
# Declare variables 
# Define the functions
# Open google maps website and type the key words to list the schools in a specific location  
# Get "name", "address", "phone number" and "miscelaneous"
# Reloop the script while the condition is true

# Import the libraries:
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
import pandas as pd

# Declare variables
business_place_list = []
barber_business = {}
business_name = []
business_address = []
business_phone = []
business_type = []
       
def driver_open_browser():
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    options.add_argument('--incognito') 
    #options.add_argument('user-agent=User-Agent:Chrome/98.0.4758.102') #Chrome/98.0.4758.102
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"+"AppleWebKit/537.36 (KHTML, like Gecko)"+"Chrome/87.0.4280.141 Safari/537.36")
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) # by ricaportela
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
    driver.set_window_size(1920,1080)
    driver.set_window_position(0,0)
    sleep(2)
    return driver

####################################################################
##################---MINING_THE_SCHOOLS---######################### 
####################################################################

def page_down(driver):
    chain = ActionChains(driver)
    # chain.scroll(x=0, y= 500, delta_x= 0, delta_y= 500, duration= 2, origin= "viewport").pause(3).perform()
    # chain.scroll(x=0, y= 500, delta_x= 0, delta_y= 500, duration= 2, origin= "viewport").pause(3).perform()
    chain.scroll_by_amount(0, 500).pause(3).perform() # by ricaportela
    chain.scroll_by_amount(0, 500).pause(3).perform() # by ricaportela


# Open Coles website and get the list of products with discount
def mining_barber():
    driver = driver_open_browser()
    #driver.get('https://www.google.com/maps/search/barbearia+bairro+costa+e+silva+em+joinville+-+sc,+brazil/@-26.2952006,-48.8756068,13z/data=!3m1!4b1')
    #driver.get('https://www.google.com/maps/search/barbearia+Bairro+Centro+sorriso+mato+grosso/@-12.5638839,-55.7564769,13.25z/data=!4m2!2m1!6e1')
    urls = ["https://www.google.com/maps/search/barbearias+em+centro+Sorriso%2FMT%09/@-12.5461132,-55.7367596,14.17z", "https://www.google.com/maps/search/barbearias+em+Caravagio+Sorriso%2FMT%09/@-12.5451523,-55.7267377,13.25z", "https://www.google.com/maps/search/barbearias+em+Boa+Esperan%C3%A7a+Sorriso%2FMT%09/@-12.5450082,-55.7267377,13z/data=!3m1!4b1", "https://www.google.com/maps/search/barbearias+em+Primavera+Sorriso%2FMT%09/@-12.5448361,-55.7267378,13z/data=!3m1!4b1", "https://www.google.com/maps/search/barbearias+em+Rota+do+Sol+Sorriso%2FMT%09/@-12.5446639,-55.7267378,13z/data=!3m1!4b1", "https://www.google.com/maps/search/barbearias+em+S%C3%A3o+Domingos+Sorriso%2FMT%09/@-12.5444918,-55.7267378,13z/data=!3m1!4b1"]

    for url in urls:
        driver.get(url)
        sleep(3)
        count = len(driver.find_elements(By.XPATH, "//div[@jstcache='195']"))
        page_down(driver)

        '''
        chain = ActionChains(driver)
        chain.scroll(x=0, y= 500, delta_x= 0, delta_y= 500, duration= 2, origin= "viewport").pause(2).perform()
        chain.scroll(x=0, y= 500, delta_x= 0, delta_y= 500, duration= 2, origin= "viewport").pause(2).perform()
        '''
        while count < len(driver.find_elements(By.XPATH, "//div[@jstcache='195']")):
            count = len(driver.find_elements(By.XPATH, "//div[@jstcache='195']"))
            page_down(driver)
            
            '''
            chain = ActionChains(driver)
            chain.scroll(x=0, y= 500, delta_x= 0, delta_y= 500, duration= 2, origin= "viewport").pause(4).perform()
            chain.scroll(x=0, y= 500, delta_x= 0, delta_y= 500, duration= 2, origin= "viewport").pause(4).perform()
            '''
        print('###########################################')
        print('The total of businness found are: ', count)
        print('###########################################')

    # Apply this condition here "NoSuchElementException" to avoid code crash
        try:
            for element in range(count):
            #for element in range(94,119): # Use this line when you need to debug an especific range of elements
                #chain = ActionChains(driver)
                #chain.scroll(x=0, y= 500, delta_x= 0, delta_y= 500, duration= 2, origin= "viewport").pause(2).perform()  
                page_down(driver)           
                sleep(6) 

                if driver.find_elements(By.XPATH, "//div[@jstcache='195']") is not None:
                    driver.find_elements(By.XPATH, "//div[@jstcache='195']")[element].click()
                    sleep(5)
                    
                    # Name
                    business_name.append(driver.find_element(By.XPATH, "//h1[@class = 'DUwDvf fontHeadlineLarge']").text)
                                        
                    # Address   
                    business_address.append(driver.find_elements(By.XPATH, "//div[@class = 'Io6YTe fontBodyMedium']")[0].text)
                    
                    # Phone Number
                    phone_number_index = len(driver.find_elements(By.XPATH, "//div[@class = 'Io6YTe fontBodyMedium']"))
                    for index in range(phone_number_index):
                        if driver.find_elements(By.XPATH, "//div[@class = 'Io6YTe fontBodyMedium']")[index].text.startswith('+55'):    
                            business_phone.append(driver.find_elements(By.XPATH, "//div[@class = 'Io6YTe fontBodyMedium']")[index].text)
                        #else:
                            #business_phone.append('XXX')
                    if len(business_phone) < len(business_name):
                        business_phone.append('XXX')
                    
                    # Business Type
                    business_type.append(driver.find_element(By.XPATH, "//button[@class = 'DkEaL u6ijk' or @class = 'DkEaL']").text)    
                
                print('')
                print('###########################################')
                print('Current element', element, 'of', count)
                print('###########################################')

                if len(business_address) < len(business_name):
                    print('The address is smaller', business_name[-1])
                elif len(business_phone) < len(business_name):
                    print('The phone is smaller', business_name[-1])
                elif len(business_type) < len(business_name):
                    print('The type is smaller', business_name[-1])         
                sleep(1)     
                
        except NoSuchElementException:  
                pass

def data_frame():
    print('')
    print('###########################################')
    print('#########---CREATING DATAFRAME---##########')
    print('###########################################')

    while len(business_type) < len(business_name):
        business_type.append('XXX')

    while len(business_phone) < len(business_name):
        business_phone.append('XXX') 

    while len(business_address) < len(business_name):
        business_address.append('XXX')    

    barber_business = {
        'NOME' : business_name,
        'ENDERECO' : business_address,
        'TELEFONE' : business_phone,
        'TIPO | CATEGORIA': business_type
    }

    df_barber = pd.DataFrame(barber_business, columns = ['NOME', 'ENDERECO', 'TELEFONE', 'TIPO | CATEGORIA'])
    df_barber.to_csv('barber.csv')

mining_barber()
data_frame()

print('')
print('###########################################')
print('############---FINISH---###################')
print('###########################################')