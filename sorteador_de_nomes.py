import random


def linhas():
    print("-" * 70)


def msgError():
    print("ERRO! POR FAVOR DIGITE UM VALOR VÁLIDO!")

# TÍTULO
print("SORTEADOR DE NOMES PARA FORMAÇÃO DE TIMES")
print()

# PRIMEIRO NOME
while True:
    try:
        nome = input("Digite um nome: ").title().strip()
        lista_nomes = []
        lista_nomes.append(nome)
        linhas()

        if nome != "":
            break

        else:
            msgError()
            print()

    except:
        msgError()

while True:
    try:
        add_nome = input("Deseja inserir mais um nome? [S/N] ").upper().strip()

        if add_nome == "S":
            nome = input("Digite mais um nome: ").title().strip()
            lista_nomes.append(nome)
            linhas()
            continue

        if add_nome == "N":
            # EMBARALHANDO OS NOMES E EXIBINDO NA TELA
            print()
            print("NOMES REGISTRADOS")
            for c in lista_nomes:
                print(c)
            print()
            random.shuffle(lista_nomes)
            print(f"Total de {len(lista_nomes)} pessoas registradas.")
            print()

            # PEGANDO O NÚMERO TOTAL DE PESSOAS PRA DIVIDIR OS TIMES
            grupo_1 = dict()
            n = 2
            n_div = int(len(lista_nomes) / n)

            # RESULTADO FINAL DOS TIMES
            print("TIME 01")
            for c in lista_nomes[:n_div]:
                print(c)
            print()
            print("TIME 02")
            for c in lista_nomes[n_div:]:
                print(c)
            break

        else:
            msgError()

    except:
        msgError()

print()
print("FIM")