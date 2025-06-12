# arquivo: main.py
from fastapi import FastAPI
import random

app = FastAPI()

# Função para gerar CPF válido
def gerar_cpf():
    def calcular_digito(cpf_parcial):
        peso = len(cpf_parcial) + 1
        soma = sum(int(digito) * (peso - i) for i, digito in enumerate(cpf_parcial))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    # Gera os primeiros 9 dígitos
    cpf = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    cpf += calcular_digito(cpf)
    cpf += calcular_digito(cpf)
    return cpf

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API geradora de CPF!"}

@app.get("/gerar-cpf")
def gerar():
    cpf = gerar_cpf()
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return {"cpf": cpf_formatado}
