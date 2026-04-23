import re
import random

# Reflexões (ajuste de pronomes)
reflexoes = {
    "eu": "você",
    "você": "eu",
    "me": "te",
    "te": "me",
    "meu": "seu",
    "seu": "meu",
    "minha": "sua",
    "sua": "minha",
    "sou": "é",
    "é": "sou"
}

def refletir(texto):
    palavras = texto.lower().split()
    return " ".join([reflexoes.get(p, p) for p in palavras])


# Estrutura ELIZA (DOCTOR) em português
regras = [
    {
        "keyword": "desculpa",
        "priority": 1,
        "patterns": [
            (r'(.*)', [
                "Por favor, não precisa se desculpar.",
                "Desculpas não são necessárias.",
                "O que você sente quando pede desculpas?"
            ])
        ]
    },
    {
        "keyword": "eu",
        "priority": 5,
        "patterns": [
            (r'eu preciso de (.*)', [
                "Por que você precisa de {0}?",
                "Isso realmente ajudaria você a conseguir {0}?",
                "Você tem certeza que precisa de {0}?"
            ]),
            (r'eu sou (.*)', [
                "Por que você acha que é {0}?",
                "Há quanto tempo você é {0}?",
                "Como você se sente sendo {0}?"
            ]),
            (r'eu estou (.*)', [
                "Há quanto tempo você está {0}?",
                "O que fez você ficar {0}?",
                "Você gosta de estar {0}?"
            ]),
            (r'eu sinto (.*)', [
                "Fale mais sobre esse sentimento.",
                "Você costuma sentir {0} com frequência?",
                "Quando você geralmente se sente {0}?"
            ])
        ]
    },
    {
        "keyword": "você",
        "priority": 4,
        "patterns": [
            (r'você é (.*)', [
                "Por que você acha que eu sou {0}?",
                "Você gostaria que eu fosse {0}?",
                "Talvez você queira que eu seja {0}."
            ])
        ]
    },
    {
        "keyword": "nenhum",
        "priority": 0,
        "patterns": [
            (r'(.*)', [
                "Entendo.",
                "Por favor, continue.",
                "Você pode explicar melhor?",
                "Por que você diz isso?"
            ])
        ]
    }
]


def encontrar_regra(frase):
    frase = frase.lower()

    regras_ordenadas = sorted(regras, key=lambda r: r["priority"], reverse=True)

    for regra in regras_ordenadas:
        if regra["keyword"] in frase:
            return regra

    return next(r for r in regras if r["keyword"] == "nenhum")


def responder(frase):
    regra = encontrar_regra(frase)

    for pattern, respostas in regra["patterns"]:
        match = re.match(pattern, frase)
        if match:
            grupos = match.groups()
            resposta = random.choice(respostas)

            if grupos:
                refletido = refletir(grupos[0])
                return resposta.format(refletido)

            return resposta


# Loop principal
print("ELIZA: Olá. Como você está se sentindo hoje?\n")

while True:
    entrada = input("Você: ")

    if entrada.lower() in ["sair", "exit", "quit"]:
        print("ELIZA: Foi bom conversar com você. Até logo.")
        break

    print("ELIZA:", responder(entrada))