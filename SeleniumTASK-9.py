#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_service = ChromeService(r"D:\GUVI\Selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#To set up the Webdriver and store into variable
driver = webdriver.Chrome(service=chrome_service)

#To Get the Webpage
driver.get("https://www.saucedemo.com/")

#To Maximize the Window
driver.maximize_window()

#To Print the Title of the Webpage
print("Title of the Webpage:",driver.title)

#To Print the URL of the Webpage
print("Current URL of the WebPage:",driver.current_url)

#To assign Entire contents of the Webpage
pagecontents=driver.page_source

#Save the Entire contents of the Webpage
with open("Webpage_task_11.txt","w",encoding="utf-8") as file:
    file.write(pagecontents)
print("Webpage content extracted and saved in a Text file - Webpage_task11.txt Successfully!!!")


# In[ ]:





# In[ ]:




