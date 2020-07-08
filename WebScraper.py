from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#Use to open the chrome by python
browser = webdriver.Chrome(executable_path="D:\BQ_Assignment\chromedriver",chrome_options=option)

browser.get("https://www.dramexchange.com") #opens website
rows=len(browser.find_elements_by_xpath("//*[@id='tb_NationalDramSpotPrice']/tr"))#count rows
cols =len(browser.find_elements_by_xpath("//*[@id='tb_NationalDramSpotPrice']/tr[1]/td"))# count Columns
print(rows)
print(cols)

# for reading all the rows and column
# for r in range(2, rows+1): #will start reading the data from 2nd row so on
#     for c in range(1, cols+1): #will read column from 1 column and continue till last column
#         value = browser.find_element_by_xpath("//*[@id='tb_NationalDramSpotPrice']/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(value, end="  ")
#     print() #jumping to next line after completion of inner for loop

#Will give exact cell value in 3rd row and 6th column
value =browser.find_element_by_xpath("//*[@id='tb_NationalDramSpotPrice']/tr[3]/td[6]").text
#prints the value listed in column(6)
print(value)