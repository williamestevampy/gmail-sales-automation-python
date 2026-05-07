import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# --- 1. CONFIGURAÇÃO DE CAMINHOS ---
nome_usuario = os.getlogin()
# O seu novo caminho especificado:
caminho_arquivo = r"C:\Users\William Estevam\Desktop\Codigos\main.py\clientes.xlsx"
# Perfil isolado para o robô:
perfil_robo = rf'C:\Users\{nome_usuario}\AppData\Local\Google\Chrome\User Data\Automacao'

# --- 2. CARREGAR E LIMPAR PLANILHA ---
try:
    # Lemos a planilha
    df = pd.read_excel(caminho_arquivo)
    # Limpa espaços invisíveis nos nomes das colunas
    df.columns = df.columns.str.strip()
    # Remove linhas onde o e-mail está em branco
    df = df.dropna(subset=['E-mail'])
    print(f"✅ Lista carregada com sucesso! {len(df)} contatos encontrados.")
except Exception as e:
    print(f"❌ Erro ao ler a planilha no novo caminho: {e}")
    print(f"Verifique se o arquivo está realmente em: {caminho_arquivo}")
    exit()

# --- 3. CONFIGURAR NAVEGADOR (MODO SEGURO) ---
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f"--user-data-dir={perfil_robo}")
options.add_argument("--profile-directory=Default")
options.add_argument("--start-maximized")

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)
# Disfarce para o Google não detectar o robô
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# --- 4. VERIFICAÇÃO DE LOGIN ---
print("🟡 Abrindo Gmail... Verifique se o login está ativo.")
driver.get("https://mail.google.com/")
time.sleep(10) # Tempo para carregamento inicial

# --- 5. LOOP DE ENVIO PROFISSIONAL ---
for index, row in df.iterrows():
    email_cliente = str(row['E-mail']).strip()
    nome_fantasia = str(row['Fantasia']).strip()

    # Ignora e-mails inválidos
    if "@" not in email_cliente or email_cliente == "nan":
        continue

    print(f"📧 Preparando envio para: {nome_fantasia}...")
    
    # Abre a caixa de nova mensagem diretamente
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    time.sleep(8) # Aguarda a janelinha de escrita carregar

    try:
        actions = ActionChains(driver)

        # PASSO 1: Digitar o E-mail e fixar com Enter
        actions.send_keys(email_cliente)
        actions.perform()
        time.sleep(1.5)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)

        # PASSO 2: Ir para o campo Assunto (TAB) e preencher
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)
        
        assunto = f"🚀 Novidades Newpen: Sou seu novo contato, {nome_fantasia}!"
        actions.send_keys(assunto).perform()
        time.sleep(1)

        # PASSO 3: Ir para o Corpo do e-mail (TAB)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)

        # TEXTO REFORÇADO E PROFISSIONAL
        corpo_email = f"""Olá, {nome_fantasia}! Tudo bem?

Espero que sua semana esteja sendo excelente!

Meu nome é William e estou entrando em contato para me apresentar oficialmente como seu novo representante comercial da Newpen. A partir de agora, serei seu ponto de apoio para garantir que sua loja tenha sempre os melhores lançamentos e condições exclusivas.

A Newpen é sinônimo de inovação e qualidade, e meu objetivo é trabalhar ao seu lado para que nossos produtos continuem sendo um sucesso de vendas em seu balcão.

Estou à sua inteira disposição para:
✅ Consultas de estoque e novos pedidos;
✅ Envio do nosso catálogo atualizado;
✅ Apresentação de lançamentos e promoções do mês.

Como estão as coisas por aí? Se precisar de qualquer material ou quiser bater um papo sobre como podemos fortalecer nossa parceria, é só me chamar!

Um grande abraço e ótimas vendas,

William Estevam
Representante Comercial | Newpen"""

        actions.send_keys(corpo_email).perform()
        time.sleep(3)

        # PASSO 4: Comando de envio (Ctrl + Enter)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print(f"✅ Sucesso: E-mail enviado para {nome_fantasia}!")
        time.sleep(7) # Pausa de segurança entre clientes

    except Exception as e:
        print(f"❌ Falha técnica ao processar {nome_fantasia}: {e}")
        continue

print("\n--- 🏁 PROCESSO FINALIZADO ---")