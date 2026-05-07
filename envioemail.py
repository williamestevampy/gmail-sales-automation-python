import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. CONFIGURAÇÃO DE CAMINHOS
nome_usuario = os.getlogin()
caminho_excel = rf'C:\Users\{nome_usuario}\Desktop\Codigos\teste.xlsx'
perfil_robo = rf'C:\Users\{nome_usuario}\AppData\Local\Google\Chrome\User Data\Automacao'

# 2. CARREGAR PLANILHA
df = pd.read_excel(caminho_excel)

# 3. CONFIGURAR NAVEGADOR (COM DISFARCE)
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f"--user-data-dir={perfil_robo}")
options.add_argument("--profile-directory=Default")

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)

# Disfarce extra via Script
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# 4. PASSO CRÍTICO: LOGIN MANUAL
print("🟡 Verificando login... Se o Chrome abrir deslogado, faça o login manualmente AGORA.")
driver.get("https://mail.google.com/")
time.sleep(5) # Tempo para você conferir se está logado

# 5. LOOP DE ENVIO
for index, row in df.iterrows():
    email_cliente = row['Email']
    nome_cliente = row['Nome']

    print(f"📧 Enviando para: {nome_cliente}...")

    # LINK DIRETO: Já abre o Gmail com a caixinha de "Nova Mensagem" aberta
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    
    # Espera o Gmail carregar a janelinha (tempo vital)
    time.sleep(8)

    try:
        # Quando abrimos o link acima, o cursor JÁ FICA piscando no campo "Para"
        # Então usamos o "switch_to.active_element" para escrever direto
        actions = webdriver.ActionChains(driver)
        
        # 1. Digita o e-mail no campo que já está focado
        actions.send_keys(email_cliente)
        actions.perform()
        time.sleep(1)
        actions.send_keys(Keys.ENTER).perform() # Fixa o e-mail
        print("   - E-mail inserido.")
        time.sleep(2)

        # 2. Clicar no Assunto (usando um localizador mais genérico que não muda)
        # Procuramos por qualquer campo que tenha o nome 'subjectbox' ou o placeholder 'Assunto'
        try:
            campo_assunto = driver.find_element(By.XPATH, "//input[@name='subjectbox' or @placeholder='Assunto']")
            campo_assunto.click()
        except:
            # Se não achar por nome, tenta o TAB (plano B)
            actions.send_keys(Keys.TAB).perform()
        
        time.sleep(1)
        
        # 3. Escreve o Assunto
        assunto = f"Novo representante Newpen | Olá {nome_cliente}"
        actions = webdriver.ActionChains(driver)
        actions.send_keys(assunto).perform()
        print("   - Assunto inserido.")
        time.sleep(1)

        # 4. TAB para ir para o corpo
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)

        # 5. Escreve a mensagem
        corpo = f"Olá {nome_cliente}, tudo bem?\n\nMeu nome é William e sou o seu novo representante comercial da Newpen."
        actions.send_keys(corpo).perform()
        print("   - Corpo da mensagem inserido.")
        time.sleep(2)

        # 6. Enviar (Ctrl + Enter)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print(f"✅ Sucesso total para {email_cliente}!")
        time.sleep(5) 

    except Exception as e:
        print(f"❌ Falha técnica no envio para {nome_cliente}. Detalhe: {e}")
        continue

print("\n--- 🏁 PROCESSO FINALIZADO ---")