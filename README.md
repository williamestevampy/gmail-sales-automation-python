🚀 Automador de E-mails para Vendas (Python & Selenium)
Este é o meu primeiro projeto de automação, desenvolvido para otimizar o fluxo de trabalho de um representante comercial. O script automatiza o envio de e-mails de apresentação personalizados via Gmail, extraindo os dados diretamente de uma planilha Excel.

📋 O Problema
O envio manual de dezenas de e-mails de apresentação para novos clientes consumia muito tempo e era sujeito a erros humanos, como esquecer de trocar o nome do cliente ou cometer erros de digitação nos endereços.

✨ Funcionalidades
Integração com Excel: Lê automaticamente os dados dos clientes diretamente de arquivos .xlsx.

Personalização Dinâmica: Gera o corpo do e-mail inserindo o nome do cliente de forma automática para cada envio.

Tratamento de Dados Robusto: O código padroniza os nomes das colunas da planilha (tratando diferenças entre maiúsculas/minúsculas e espaços extras), evitando erros de leitura.

Simulação Humana: Utiliza a classe ActionChains do Selenium para simular a digitação e pausas, reduzindo as chances de detecção por filtros de spam.

Persistência de Perfil: Utiliza o perfil real do Chrome (user-data-dir) para manter o login do usuário ativo e evitar bloqueios.

🛠️ Tecnologias Utilizadas
Python (Linguagem principal)

Selenium (Automação de navegador)

Pandas (Tratamento de dados e leitura de arquivos Excel)

Webdriver Manager (Gerenciamento automático do ChromeDriver)

⚙️ Como Funciona
O script carrega uma planilha Excel localizada na pasta do projeto.

Ele abre o navegador Chrome utilizando um perfil de usuário pré-configurado.

O programa verifica o login no Gmail.

Para cada linha da planilha, ele acessa o link direto de composição do Gmail (compose=new).

Preenche automaticamente o destinatário, o assunto e o corpo da mensagem.

Realiza o envio seguro através de comandos de teclado (Ctrl + Enter).

⚠️ Aviso Legal
Este projeto foi desenvolvido para fins de estudo e aumento de produtividade pessoal. O uso de automações em plataformas como o Gmail deve seguir rigorosamente os termos de serviço da Google para evitar penalidades na conta do usuário.