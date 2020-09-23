from selenium import webdriver
#pip install selenium 



second = input("What test do you wish to MASTER?\nOptions include:\n1 second,2 seconds,5 seconds\n10 seconds, 15 seconds 30 seconds\n60 seconds 100 seconds\nAnswer should ONLY be the number...\n>")
cps = f"https://cpstest.org/{second}-seconds.php"
driver = webdriver.Chrome(executable_path= r'C:\Users\Kieronia\Downloads\chromedriver.exe') #MAKE SURE TO PUT YOUR CHROMEDRIVER PATH HERE

driver.get(cps)


input("Press enter once the page has loaded.\n>")



driver.find_element_by_xpath('//*[@id="start"]').click()

    

while True:
    driver.find_element_by_xpath('//*[@id="clickarea"]').click()
