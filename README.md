\# CPF Cleaner - Python



Automação em Python para sanitização e padronização de CPFs extraídos de planilhas Excel, preservando integridade e conformidade de dados.



---



\## 🎯 Objetivo



Padronizar CPFs removendo pontuação ('.' e '-') sem alterar o valor numérico, garantindo:



\- Manutenção de zeros à esquerda

\- Formato com 11 dígitos

\- Tratamento seguro como string (evitando perda de dados no Excel)

\- Geração de nova coluna tratada



---



\## 🔎 Funcionalidades



✔ Remove caracteres não numéricos  

✔ Mantém zeros à esquerda  

✔ Garante 11 dígitos  

✔ Processa planilhas `.xlsx`  

✔ Gera arquivo tratado automaticamente  



---



\## 🛠 Tecnologias Utilizadas



\- Python 3.x

\- Pandas

\- OpenPyXL



---



\## 📂 Estrutura Esperada



O script deve estar na mesma pasta do arquivo Excel a ser tratado.



\## ▶ Como Executar



1\. Instale as dependências:



pip install pandas openpyxl



2\. Execute:



python tratar\_cpf.py



3\. O sistema irá gerar:



SAIDA\_TRATADO.xlsx



---



\## 🔐 Boas Práticas Aplicadas



\- Manipulação de CPF como string (evita perda de zeros)

\- Não altera o valor original do dado

\- Geração de nova coluna para preservar rastreabilidade

\- Recomenda-se não versionar planilhas com dados reais (LGPD)



---



\## 📌 Contexto de Aplicação



Ferramenta útil para:



\- Governança de Dados

\- Padronização cadastral

\- Automação administrativa

\- Preparação de base para integração sistêmica

\- Conformidade com boas práticas de tratamento de dados pessoais



---



\## 📜 Licença



Uso educacional e demonstrativo.

