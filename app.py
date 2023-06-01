from flask import Flask
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

@app.route('/')
def hello():

    options = Options()
    options.add_experimental_option("detach", True)

    #Install the chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.maximize_window()

    #Link to be open
    driver.get("https://www.digitalocean.com/company/contact/abuse#intrusion")
    agree = driver.find_element("xpath",'.//*[@id="truste-consent-button"]')
    agree.click()



    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
