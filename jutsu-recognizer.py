estado_inicial = "q0"
estados_finais = ["qf", "qf2"]
estados_finais = ["qf1", "qf2", "qf3", "qf4", "qf5", "qf6"]

alfabeto = [
    "cobra", "dragao", "coelho", "tigre",
    "cavalo", "boi", "macaco"
]
transicoes = {
    ("q0", "cobra"): ["q1"],
    ("q1", "dragao"): ["q2"],

   
    ("q2", "coelho"): ["q3"],
    ("q3", "tigre"): ["qf1"],  
    ("q3", "cachorro"): ["qf2"],  

   
    ("q2", "tigre"): ["qf3"],  

    
    ("q0", "cavalo"): ["q10"],
    ("q10", "dragao"): ["q11"],
    ("q11", "boi"): ["q12"],
    ("q12", "tigre"): ["qf4"],

    
    ("q0", "boi"): ["q20"],
    ("q20", "cobra"): ["q21"],

    ("q21", "cachorro"): ["qf5"],
    ("q21", "dragao"): ["q22"],
    ("q22", "rato"): ["qf6"],
}   

jutsu_por_estado = {
    "qf1": "Katon: Goukakyuu",
    "qf2": "Katon: Housenka",
    "qf3": "Raiton: Chidori",
    "qf4": "Suiton: Suiryuudan",
    "qf5": "Doton: Doryuheki",
    "qf6": "Doton: Doryuudan"
}

def executar_afnd(entrada):
    estados_atuais = {estado_inicial}

    for simbolo in entrada:
        novos_estados = set()

        for estado in estados_atuais:
            chave = (estado, simbolo)

            if chave in transicoes:
                novos_estados.update(transicoes[chave])

        estados_atuais = novos_estados

        if not estados_atuais:
            return "Sequência inválida"

    # Verifica se terminou em estado final
    for estado in estados_atuais:
        if estado in estados_finais:
            return f"Jutsu reconhecido: {jutsu_por_estado[estado]}"
    return "Sequência incompleta"

#entrada = ["cobra", "dragao", "coelho", "tigre"]
#entrada = ["cobra", "dragao", "coelho", "cachorro"]
#entrada = ["cobra", "dragao", "tigre"]
entrada = ["boi", "cobra", "dragao", "rato"]

print(executar_afnd(entrada))
