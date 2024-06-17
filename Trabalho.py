# aluno: Apollo

"""
Crie uma aplicação Python que tera uma lista de alunos, com as notas de b1 e b2, um menu para selecionar a opção

1 - adicionar aluno
2 - listar aluno
3 - remover aluno
4 - procurar aluno
5 - aprovados
6 - reprovados
7 - Procurar pelo nome do aluno
8 - Média da turma B1
9 - Média da turma B2
10 - Média da turma GERAL
11 - Diário da turma
0 - sair


Para o item 11 deve:Deve imprimir na tela neste padrão exatamente, com os alinhamentos igual ao exemplo abaixo:
Total linha: 56 colunas.
RA: 5 CARACTERES
Nome: 27 CARACTERES
B1, B2, Média: 5 CARACTERES CADA
DICA: var.ljust(QTD, CHAR) | var.rjust(QTD, CHAR)


--------------------------------------------------------
                   Diario da turma
--------------------------------------------------------
RA    Nome                      Nota B1  Nota B2   Média
--------------------------------------------------------
00001 Aluno fulano de tal         10.00    10.00   10.00
00001 Aluno fulano de tal         10.00    10.00   10.00
00001 Aluno fulano de tal         10.00    10.00   10.00
00001 Aluno fulano de tal         10.00    10.00   10.00
--------------------------------------------------------
                  Médias da Turma 10.00    10.00   10.00
--------------------------------------------------------

Deve ser entregue o link do repositório do github.
"""

alunos = {}

def menu():
    print("1 - Adicionar aluno")
    print("2 - listar aluno")
    print("3 - Remover aluno")
    print("4 - procurar aluno")
    print("5 - Aprovados")
    print("6 - Reprovados")
    print("7 - procurar pelo nome do aluno")
    print("8 - Média da turma B1")
    print("9 - Média da turma B2")
    print("10 -Média da turma GERAL" )
    print("11 - Diário")
    print(" 0 - sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except Exception as e:
        print(f"Opção invalida: {e}")
def add_aluno():
    try:
        ra = input("digite a ra do aluno: ")
        nome =  input("digite o nome do aluno: ")
        nota_b1 = float(input("digite a nota b1 do aluno: "))
        nota_b2 = float(input("digite a nota b2 do aluno: "))
        dados = {"nome": nome, "b1": nota_b1, "b2": nota_b2}
        alunos[ra] = dados
    except Exception as e:
        print(f" alguma coisa foi digitada errado!:")
def listar_aluno():
    for ra, dados in alunos.items():
        print(f"RA: {ra} - aluno: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
    input("presione qualquer tecla para continuar!")
    
def remover_aluno():
    ra = input("Digite a Ra do aluno")
    if ra in alunos:
        aluno = alunos.pop(ra)
        print(f"O aluno: {aluno["nome"]} foi removido")
    else:
        print("aluno não encontrado!")
    input("presione qualquer tecla para continuar!")
    
def procurar_aluno():
    ra = input("Digite a Ra do aluno: ")
    if ra in alunos:
        dados = alunos[ra]
        print(f"RA: {ra} - nome: {dados["nome"]}")
    else:
        print("Aluno não encontrado!")
    input("presione qualquer tecla para continuar!")
    
def aprovados():
    for ra, dados in alunos.items():
        if ((dados["b1"] + dados["b2"]) / 2) >= 7.0:
            aluno = f"RA: {ra} - "
            aluno += f"Nome: {dados["nome"]} - "
            aluno += f"B1: {dados["b1"]} - "
            aluno += f"B2: {dados["b2"]} - "
            print(aluno)
    input("presione qualquer tecla para continuar!")

def reprovados():
    for ra, dados in alunos.items():
        if ((dados["b1"] + dados["b2"]) / 2) < 7.0:
            aluno = f"RA: {ra} - "
            aluno += f"Nome: {dados["nome"]} - "
            aluno += f"B1: {dados["b1"]} - "
            aluno += f"B2: {dados["b2"]} - "
            print(aluno)
    input("presione qualquer tecla para continuar!")
    
def procurar_nome():
    nome = input("Digite o nome do aluno: ")
    for ra, dados in alunos.items():
        if dados['nome'] == nome:
            print(f"RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2: {dados['b2']}")
    input("presione qualquer tecla para continuar!")

def media_b1():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados['b1']
        qtd += 1
    if qtd > 0:
        media = soma / qtd
        print(f"A média de B1 é: {media:.2f}")
    else:
        input("Pressione qualquer tecla para continuar")

def media_b2():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados['b2']
        qtd += 1
    if qtd > 0:
        media = soma / qtd
        print(f"A média de B2 é: {media:.2f}")
    else:
        input("Pressione qualquer tecla para continuar")
    
def media_geral():
    total = 0
    soma = 0
    for dados in alunos.items():
        total += (dados['b1'] + dados['b2'])
        soma += 1
    if soma > 0:
        media = total / (2 * soma)
        print(f"Média geral da turma: {media}")
    input("Pressione qualquer tecla para continuar")

def diario():
    cabecalho = '--------------------------------------------------------\n'
    titulo = '                   Diario da turma\n'
    colunas = 'RA    Nome                      Nota B1  Nota B2   Média\n'
    
    print(cabecalho + titulo + cabecalho + colunas + cabecalho)
    
    for aluno in alunos:
        ra = aluno["RA"].ljust(5)
        nome = aluno["Nome"].ljust(27)
        nota_b1 = str(aluno["Nota B1"]).rjust(5)
        nota_b2 = str(aluno["Nota B2"]).rjust(8)
        media = str(aluno["Média"]).rjust(7)
        print(f"{ra} {nome} {nota_b1} {nota_b2} {media}")
        
    print(cabecalho)
    input("Pressione qualquer tecla para continuar!")

def sair():
    print("Saindo do programa...")
    exit()

if __name__ == "__main__":
    while True:
        match menu():
            case 1:
                add_aluno()
            case 2:
                listar_aluno()
                break
            case 3:
                remover_aluno()
                break
            case 4:
                procurar_aluno()
                break
            case 5:
                aprovados()
                break
            case 6:
                reprovados()
                break
            case 7:
                procurar_nome()
            case 8:
                media_b1()
            case 9:
                media_b2()
            case 10:
                media_geral()
            case 11:
                diario()
            case 0:
                sair()