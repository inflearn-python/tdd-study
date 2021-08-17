from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# browser = webdriver.Chrome('C:/Users/user/PycharmProjects/chromedriver.exe')
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('http://localhost:8000')

assert 'Congratulations!' in browser.title
