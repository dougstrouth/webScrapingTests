# reddit.py
from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841')
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://reddit.com')

topLinks = driver.find_elements_by_xpath("//div/p/a[contains(@class, 'title')]")

for link in topLinks:
  print ('Title: ', link.text)

driver.quit()