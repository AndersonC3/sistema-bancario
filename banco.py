print("Bem vindo ao Banco Mercosul")
print(input("Informe o nome do Titular:"))

menu = """

[d]Deposito
[s]Sacar
[e]Extrato
[q]Sair

=> """

saldo = 800
extrato = ""
limite = 650
LIMITE_SAQUES = 3
numero_saques = 0




while True:

    opcao = input(menu)
    
    if opcao =="d":
        valor = float(input("Informe o valor do depósito:"))
        print("Ai sim meu nobre, parou de gastar!")

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: U$ {valor:.2f}\n"

        else:
            print("Operação Falhou! Tente novamente")

    elif opcao =="s":
       valor = float(input("Informe o valor de Saque:"))
       print("Maninho é bom gastar, mas pense em enconomizar e investir um pouco tbm!")

       excedeu_saldo = valor > saldo

       excedeu_limite = valor > limite 

       excedeu_saque = numero_saques >= LIMITE_SAQUES

       if excedeu_saldo:
        print("Mano vc gastou demais!")
               
       elif excedeu_limite:
         print("Caramba mano, hora de repensar os gastos!")

       elif excedeu_saque:
         print("Chega de gastar dinheiro por hj meu nobre!")

       elif valor > 0:
        saldo -= valor
        extrato += f"Saque: U$ {valor:.2f}\n"

       else:
         print("Operação falhou.O valor informado é invalido!")

    elif opcao == "e":
        print("\n========Extrato========")
        print("Não foram realizdas movimentações na conta."if not extrato else extrato)
        print("========================")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços. Volte Sempre!")
        break

    else:
        print("Operação invalida! Por favor, tente mais tarde!")





        
        
else:
    print("Obrigado por utilizar nossos serviços, Volte Sempre!")    
