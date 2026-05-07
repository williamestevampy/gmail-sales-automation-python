import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# ESTA É A LINHA QUE ESTAVA FALTANDO:
from selenium.webdriver.chrome.options import Options 

# Agora o comando abaixo vai funcionar:
options = Options()
# ... resto do código
# --- CONFIGURAÇÃO PARA DISFARÇAR O ROBÔ ---
options = Options()
options.add_experimental_option("detach", True)

# 1. Desativa o modo "robô" que o Google detecta
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 2. Define um User-Agent real (faz o Google achar que é um Windows comum)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# 3. Caminho do seu perfil (mantenha o que criamos antes)
nome_usuario = os.getlogin()
perfil_robo = rf'C:\Users\{nome_usuario}\AppData\Local\Google\Chrome\User Data\Automacao'
options.add_argument(f"--user-data-dir={perfil_robo}")
options.add_argument("--profile-directory=Default")

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)

# 4. Comando extra para esconder o Selenium de vez
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://accounts.google.com/")