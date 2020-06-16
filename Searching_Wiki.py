#Searching_Wiki_Final

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


user_search = input("what would you like to search for in Wikipedia: ")

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

search_field = driver.find_element_by_name('q')       
search_field.send_keys("wikipedia")

search_button = WebDriverWait(driver, 1).until(
EC.element_to_be_clickable((By.NAME,'btnK'))) 

search_button.click()                                                                                                                 

link_block = driver.find_elements_by_class_name('r')
first_link_element = link_block[0]

wiki_link = first_link_element.find_element_by_tag_name('h3')
wiki_link.click()

search_wiki_field = driver.find_element_by_id('searchInput')            
search_wiki_field.send_keys(user_search)


search_wiki_button = driver.find_element_by_class_name('pure-button')
search_wiki_field.click()


driver.quit()
