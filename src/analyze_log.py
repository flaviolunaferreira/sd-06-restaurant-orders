import csv
from collections import Counter

maria_pratos = []
arnaldo_hamburguer = 0
joao_pratos = []
pratos = []
joao_dias = []
dias = []
result_pratos = []
result_dias = []


def escreve_no_arquivo(linha_1, linha_2, linha_3, linha_4):
    linha_3 = str(linha_3).strip("[]")
    linha_4 = str(linha_4).strip("[]")
    file = open("data/mkt_campaign.txt", "w+")
    file.write(f"{linha_1}\n")
    file.write(f"{linha_2}\n")
    file.write("{" + f"{linha_3}" + "}\n")
    file.write("{" + f"{linha_4}" + "}\n")


def maria(linha):
    if linha[0] == "maria":
        maria_pratos.append(linha[1])


def arnaldo(linha):
    if linha[0] == "arnaldo":
        if linha[1] == "hamburguer":
            global arnaldo_hamburguer
            arnaldo_hamburguer += 1


def joao(linha):
    if linha[0] == "joao":
        if linha[1] not in joao_pratos:
            joao_pratos.append(linha[1])
        if linha[2] not in joao_dias:
            joao_dias.append(linha[2])


def pratos_dias(linha):
    if linha[1] not in pratos:
        pratos.append(linha[1])
    if linha[2] not in dias:
        dias.append(linha[2])


def pratos_dias_joao(pratos, dias):
    for prato in pratos:
        if prato not in joao_pratos:
            result_pratos.append(prato)
    for dia in dias:
        if dia not in joao_dias:
            result_dias.append(dia)


def analyze_log(path_to_file):
    arquivo = csv.reader(open(path_to_file))
    for linha in arquivo:
        maria(linha)
        arnaldo(linha)
        joao(linha)
        pratos_dias(linha)
    prefer_dish = Counter(maria_pratos).most_common(1)
    pratos_dias_joao(pratos, dias)
    escreve_no_arquivo(
        prefer_dish[0][0], arnaldo_hamburguer, result_pratos, result_dias
    )

    # raise NotImplementedError
