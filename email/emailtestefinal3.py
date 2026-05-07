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
from selenium.webdriver.common.action_chains import ActionChains

# 1. CONFIGURAÇÃO DE CAMINHOS
nome_usuario = os.getlogin()
caminho_arquivo = r"C:\Users\William Estevam\Desktop\Codigos\LISTA DE CLIENTE 2 - NEWPEN.xlsx"
perfil_robo = rf'C:\Users\{nome_usuario}\AppData\Local\Google\Chrome\User Data\Automacao'

# 2. CARREGAR PLANILHA E TRATAR COLUNAS
try:
    df = pd.read_excel(caminho_arquivo)
    
    # TRUQUE DE MESTRE: Transforma todos os nomes de colunas em MAIÚSCULO e remove espaços
    # Assim, não importa se no Excel está 'Email', 'email' ou 'EMAIL', o código vai achar.
    df.columns = [str(col).strip().upper() for col in df.columns]
    
    print("✅ Planilha carregada com sucesso!")
    print(f"Colunas detectadas (padronizadas): {list(df.columns)}")
except Exception as e:
    print(f"❌ Erro ao carregar o arquivo Excel: {e}")
    exit()

# 3. CONFIGURAR NAVEGADOR
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f"--user-data-dir={perfil_robo}")
options.add_argument("--profile-directory=Default")

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# 4. PASSO CRÍTICO: LOGIN MANUAL
print("\n🟡 Verificando login... Se o Chrome abrir deslogado, faça o login manualmente AGORA.")
driver.get("https://mail.google.com/")
time.sleep(10) 

# 5. LOOP DE ENVIO
for index, row in df.iterrows():
    try:
        # Agora o código sempre busca por 'EMAIL' e 'NOME' pois padronizamos acima
        email_cliente = str(row['EMAIL']).strip()
        nome_cliente = str(row['NOME']).strip()

        print(f"\n📧 Enviando para: {nome_cliente} ({email_cliente})...")

        driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
        time.sleep(8)

        actions = ActionChains(driver)
        
        # 1. Digita o e-mail
        actions.send_keys(email_cliente)
        actions.perform()
        time.sleep(1.5)
        actions.send_keys(Keys.ENTER).perform() 
        time.sleep(2)

        # 2. Ir para o Assunto
        try:
            campo_assunto = driver.find_element(By.XPATH, "//input[@name='subjectbox' or @placeholder='Assunto']")
            campo_assunto.click()
        except:
            actions.send_keys(Keys.TAB).perform()
        
        time.sleep(1)
        
        # 3. Digitar Assunto
        assunto_novo = f"🚀 Novidades Newpen: Sou seu novo contato, {nome_cliente}!"
        actions = ActionChains(driver)
        actions.send_keys(assunto_novo).perform()
        time.sleep(1)

        # 4. TAB para ir para o corpo
        actions.send_keys(Keys.TAB).perform()
        time.sleep(1)

        # 5. Corpo da Mensagem
        corpo_novo = f"""Olá, {nome_cliente}! Tudo bem?

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

        actions = ActionChains(driver)
        actions.send_keys(corpo_novo).perform()
        time.sleep(3)

        # 6. Enviar (Ctrl + Enter)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print(f"✅ Sucesso total para {email_cliente}!")
        time.sleep(5)

    except KeyError as e:
        print(f"❌ Erro: Coluna não encontrada! Verifique se sua planilha tem as colunas 'Nome' e 'Email'.")
        break 
    except Exception as e:
        print(f"❌ Falha técnica no envio para {row.get('NOME', 'Cliente')}. Detalhe: {e}")
        continue

print("\n--- 🏁 PROCESSO FINALIZADO ---")