import pandas as pd

df = pd.read_csv("Bia - Atividades/Prova/saneago_colera_2025.csv") 

df = df.drop_duplicates()

df["populacao_atendida"] = pd.to_numeric(df["populacao_atendida"], errors="coerce")
df["casos_suspeitos"] = pd.to_numeric(df["casos_suspeitos"], errors="coerce")

df["data_coleta"] = pd.to_datetime(df["data_coleta"], errors="coerce")

df["regiao"] = df["regiao"].astype(str).str.strip().str.title()

df["casos_suspeitos"] = df["casos_suspeitos"].fillna(0)

df = df[df["populacao_atendida"] > 0]
df = df.dropna(subset=["regiao", "data_coleta"])


df["incidencia"] = df["casos_suspeitos"] / df["populacao_atendida"]


def alerta(x):
    if x < 0.01:
        return "Normal"
    elif x < 0.03:
        return "Atenção"
    elif x < 0.06:
        return "Alerta"
    else:
        return "Crítico"

df["nivel_alerta"] = df["incidencia"].apply(alerta)


resumo = df.groupby("regiao").agg(
    taxa_media_incidencia=("incidencia", "mean"),
    total_casos=("casos_suspeitos", "sum"),
    quantidade_cds=("id_cd", "count")
).round(4).reset_index()

distribuicao = df.groupby(["regiao", "nivel_alerta"]).size().reset_index(name="quantidade")


print("\nResumo po região")
print(resumo)

print("\nDistribuição por alertas")
print(distribuicao)