from flask import Flask, render_template
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_selenium')
def start_selenium():
    options = Options()
    options.add_experimental_option("detach", True)

    # Install the chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    # Link to be opened
    driver.get("https://www.digitalocean.com/company/contact/abuse#intrusion")
    agree = driver.find_element_by_xpath('//*[@id="truste-consent-button"]')
    agree.click()

    return 'Selenium code started!'

if __name__ == '__main__':
    app.run()
