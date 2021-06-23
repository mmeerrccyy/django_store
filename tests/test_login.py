from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://127.0.0.1:8000')


def login(login, password):
    driver.implicitly_wait(10)

    driver.find_element_by_class_name('header-login').click()

    driver.implicitly_wait(10)

    driver.find_element_by_id('id_username').send_keys(login)
    driver.find_element_by_id('id_password').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/form/p[3]/input').click()


if __name__ == '__main__':
    login('selenium_test_user', 'selenium_test_user')
