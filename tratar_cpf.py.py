import pandas as pd
import os

# Caminho da pasta - OBSERVAR O CAMINHO CORRETO
PASTA = r"C:\Users\Downloads" 

ARQUIVO_ENTRADA = os.path.join(PASTA, "entrada.xlsx")
ARQUIVO_SAIDA = os.path.join(PASTA, "saida.xlsx")

COLUNA_CPF = "CPF"

def limpar_cpf(valor):
    if pd.isna(valor):
        return ""
    
    s = str(valor).strip()
    s = s.replace(".", "").replace("-", "")
    s = "".join(c for c in s if c.isdigit())
    s = s.zfill(11)  # garante 11 dígitos mantendo zeros à esquerda

    return s

# Lê a primeira aba automaticamente
df = pd.read_excel(ARQUIVO_ENTRADA, sheet_name=0, dtype={COLUNA_CPF: "string"})

# Cria nova coluna
df["CPF_LIMPO"] = df[COLUNA_CPF].apply(limpar_cpf)

# Mostra no terminal
print("\n".join(df["CPF_LIMPO"]))

# Salva arquivo novo
df.to_excel(ARQUIVO_SAIDA, index=False)

print("\nArquivo gerado com sucesso em:")
print(ARQUIVO_SAIDA)