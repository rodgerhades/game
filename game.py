print("cidade abandonada")
print("1.ir para a cabana")
print("2.ir para a floresta")
print("3.sair do jogo")

escolha = int(input("qual sua escolha? "))
if escolha == 1:       
    print("você entrou na cabana")
    espada = int(input("1.pegar a espada 2.sair"))
    if espada == 1:
        print("você pegou a espada!")
        sair = int(input("1.sair?"))
        while not(sair == 1):
            sair = int(input("1.sair?"))
        print("você saiu")    
        
                       
    else:
        print("você saiu")
        print("cidade abandonada")
    
print("1.ir para a cabana")
print("2.ir para a floresta")
print("3.sair do jogo")
    
