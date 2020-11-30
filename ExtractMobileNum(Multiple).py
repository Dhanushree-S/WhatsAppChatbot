from selenium import webdriver
import time

def new_chat(keyword):
    search_icon = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/button')
    time.sleep(5)
    search_icon.click() 
    
    search_string = chrome_browser.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
    time.sleep(5)
    search_string.send_keys(keyword)
    
def extract():
    more = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div')
    time.sleep(5)
    more.click()
    time.sleep(5)
    contact_info= chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/ul/li[1]')
    time.sleep(5)
    contact_info.click()
    time.sleep(5)
    mob_no = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[4]/div[3]/div/div/span').text
    time.sleep(5)
    print(mob_no)
    time.sleep(5)
    
    
chrome_browser = webdriver.Chrome(executable_path='D:\chromedriver')
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(20)

keyword = "Hello_chatbot"
    
try:
    new_chat(keyword)
    try:
        msg_category = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]')
        time.sleep(5)
        try:
            if msg_category:
                i = 2
                try:
                    user_name = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div['+str(i)+']')
                    time.sleep(5)
                    try:
                        while user_name:
                            user_name.click()
                            time.sleep(5)
                            extract()
                            i+=1
                            try:
                                user_name = chrome_browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div['+str(i)+']')
                            except:
                                break
                    except:
                        print("Exception caught 4")
                except:
                    print("Exception caught 3")
        except:
            print("Exception caught 2")
    except:
        print("Exception caught 1")
    
except:
    print("Exception caught")
    