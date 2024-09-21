import os

class Produto:
    codigo: int
    nome: str
    descricao: str
    preco_compra: float
    preco_venda: float

red = "\033[0;31;m"

def ProdutoComoTexto(c: Produto) -> str:
    return (f"{c.codigo};{c.nome};{c.descricao};{c.preco_compra};{c.preco_venda}\n")


def TextoComoProduto(s: str) -> Produto:
    codigo, nome, descricao, preco_compra, preco_venda = s.split(";")
    c = Produto()
    c.codigo = int(codigo)
    c.nome = (nome)
    c.descricao = (descricao)
    c.preco_compra = float(preco_compra)
    c.preco_venda = float(preco_venda)
    return c


def CadastrarProduto() -> Produto:
    os.system("cls")
    try:
        c = Produto()
        print("Cadastrando produto...")
        c.codigo = int(input("Defina o código do produto: "))
        c.nome = str(input("Defina o nome do produto: "))
        c.descricao = str(input("Defina a descrição do produto: "))
        c.preco_compra = float(input("Defina o preço de compra do produto: "))
        c.preco_venda = float(input("Defina o valor de venda do produto: "))
        produtos.append(c)
        SalvarProduto(c)
        input("Produto cadastrado com sucesso. Tecle Enter para prosseguir: ")
        Menu()
    except ValueError:
        while True:
            print("Dados inválidos.")
            print("1 - Tentar novamente")
            print("2 - Menu principal")
            option = input()
            if option == "1":
                CadastrarProduto()
            elif option == "2":
                Menu()
            else:
                print("Opção inválida. Tecle Enter para retornar ao Menu principal.")
            input()
            Menu()

def EncontrarProdutoPeloCodigo(codigo:int)->Produto:
    f = open("produtos.txt", "r", encoding="UTF8")
    linhas = f.readlines()
    f.close()
    for linha in linhas:
        p:Produto = TextoComoProduto(linha)
        if p.codigo == codigo: return p
        return None

def AlterarProduto():
    try:
        print("Digite o codigo do produto a ser alterado")
        codigo = int(input())
        p = EncontrarProdutoPeloCodigo(codigo)
        if p is None:
            print("Produto não encontrado")
            input()
            return
        else:
            print("Digite um novo nome para o produto:")
            novoNome = input()
            print("Digite uma nova descrição para o produto:")
            novaDescricao = input()
            print("Digite um novo preço de compra para o produto")
            novoPrecoCompra = float(input())
            print("Digite um novo preço de compra para o produto:")
            novoPrecoVenda = float(input())
            p.nome = novoNome
            p.descricao = novaDescricao
            p.preco_compra = novoPrecoCompra
            p.preco_venda = novoPrecoVenda
            SalvarAlteracaoProduto(p)
            print("Produto Atualizado com sucesso...")
            input()
            return
    except:
        print("ERRRO - Falha ao tentar atualizar produto...")
        print("1 - Tentar novamente")
        print("Enter - Menu Principal")
        option = input()
        if option == "1": AlterarProduto()
        else: Menu()

def SalvarAlteracaoProduto(novosDados:Produto):
    try:
        linhaNova = ProdutoComoTexto(novosDados)
        f = open("produtos.txt", "r", encoding="UTF8")
        linhas = f.readlines()
        f.close()
        for i in range(len(linhas)):
            if linhas[i].split(";")[0] == str(novosDados.codigo): linhas[i] = linhaNova
        f = open("produtos.txt", "w+", encoding="UTF8")
        f.writelines(linhas)
        f.close()
    except:
        print("Erro ao atualizar produto...")

def SalvarProduto(c: Produto):
    f = open("produtos.txt", "a+", encoding="UTF8")
    f.write(ProdutoComoTexto(c))
    f.close()

def imprimirProduto(c: Produto):
    print(f"Código: {c.codigo}")
    print(f"Nome: {c.nome}")
    print(f"Descrição: {c.descricao}")
    print(f"Preço de compra : R${c.preco_compra:.2f}")
    print(f"Preço de venda: R${c.preco_venda:.2f}")
    lucro = c.preco_venda - c.preco_compra
    if lucro > 0:
        print(f"Lucro estimado por venda: R${lucro:.2f}")
        print("-"*40)
    else:
        print(f"Prejuízo estimado por venda: R${lucro:.2f}")
        print("-"*40)

def ListarProduto():
    os.system("cls")
    f = open("produtos.txt", "r", encoding="UTF8")
    print("-"*40)
    print("        PRODUTOS CADASTRADOS: ")
    print("-"*40)
    try:
        for linha in f:
            produto = TextoComoProduto(linha)
            imprimirProduto(produto)
        input()
    except:
        while True:
            print("Nenhum produto cadastrado. Escolha uma opção.")
            print("1 - Cadastrar Produto")
            print("Enter - Menu principal")
            option = input()
            if option == "1":
                CadastrarProduto()
            else:
                Menu()

def RemoverProduto():
    os.system("cls")
    try:
        codigo = int(input("Digite o código do produto a ser removido: "))
        #produtos = []  # Lista para armazenar produtos que vão permanecer

        # Lendo produtos do arquivo
        with open("produtos.txt", "r", encoding="UTF8") as f:
            linhas = f.readlines()

        # Filtrando produtos, excluindo o que tem o código especificado
        for linha in linhas:
            produto = TextoComoProduto(linha)
            if produto.codigo != codigo:  # Mantém o produto se o código não for o especificado
                produtos.append(produto)

        # Verificando se algum produto foi removido
        if len(produtos) == len(linhas):
            print("Impossível excluir um produto não cadastrado.")
        else:
            # Reescrevendo o arquivo sem o produto removido
            with open("produtos.txt", "w", encoding="UTF8") as f:
                for p in produtos:
                    f.write(ProdutoComoTexto(p))

            print("Produto removido com sucesso.")
        input("Tecle Enter para prosseguir: ")
        Menu()

    except ValueError:
        print("Dados inválidos.")
        print("1 - Tentar novamente")
        print("Enter - Menu principal")
        option = input()
        if option == "1":
            RemoverProduto()
        else:
            Menu()


def Senha():
    while True:
        os.system("cls")
        print("Insira a senha para prosseguir: ")
        senha = input()
        if senha != "":
            print("\033[1;31m Senha incorreta. Tecle Enter para tentar novamente.\033[m")
            input()
        else: 
            Menu()
            break

produtos = []

def Menu():
    while True:
        os.system("cls")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Excluir produto")
        print("5 - Encerrar")
        option = input()
        if option == "1": CadastrarProduto()
        elif option == "2": ListarProduto()
        elif option == "3": AlterarProduto()
        elif option == "4": RemoverProduto()
        elif option == "5": break
        else: input("Opção inválida. Tecle Enter para prosseguir.")
        Menu()
Senha()