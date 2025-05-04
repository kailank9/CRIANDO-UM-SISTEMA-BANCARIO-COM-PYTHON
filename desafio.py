import textwrap
import webbrowser

def menu():
    menu = """ BEM VINDO AO _____CALANGOBANK_____


 ########MENU##########

[s]- SACAR
[d]- DEPOSITAR
[e]- EXTRATO
[nc]-NOVA CONTA
[lc]-LISTAR CONTA
[nu]-NOVO USUARIO
[q]- SAIR
[eu]- CONECTE-SE COMIGO


=> """
    return input(menu)


def sacar(*,saldo, limite,  numero_de_saques,valor,extrato, LIMITE_DE_SAQUE):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUE

    if excedeu_saldo:
            print("Operação falhou! você nao tem saldo suficiente")
    elif excedeu_limite:
            print("Operação falhou! limite de saque R$ 500")
    elif excedeu_saques:
            print("Operação falhou! você excedeu o limite de saques! ")
    elif valor > 0:
            saldo -= valor
            extrato += f"SAQUE: R$ {valor:.2f}\n"
    else:
            print("Operação falhou! o valor informado e invalido.")
    return saldo, extrato, numero_de_saques

def deposito(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"DEPOSITO: R$ {valor:.2f}\n"
        
    else:
        print("Operação falhou! o valor informado e invalido.")

    return saldo, extrato
    
def exibir_extrato(saldo, /,*,extrato):
    print("\n===============EXIBINDO EXTRATO==================")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"\nSALDO: R$ {saldo:.2f}\n")
    print("=================================================")


def criar_usuario(usuarios):
     cpf = input("Informe os 11 digitos do seu CPF:")
     usuario = filtrar_usuario(cpf, usuarios)
     if usuario:
          print("ja existe usuario com esse CPF!")
          return
     nome = input("Informe o nome completo :")
     data_nascimento = input("Informe a data de NASCIMENTO (dd-mm-aa):")
     endereco = input("Informe seu ENDEREÇO (logradouro, nro - bairro - cidade/sigla estado):")
     usuarios.append({"nome" : nome, "data_nascimento" : data_nascimento, "cpf" : cpf, "endereco": endereco  })
     print("==========Usuario criado com Sucesso==========")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in  usuarios if usuario["cpf"]== cpf ] 
     return usuarios_filtrados [0] if usuarios_filtrados else None


def criar_conta(agencia,numero_conta, usuarios):
     cpf = input("Informe o CPF do usuario:")
     usuario = filtrar_usuario(cpf, usuarios)
     if usuario:
        print("\n ===conta criada com sucesso!===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     print("usuario nao encontrado! criação de conta encerrado")

def listar_contas(contas):
     for conta in contas:
          linha =  f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
          print("*" *100)
          print(textwrap.dedent(linha))

def open_link(url):
    webbrowser.open(url)

     



     

      
    



def main():

    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    LIMITE_DE_SAQUE = 3
    usuarios = []
    contas = []
     
     

    while True:
        opcao = menu()

        if opcao == "s":
            valor  = float(input("INFORME O VALOR DO SAQUE:"))
            saldo, extrato, numero_de_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_de_saques=numero_de_saques,
            LIMITE_DE_SAQUE=LIMITE_DE_SAQUE,
            )



        elif opcao == "d":
            valor = float(input("INFORME O VALOR DE DEPOSITO:"))
            saldo, extrato = deposito(saldo,valor,extrato)
            print("\n=== Depósito realizado com sucesso! ===")
            

    
        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "eu":
            open_link("https://github.com/kailank9")
              

        elif opcao == "q":
            break

        else:
            print("ERRO NA OPERACAO...")
        

main()
    


