import random


def linhas():
    print("-" * 70)

# TÍTULO
print("SORTEADOR DE NOMES PARA FORMAÇÃO DE TIMES")
print()

# PRIMEIRO NOME
nome = input("Digite um nome: ").title().strip()
lista_nomes = []
lista_nomes.append(nome)
linhas()

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
            random.shuffle(lista_nomes)
            print()
            print("NOMES REGISTRADOS")
            for c in lista_nomes:
                print(c)
            print()
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
            print("ERRO!2")

    except:
        print("ERRO!")

print()
print("FIM")