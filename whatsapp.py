from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # Mantém o navegador aberto

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=chrome_options)

driver.get("https://web.whatsapp.com")