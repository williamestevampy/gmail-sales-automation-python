import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

# 1. DEFINIR CAMINHOS COM AUTONOMIA
nome_usuario = os.getlogin() # Captura "William Estevam" automaticamente do Windows
caminho_excel = rf'C:\Users\{nome_usuario}\Desktop\Codigos\teste.xlsx'
# Criamos uma pasta exclusiva para o robô não conflitar com seu Chrome de trabalho
perfil_robo = rf'C:\Users\{nome_usuario}\AppData\Local\Google\Chrome\User Data\Automacao'

# 2. CARREGAR BASE DE DADOS
try:
    df = pd.read_excel(caminho_excel)
    print(f"✅ Planilha carregada com {len(df)} contatos.")
except Exception as e:
    print(f"❌ Erro ao ler planilha: {e}")
    exit()

# 3. CONFIGURAR CHROME PARA USO AUTÔNOMO
options = Options()
options.add_experimental_option("detach", True) # Mantém aberto após o envio
options.add_argument(f"--user-data-dir={perfil_robo}") # Pasta exclusiva do robô
options.add_argument("--profile-directory=Default")
options.add_argument("--start-maximized") # Abre em tela cheia para facilitar achar botões

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)

print("🚀 Navegador iniciado. Se for a primeira vez, faça login no Gmail.")

# 4. LOOP DE ENVIO
for index, linha in df.iterrows():
    email_cliente = linha['Email']
    nome_cliente = linha['Nome']

    # Vai direto para a tela de novo e-mail para ganhar tempo
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    
    # Na primeira rodada, o script espera você logar. Se já estiver logado, ele segue.
    time.sleep(7) 

    try:
        # Localiza campo 'Para'
        campo_para = driver.find_element(By.NAME, "to")
        campo_para.send_keys(email_cliente)
        campo_para.send_keys(Keys.ENTER)
        time.sleep(1)

        # Localiza campo 'Assunto'
        assunto = f"Novo representante Newpen | Olá {nome_cliente}"
        driver.find_element(By.NAME, "subjectbox").send_keys(assunto)
        time.sleep(1)

        # Escreve a mensagem
        corpo = f"Olá {nome_cliente}, tudo bem?\n\nMeu nome é William e sou o seu novo representante comercial da Newpen."
        campo_corpo = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Corpo da mensagem']")
        campo_corpo.send_keys(corpo)
        
        # Pequena pausa para simular digitação humana
        time.sleep(2)

        # Comando de envio (Ctrl + Enter)
        campo_corpo.send_keys(Keys.CONTROL + Keys.ENTER)
        
        print(f"✅ Enviado: {nome_cliente} ({email_cliente})")
        time.sleep(4) # Delay de segurança para não ser bloqueado como spam

    except Exception as e:
        print(f"⚠️ Erro ao processar {email_cliente}. Verifique se o Gmail está aberto e logado.")

print("\n--- 🏁 PROCESSO FINALIZADO ---")