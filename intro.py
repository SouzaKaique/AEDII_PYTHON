import os

class Informacoes:
    def __init__(self, nome, endereco, cidade, uf, status='ativo'):
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf
        self.status = status

class NoArvore:
    def __init__(self, codigo, informacoes):
        self.codigo = codigo
        self.informacoes = informacoes
        self.esquerda = None
        self.direita = None

def inserir(raiz, codigo, informacoes):
    if raiz is None:
        return NoArvore(codigo, informacoes)
    if codigo < raiz.codigo:
        raiz.esquerda = inserir(raiz.esquerda, codigo, informacoes)
    elif codigo > raiz.codigo:
        raiz.direita = inserir(raiz.direita, codigo, informacoes)
    else:
        print("Código já existe!")
    return raiz

def buscar(raiz, codigo):
    if raiz is None or raiz.codigo == codigo:
        return raiz
    if codigo < raiz.codigo:
        return buscar(raiz.esquerda, codigo)
    else:
        return buscar(raiz.direita, codigo)

def excluir_logicamente(raiz, codigo):
    no = buscar(raiz, codigo)
    if no:
        no.informacoes.status = 'excluído'
        print(f"\nRegistro com código {codigo} excluído.")
    else:
        print("\nCódigo não encontrado.")

def ler_informacoes():
    nome = input('Digite um nome: ')
    endereco = input('Digite um endereço: ')
    cidade = input('Digite uma cidade: ')
    uf = input('Digite uma UF: ')
    return Informacoes(nome, endereco, cidade, uf)

def imprimir_registros(raiz):
        if raiz:
            if raiz.informacoes.status != 'excluído':
                print(f"Código: {raiz.codigo}")
                print(f"Nome: {raiz.informacoes.nome}")
                print(f"Endereço: {raiz.informacoes.endereco}")
                print(f"Cidade: {raiz.informacoes.cidade}")
                print(f"UF: {raiz.informacoes.uf}")
            imprimir_registros(raiz.esquerda)
            imprimir_registros(raiz.direita)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar_tela()
    raiz = None

    while True:
        codigo = int(input('\nDigite o código: '))
        info = ler_informacoes()
        raiz = inserir(raiz, codigo, info)

        continuar = input("\nDeseja cadastrar mais informações? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\nBusca por código")
    codigo_busca = int(input("Digite o código para busca: "))
    resultado = buscar(raiz, codigo_busca)
    if resultado and resultado.informacoes.status != 'excluído':
        print("\nRegistro encontrado:")
        print(f"Código: {resultado.codigo}")
        print(f"Nome: {resultado.informacoes.nome}")
        print(f"Endereço: {resultado.informacoes.endereco}")
        print(f"Cidade: {resultado.informacoes.cidade}")
        print(f"UF: {resultado.informacoes.uf}")
    elif resultado and resultado.informacoes.status == 'excluído':
        print("\nRegistro encontrado, mas está marcado como excluído.")
    else:
        print("\nCódigo não encontrado.")

    print("\nExclusão de registro")
    codigo_exclusao = int(input("Digite o código para exclusão: "))
    excluir_logicamente(raiz, codigo_exclusao)

    print("\nOs registros restantes são:")

    imprimir_registros(raiz)

if __name__ == "__main__":
    main()
