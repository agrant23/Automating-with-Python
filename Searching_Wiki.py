#Searching_Wiki through google with a user search. 

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http:google.com")

user_search = input("what would you like to search? ")

search_box = driver.find_element_by_name('q')       #XPath < CSS < Links Text < Name < ID

search_box.send_keys("wikipedia")

driver.implicitly_wait(30)

search_button = driver.find_element_by_name("btnK")

search_button.click()

wiki = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/h3')    #wiki = driver.find_element_by_link_text('Wikipedia') couldn't make this work?

wiki.click()

search_wiki_box = driver.find_element_by_name('search')

search_wiki_box.send_keys(user_search)

driver.implicitly_wait(30)

search_wiki_box.submit()                                                    #is using this a poor coding procedure?  couldn't use #wiki_search_button = driver.find_element_by_name("go")

view_history = driver.find_element_by_link_text('View history')             #this is just for fun.

view_history.click()

#maybe use view_history.submit()   since it's the final method.