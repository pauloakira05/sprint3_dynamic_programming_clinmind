# SPRINT 3 – Dynamic Programming (ClinMind)
# 2ESPI
# Integrantes:
# Bruno Carneiro Leão - 555563 (2ESPV)
# Guilherme da Cunha Melo - 555310 (2ESPI)
# Matheus Gushi Morioka - 556935 (2ESPI)
# Paulo Akira Okama - 556840 (2ESPI)
# Repositório: https://github.com/pauloakira05/sprint3_dynamic_programming_clinmind.git

# DADOS SIMULADOS (5 registros)
dados = [
    {"id": 1, "nome": "Reagente A",  "lote": "L1001", "validade": "051025", "data": "010925", "qtd": 7},
    {"id": 2, "nome": "Tubo 10ml",   "lote": "L2101", "validade": "201225", "data": "010925", "qtd": 3},
    {"id": 3, "nome": "Reagente B",  "lote": "L1302", "validade": "150126", "data": "020925", "qtd": 11},
    {"id": 4, "nome": "Lamina",      "lote": "L3103", "validade": "010726", "data": "020925", "qtd": 5},
    {"id": 5, "nome": "Caixa Coleta","lote": "L4104", "validade": "100326", "data": "030925", "qtd": 9},
]

# Fila e Pilha iniciais
fila = []
pilha = []
indice_carga = 0
while indice_carga < len(dados):
    fila.append(dados[indice_carga])   # FIFO
    pilha.append(dados[indice_carga])  # LIFO
    indice_carga += 1

# COMPARAÇÃO DE DATA (ddmmyy)
def data_menor_ou_igual(data1, data2):
    dia1 = int(data1[0:2]); mes1 = int(data1[2:4]); ano1 = int(data1[4:6])
    dia2 = int(data2[0:2]); mes2 = int(data2[2:4]); ano2 = int(data2[4:6])
    if ano1 < ano2: return True
    if ano1 > ano2: return False
    if mes1 < mes2: return True
    if mes1 > mes2: return False
    return dia1 <= dia2

# ORDENAÇÃO
def merge_sort_por_qtd(lista):
    if len(lista) <= 1:
        return lista[:]
    meio = len(lista) // 2
    lista_esquerda = merge_sort_por_qtd(lista[:meio])
    lista_direita  = merge_sort_por_qtd(lista[meio:])
    indice_esq = 0
    indice_dir = 0
    resultado = []
    while indice_esq < len(lista_esquerda) and indice_dir < len(lista_direita):
        if lista_esquerda[indice_esq]["qtd"] <= lista_direita[indice_dir]["qtd"]:
            resultado.append(lista_esquerda[indice_esq]); indice_esq += 1
        else:
            resultado.append(lista_direita[indice_dir]); indice_dir += 1
    while indice_esq < len(lista_esquerda):
        resultado.append(lista_esquerda[indice_esq]); indice_esq += 1
    while indice_dir < len(lista_direita):
        resultado.append(lista_direita[indice_dir]); indice_dir += 1
    return resultado

def merge_sort_por_nome(lista):
    if len(lista) <= 1:
        return lista[:]
    meio = len(lista) // 2
    lista_esquerda = merge_sort_por_nome(lista[:meio])
    lista_direita  = merge_sort_por_nome(lista[meio:])
    indice_esq = 0
    indice_dir = 0
    resultado = []
    while indice_esq < len(lista_esquerda) and indice_dir < len(lista_direita):
        if lista_esquerda[indice_esq]["nome"] <= lista_direita[indice_dir]["nome"]:
            resultado.append(lista_esquerda[indice_esq]); indice_esq += 1
        else:
            resultado.append(lista_direita[indice_dir]); indice_dir += 1
    while indice_esq < len(lista_esquerda):
        resultado.append(lista_esquerda[indice_esq]); indice_esq += 1
    while indice_dir < len(lista_direita):
        resultado.append(lista_direita[indice_dir]); indice_dir += 1
    return resultado

def particiona_por_validade(lista, inicio, fim):
    validade_pivo = lista[fim]["validade"]
    indice_menores = inicio - 1
    indice_atual = inicio
    while indice_atual < fim:
        validade_atual = lista[indice_atual]["validade"]
        if data_menor_ou_igual(validade_atual, validade_pivo):
            indice_menores += 1
            temp = lista[indice_menores]
            lista[indice_menores] = lista[indice_atual]
            lista[indice_atual] = temp
        indice_atual += 1
    temp2 = lista[indice_menores + 1]
    lista[indice_menores + 1] = lista[fim]
    lista[fim] = temp2
    return indice_menores + 1

def quick_sort_por_validade(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        posicao_pivo = particiona_por_validade(lista, inicio, fim)
        quick_sort_por_validade(lista, inicio, posicao_pivo - 1)
        quick_sort_por_validade(lista, posicao_pivo + 1, fim)

# BUSCAS
def busca_sequencial_por_nome(lista, nome):
    indices_encontrados = []
    indice = 0
    while indice < len(lista):
        if lista[indice]["nome"] == nome:
            indices_encontrados.append(indice)
        indice += 1
    return indices_encontrados

def busca_sequencial_por_lote(lista, lote):
    indices_encontrados = []
    indice = 0
    while indice < len(lista):
        if lista[indice]["lote"] == lote:
            indices_encontrados.append(indice)
        indice += 1
    return indices_encontrados

def busca_binaria_por_nome(lista_ordenada_por_nome, alvo_nome):
    inicio = 0
    fim = len(lista_ordenada_por_nome) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_no_meio = lista_ordenada_por_nome[meio]["nome"]
        if nome_no_meio == alvo_nome:
            return meio
        if nome_no_meio < alvo_nome:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

# UTIL (mostrar)
def mostrar_um(registro):
    linha = "id=" + str(registro["id"]) + ", nome=" + registro["nome"] + ", lote=" + registro["lote"] \
            + ", validade=" + registro["validade"] + ", data=" + registro["data"] + ", qtd=" + str(registro["qtd"])
    print(linha)

def mostrar(lista):
    # uso para Fila (ordem cronológica)
    indice = 0
    while indice < len(lista):
        mostrar_um(lista[indice])
        indice += 1

def mostrar_pilha(lista):
    # exibe do TOPO para a base (últimos primeiro)
    indice = len(lista) - 1
    while indice >= 0:
        mostrar_um(lista[indice])
        indice -= 1

# MENU
proximo_id = len(dados) + 1

while True:
    print("\n=== CLINMIND | CONTROLE DE INSUMOS ===")
    print("1 - Registrar consumo (adiciona em Fila e Pilha) [datas ddmmyy]")
    print("2 - Atender Fila (FIFO)")
    print("3 - Desfazer último da Pilha (LIFO)")
    print("4 - Mostrar Fila")
    print("5 - Mostrar Pilha (topo primeiro)")
    print("6 – Ordenar por QUANTIDADE (Merge) em todos os dados")
    print("7 – Ordenar por VALIDADE (Quick) em todos os dados")
    print("8 - Busca SEQUENCIAL (por NOME ou LOTE)")
    print("9 - Busca BINÁRIA (por NOME) em lista ordenada por NOME")
    print("0 - Sair")

    opcao_menu = input("Escolha: ")

    if opcao_menu == "1":
        nome = input("Nome do insumo: ")
        lote = input("Lote: ")
        validade = input("Validade (ddmmyy): ")
        data = input("Data do consumo (ddmmyy): ")
        quantidade_texto = input("Quantidade (inteiro): ")

        # valida ddmmyy - validade
        validade_ok = False
        if len(validade) == 6:
            somente_digitos = True
            posicao = 0
            while posicao < 6:
                caractere = validade[posicao]
                if caractere < '0' or caractere > '9':
                    somente_digitos = False
                posicao += 1
            if somente_digitos:
                dia = int(validade[0:2]); mes = int(validade[2:4])
                if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12:
                    validade_ok = True

        # valida ddmmyy - data
        data_ok = False
        if len(data) == 6:
            somente_digitos_data = True
            posicao_data = 0
            while posicao_data < 6:
                caractere_data = data[posicao_data]
                if caractere_data < '0' or caractere_data > '9':
                    somente_digitos_data = False
                posicao_data += 1
            if somente_digitos_data:
                dia_data = int(data[0:2]); mes_data = int(data[2:4])
                if dia_data >= 1 and dia_data <= 31 and mes_data >= 1 and mes_data <= 12:
                    data_ok = True

        # valida quantidade inteira não negativa
        quantidade_ok = False
        if len(quantidade_texto) > 0:
            somente_digitos_qtd = True
            posicao_qtd = 0
            while posicao_qtd < len(quantidade_texto):
                caractere_qtd = quantidade_texto[posicao_qtd]
                if caractere_qtd < '0' or caractere_qtd > '9':
                    somente_digitos_qtd = False
                posicao_qtd += 1
            if somente_digitos_qtd:
                quantidade_ok = True

        if not validade_ok:
            print("Validade inválida. Use ddmmyy (ex.: 010925).")
            continue
        if not data_ok:
            print("Data inválida. Use ddmmyy (ex.: 010925).")
            continue
        if not quantidade_ok:
            print("Quantidade inválida (use número inteiro).")
            continue

        quantidade = int(quantidade_texto)
        novo_registro = {"id": proximo_id, "nome": nome, "lote": lote, "validade": validade, "data": data, "qtd": quantidade}
        dados.append(novo_registro)
        fila.append(novo_registro)   # FIFO
        pilha.append(novo_registro)  # LIFO
        proximo_id += 1
        print("Registro efetuado.")

    elif opcao_menu == "2":
        if len(fila) == 0:
            print("Fila vazia.")
        else:
            removido_fifo = fila.pop(0)  # FIFO
            print("Atendido (FIFO):")
            mostrar_um(removido_fifo)

    elif opcao_menu == "3":
        if len(pilha) == 0:
            print("Pilha vazia.")
        else:
            removido_lifo = pilha.pop()  # LIFO
            print("Removido do topo (LIFO):")
            mostrar_um(removido_lifo)

    elif opcao_menu == "4":
        print("\n--- Fila (ordem cronológica) ---")
        if len(fila) == 0:
            print("Fila vazia.")
        else:
            mostrar(fila)

    elif opcao_menu == "5":
        print("\n--- Pilha (topo primeiro) ---")
        if len(pilha) == 0:
            print("Pilha vazia.")
        else:
            mostrar_pilha(pilha)

    elif opcao_menu == "6":
        print("\n--- Ordenado por QUANTIDADE (Merge) ---")
        lista_ordenada_qtd = merge_sort_por_qtd(dados)
        mostrar(lista_ordenada_qtd)

    elif opcao_menu == "7":
        print("\n--- Ordenado por VALIDADE (Quick, ddmmyy) ---")
        copia_validade = dados[:]               # não altera o original
        quick_sort_por_validade(copia_validade) # in-place na cópia
        mostrar(copia_validade)

    elif opcao_menu == "8":
        modo_busca = input("Buscar por (1) NOME ou (2) LOTE: ")
        termo_busca = input("Valor exato a procurar: ")
        if modo_busca == "1":
            indices = busca_sequencial_por_nome(dados, termo_busca)
        elif modo_busca == "2":
            indices = busca_sequencial_por_lote(dados, termo_busca)
        else:
            print("Opção inválida.")
            indices = []
        if len(indices) == 0:
            print("Nada encontrado.")
        else:
            print("Encontrados nos índices:")
            indice_listagem = 0
            while indice_listagem < len(indices):
                print(indices[indice_listagem])
                mostrar_um(dados[indices[indice_listagem]])
                indice_listagem += 1

    elif opcao_menu == "9":
        print("\nObs.: Busca binária exige lista ORDENADA pela MESMA chave (nome).")
        lista_por_nome = merge_sort_por_nome(dados)
        alvo_nome = input("Nome exato a localizar: ")
        posicao_encontrada = busca_binaria_por_nome(lista_por_nome, alvo_nome)
        if posicao_encontrada is None:
            print("Não encontrado.")
        else:
            print("Encontrado na posição:")
            print(posicao_encontrada)
            mostrar_um(lista_por_nome[posicao_encontrada])

    elif opcao_menu == "0":
        print("Encerrando. Obrigado!")
        break

    else:
        print("Opção inválida. Tente novamente.")
