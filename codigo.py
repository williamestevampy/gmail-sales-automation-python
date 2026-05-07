from os import link
import pyautogui
import time
link = "https://mail.google.com/mail/u/1/#inbox"
pyautogui.press("win")
time.sleep(1)
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=113, y=214)
time.sleep(2)
pyautogui.write("bruna.estevam23@gmail.com")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=1279, y=519)
time.sleep(1)
pyautogui.write("Novo representante Newpen | Atendimento personalizado para você")
time.sleep(2)
pyautogui.click(x=1294, y=550)
time.sleep(2)
pyautogui.write("""Olá, tudo bem?
Meu nome é William e, a partir de agora, sou o seu novo representante comercial da Newpen.

Quero me colocar à disposição para oferecer um atendimento mais próximo, ágil e eficiente, entendendo suas necessidades e trazendo as melhores soluções em papelaria para o seu negócio.

A Newpen se destaca pela qualidade dos produtos, inovação constante e excelente custo-benefício — sempre com foco em ajudar nossos clientes a vender mais e melhor.

Será um prazer construir uma parceria sólida com você. Em breve entro em contato, mas se preferir, já fico à disposição por aqui para qualquer dúvida ou pedido.

Conte comigo!""")
time.sleep(10)
pyautogui.click(x=1304, y=999)