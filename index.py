from classes.Produto import Produto

def menu():
    print()
    print("1 - Listar Produtos")
    print("2 - Inserir Produtos")
    print("3 - Alterar Produtos")
    print("4 - Excluir Produtos")
    print("0 - Sair")
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção "))
    
    match opcao:
        
        #LISTAR TODOS OS PRODUTOS CADASTRADOS
        case 1:
            Produto.listarTodos()
         
        #CADASTRAR NOVO PRODUTO
        case 2:
            codigo = input("Digite o código: ")
            nome = input("Digite o nome: ")
            quantidade = input("Digite a quantidade: ")
            valor = input("Digite o valor: ")        

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
         
        #ALTERAR PRODUTO JÁ CADASTRADO
        case 3:
            Produto.listarTodos()
            seletor = int(input("Qual item deseja alterar? "))
            item = Produto.consultar(seletor)
            
            quantidade = int(input("Qual a nova quantidade? "))
            valor = int(input("Qual o novo valor? "))
            
            produto = Produto(item["codigo"], item["nome"], quantidade, valor)
            produto.alterar(seletor)            
        
        #EXCLUIR PRODUTO
        case 4:
            Produto.listarTodos()
            seletor = int(input("Qual item deseja excluir? "))
            Produto.excluir(seletor)

print()
print("Sistema finalizado.")
print()