import pyautogui
import time
import pyperclip  

link = "https://mail.google.com/mail/u/1/#inbox"

# Abre o navegador
pyautogui.press("win")
time.sleep(1)
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)

# Acessa o Gmail
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5) # Aumentei um pouco para garantir o carregamento

# Clica em Escrever
pyautogui.click(x=109, y=213)
time.sleep(2)
pyautogui.click(x=1303, y=472)
pyautogui.write("arnaldo.adm@polgrymas.com.br")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)

# Assunto (Usando Copiar e Colar para garantir os acentos)
pyautogui.click(x=1279, y=519)
assunto = "Novo representante Newpen | Atendimento personalizado para você"
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# Corpo do E-mail (Usando Copiar e Colar)
pyautogui.click(x=1294, y=550)
corpo = """Olá, tudo bem?
Meu nome é William e, a partir de agora, sou o seu novo representante comercial da Newpen.

Quero me colocar à disposição para oferecer um atendimento mais próximo, ágil e eficiente, entendendo suas necessidades e trazendo as melhores soluções em papelaria para o seu negócio.

A Newpen se destaca pela qualidade dos produtos, inovação constante e excelente custo-benefício — sempre com foco em ajudar nossos clientes a vender mais e melhor.

Será um prazer construir uma parceria sólida com você. Em breve entro em contato, mas se preferir, já fico à disposição por aqui para qualquer dúvida ou pedido.

Conte comigo!"""

pyperclip.copy(corpo) # Copia o texto com acentos
pyautogui.hotkey('ctrl', 'v') # Cola o texto no Gmail
time.sleep(2)

# Enviar
pyautogui.click(x=1304, y=999)
# Arquivo csv e envio de varios e-mails
import pandas as pd

email = pd.read_excel('C:\\Users\\William Estevam\\Desktop\\Codigos\\teste.xlsx')

