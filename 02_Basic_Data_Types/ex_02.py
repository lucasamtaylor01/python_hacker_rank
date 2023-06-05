# Nested Lists
def acha_min(lista):
    ind_min = 0
    min = lista[ind_min][1]
    for i in range(len(lista)):
        if lista[i][1] < lista[ind_min][1]:
            ind_min = i
            min = lista[ind_min][1]
    return min

def retira_min(lista, min):
    nova_lista = []        
    for i in range(len(lista)):
        if lista[i][1] != min:
            nova_lista.append(lista[i])
    return nova_lista

def imprime_solucao(lista, min):
    for i in range(len(lista)):
        if lista[i][1] == min:
            print(lista[i][0])

def main():
    lista = []
    for i in range(int(input())):
        nome = input()
        pontuacao = float(input())
        lista.append([nome, pontuacao])

    lista = sorted(lista)
    lista_sem_min = retira_min(lista, acha_min(lista))

    novo_min = acha_min(lista_sem_min)
    imprime_solucao(lista_sem_min, novo_min)

main()





