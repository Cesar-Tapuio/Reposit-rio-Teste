import pandas as pd
from datetime import datetime

df = pd.read_csv("Bia - Atividades/Prova/populacao_imc.csv")
df["data_nascimento"] = pd.to_datetime(df["data_nascimento"])

hoje = datetime.today()

df["idade"] = df["data_nascimento"].apply(
    lambda d: hoje.year - d.year - ((hoje.month, hoje.day) < (d.month, d.day))
)

df["imc"] = df["peso_kg"] / (df["altura_m"] ** 2)

def faixa(i):
    if i < 12:
        return "Crianca"
    elif i <= 17:
        return "Adolescente"
    elif i <= 59:
        return "Adulto"
    else:
        return "Idoso"

df["faixa_etaria"] = df["idade"].apply(faixa)

def class_imc(r):
    imc = r["imc"]
    f = r["faixa_etaria"]

    if f in ["Adulto", "Idoso"]:
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"
    else:
        if imc < 14:
            return "Abaixo do peso"
        elif imc < 22:
            return "Normal"
        elif imc < 27:
            return "Sobrepeso"
        else:
            return "Obesidade"

df["classificacao_imc"] = df.apply(class_imc, axis=1)


contagem = df.groupby(["faixa_etaria", "classificacao_imc"]).size().reset_index(name="quantidade")

percentual = contagem.copy()
percentual["percentual"] = percentual.groupby("faixa_etaria")["quantidade"].transform(lambda x: (x / x.sum()) * 100)
percentual["percentual"] = percentual["percentual"].round(2)


estatisticas = df.groupby(["faixa_etaria", "sexo"])["imc"].agg(
    media="mean",
    mediana="median",
    desvio_padrao="std"
).round(2).reset_index()


df["risco"] = df["classificacao_imc"].isin(["Sobrepeso", "Obesidade"])

risco = df.groupby(["faixa_etaria", "sexo"])["risco"].mean().reset_index()
risco["percentual_risco"] = (risco["risco"] * 100).round(2)
risco = risco.drop(columns="risco").sort_values(by="percentual_risco", ascending=False)


print("\nCONTAGEM")
print(contagem)

print("\nPERCENTUAL")
print(percentual)

print("\nESTATÍSTICAS IMC")
print(estatisticas)

print("\nRISCO")
print(risco)