from selenium import webdriver

browser = webdriver.Firefox(executable_path='./selenium/geckodriver')
browser.get('http://www.ubuntu.com/')

if __name__ == '__main__':
    print("oi")