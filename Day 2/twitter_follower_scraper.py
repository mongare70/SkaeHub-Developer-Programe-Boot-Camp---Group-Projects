from selenium import webdriver
from selenium.common.exceptions import WebDriverException,NoSuchElementException


handle = input('Enter the handle here: ')


web_driver = webdriver.Chrome()

#setting timeout before raisng an exception
web_driver.implicitly_wait(100)

url = 'http://twitter.com/'+handle


#check incase of an error
def get_twitter_followers():
    try:
        web_driver.get(url)

    #raise error 
    except WebDriverException as e:
        return "An error occured ", e


    else:
        try:
            #opens the profile of the user
            web_element = web_driver.find_element_by_xpath('//a[@href="/' + handle + '/followers"]')
    
        #checks for an error
        except NoSuchElementException as e:
            return "An error occured ", e

        #prints the number of followers 
        else:
            return web_element.text

print(get_twitter_followers())