from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

while True:
    name = input('\nEnter the name of User or Group: ')
    msg = input('\nEnter your Message: ')
    count = int(input('Enter the Count: '))

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_1Plpp')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()

    continue

