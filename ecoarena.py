import os
import random
import string

def verificar_login():
    caminho_username = "username.txt"
    caminho_senhas = "senhas.txt"
    caminho_pontos = "pontos.txt"  

    while True:
       
        username = input("\n ❖  Digite seu nome de usuário: ")
        
        
        password = input("\n ❖  Digite sua senha: ")
        
        
        with open(caminho_username, "r") as file_username, open(caminho_senhas, "r") as file_senhas:
            usernames = file_username.read().splitlines()
            senhas = file_senhas.read().splitlines()
            
            if username in usernames:
                
                index = usernames.index(username)
                
                
                if senhas[index] == password:
                    print("\n ☑  Login realizado com sucesso! ☑")
                    
                   
                    interagir_usuario(username, caminho_pontos, index)
                    break
                else:
                    print("\n ☒  Usuário ou Senha incorretos. Tente novamente. ☒")
            else:
                print("\n ☒  Usuário ou Senha incorretos. Tente novamente. ☒")
        
        

def interagir_usuario(username, caminho_pontos, index):
    while True:
    
        opcao = input(f"\n▶ Olá, {username}! Deseja cadastrar alimentos, verificar pontos ou sair? (cadastrar/verificar/sair): \n").strip().lower()
        
        if opcao == "cadastrar":
            
            cadastrar_alimento(username, index, caminho_pontos)
        elif opcao == "verificar":
        
            verificar_pontos(username, caminho_pontos, index)

        elif opcao == 'sair':
            print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\n▏Obrigado por acessar ECOARENA!⌦ ▕\n▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔')
            exit()
        else:
            print("\n ☒  Opção inválida. Por favor, escolha 'cadastrar','verificar' ou 'sair'. ☒")

def obter_setor(username, caminho_pontos, index):

    setores_disponiveis = {
        "1": "Norte inferior",
        "2": "Norte superior",
        "3": "Leste inferior",
        "4": "Leste superior",
        "5": "Oeste inferior",
        "6": "Oeste superior",
        "7": "Sul inferior",
        "8": "Sul superior"
    }

    while True:
        setor_usuario = input("\n ▶ Em qual setor da arena você está?\n  1. Norte inferior\n  2. Norte superior\n  3. Leste inferior\n  4. Leste superior\n  5. Oeste inferior\n  6. Oeste superior\n  7. Sul inferior\n  8. Sul superior\n ▶ INFORME APENAS O NÚMERO: ")
        
        if setor_usuario in setores_disponiveis:
            if setor_usuario == "1":
                print(f"{setores_disponiveis[setor_usuario]}: ☒  Não há lixeiras seletivas neste setor. Vá para o setor Oeste inferior, onde há lixeiras seletivas. ☒")
            elif setor_usuario == "2":
                print(f"{setores_disponiveis[setor_usuario]}: ☑  Há lixeiras seletivas neste setor. Faça o descarte de forma correta. ☑")
            elif setor_usuario == "3":
                print(f"{setores_disponiveis[setor_usuario]}: ☒  Não há lixeiras seletivas neste setor. Vá para o setor Sul inferior, onde há lixeiras seletivas. ☒")
            elif setor_usuario == "4":
                print(f"{setores_disponiveis[setor_usuario]}: ☑  Há lixeiras seletivas neste setor. Faça o descarte de forma correta. ☑")
            elif setor_usuario == "5":
                print(f"{setores_disponiveis[setor_usuario]}: ☑  Há lixeiras seletivas neste setor. Faça o descarte de forma correta. ☑")
            elif setor_usuario == "6":
                print(f"{setores_disponiveis[setor_usuario]}: ☒  Não há lixeiras seletivas neste setor. Vá para o setor Norte superior, onde há lixeiras seletivas. ☒")
            elif setor_usuario == "7":
                print(f"{setores_disponiveis[setor_usuario]}: ☑  Há lixeiras seletivas neste setor. Faça o descarte de forma correta. ☑")
            elif setor_usuario == "8":
                print(f"{setores_disponiveis[setor_usuario]}: ☒  Não há lixeiras seletivas neste setor. Vá para o setor Leste superior, onde há lixeiras seletivas. ☒")
            

            while True:
                decisao_patamar = input("\n▶ Deseja verificar seu patamar e prêmios? (sim/nao): ").strip().lower()
                if decisao_patamar == 'sim':
                    patamar(username, caminho_pontos, index)
                elif decisao_patamar == 'nao':
                    print('\n▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\n▏Obrigado por ajudar o meio ambiente, torcedor!⌦ ▕\n▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔')
                    exit()
                else:
                    print('\n ☒  Responda apenas com "sim" ou "não". ☒')

        else:
            print("\n ☒  Resposta inválida. Por favor, escolha um setor válido. ☒")

            

def cadastrar_alimento(username, index, caminho_pontos):
    # Dicionário de pontos por código de alimento
    pontos_por_codigo = {
        "PL01": 15,
        "PL02": 10,
        "PL03": 30,
        "PL04": 15,
        "PL05": 30,
        "PL06": 40,
        "PL07": 30,
        "PA01": 15,
        "PA02": 20,
        "PA03": 35,
        "ME01": 25,
    }
    
    codigo_alimento = input("\n ▶ Digite o código do alimento: \n")
    
    if codigo_alimento in pontos_por_codigo:
        pontos_adicionados = pontos_por_codigo[codigo_alimento]
        print(f"\n ☑  Alimento com código {codigo_alimento} cadastrado com sucesso. Você ganhou {pontos_adicionados} pontos. ☑")

        # Leitura dos pontos atuais
        with open(caminho_pontos, "r") as file_pontos:
            pontos = file_pontos.read().splitlines()
        
        # Garantir que o índice exista na lista de pontos
        if index >= len(pontos):
            while len(pontos) <= index:
                pontos.append("0")
        
        # Atualização dos pontos do usuário
        pontos_usuario_atual = int(pontos[index])
        pontos_usuario_atual += pontos_adicionados
        pontos[index] = str(pontos_usuario_atual)
        
        # Gravação dos pontos atualizados
        with open(caminho_pontos, "w") as file_pontos:
            for ponto in pontos:
                file_pontos.write(f"{ponto}\n")

    else:
        print("\n ☒  Código do alimento inválido. Tente novamente. ☒")
    
    while True:

        opcao = input("\n▶ Deseja cadastrar outro alimento, verificar seus pontos ou verificar seu setor? (cadastrar/verificar/setor): ").strip().lower()
        
        if opcao == "cadastrar":
            cadastrar_alimento(username, index, caminho_pontos)
        elif opcao == "verificar":
            verificar_pontos(username, caminho_pontos, index)
        elif opcao == "setor":
            obter_setor(username, caminho_pontos, index)
        else:
            print("\n ☒  Responda com Cadastrar,verificar ou setor. ☒\n")


    
def verificar_pontos(username, caminho_pontos, index):
    if not os.path.exists(caminho_pontos):
        print(f"\n ➤ {username}, você tem 0 pontos.\n")
    else:
        with open(caminho_pontos, "r") as file_pontos:
            pontos = file_pontos.read().splitlines()
            
            if index < len(pontos):
                pontos_usuario = pontos[index]
                print(f"\n ➤ {username}, você tem {pontos_usuario} pontos.\n")
            else:
                print(f"\n ➤ {username}, você tem 0 pontos.\n")
                
    
    while True:
    
        decisao = input("\n▶ Deseja voltar para o cadastro de alimentos, verificar o patamar ou sair? (cadastrar/patamar/sair): \n").strip().lower()
        
        if decisao == "cadastrar":
            cadastrar_alimento(username, index, caminho_pontos)
            break  
        elif decisao == 'patamar':
            patamar(username, caminho_pontos, index)
            break
        elif decisao == 'sair':
            print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\n▏Obrigado por acessar ECOARENA!⌦ ▕\n▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔')
            exit()
        else:
            print("\n ☒  Resposta inválida. Por favor, responda com 'patamar', 'cadastrar' ou 'sair'. ☒")

def patamar(username, caminho_pontos, index):
    premios_NT = ['⤴ 1: 1 CERVEJA', '⤴ 2: 1 REFRIGERANTE', '⤴ 3: 1 SALGADINHO']
    premios_AF = ['⤴ 4: 2 CERVEJAS', '⤴ 5: 1 PIZZA', '⤴ 6: 1 HAMBURGUER', '⤴ 7: 1 CHURROS', '⤴ 8: 1 CACHORRO QUENTE']
    premios_LL = ['⤴ 9: 3 CERVEJAS', '⤴ 10: 1 PIZZA + REFRIGERANTE', '⤴ 11: 1 HAMBURGUER + REFRIGERANTE', '⤴ 12: 1 CHURROS + REFRIGERANTE', '13: 1 CACHORRO QUENTE + REFRIGERANTE']

    if not os.path.exists(caminho_pontos):
        print(f"\n ☒  {username}, você não possui pontos cadastrados. ☒")
    else:
        with open(caminho_pontos, "r") as file_pontos:
            pontos = file_pontos.read().splitlines()
            
            if index < len(pontos):
                pontos_usuario = int(pontos[index])
                
                # Verifica o patamar do usuário com base nos pontos
                if 200 <= pontos_usuario < 500:
                    patamar_usuario = "Novato da Torcida"
                elif 500 <= pontos_usuario < 800:
                    patamar_usuario = "Amante do Futebol"
                elif 800 <= pontos_usuario < 1000:
                    patamar_usuario = "Lenda Local"
                elif 1000 <= pontos_usuario:
                    patamar_usuario = "Ídolo Nacional"
                elif pontos_usuario < 200:
                    print('\n ☒  Você não possui pontos suficientes para ter um patamar ☒')
                    saida_patamar = input('\n▶ Deseja sair, cadastrar alimentos ou verificar seus pontos? (sair/cadastrar/verificar)')
                    if saida_patamar == 'sair':
                        print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\n▏Obrigado por acessar ECOARENA!⌦ ▕\n▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔')
                        exit()
                    elif saida_patamar == 'cadastrar':
                        cadastrar_alimento(username, index, caminho_pontos)
                    elif saida_patamar == 'verificar':
                        verificar_pontos(username, caminho_pontos, index)
                    else:
                        print("\n ☒  Resposta inválida. Por favor, responda com 'verificar' ou 'cadastrar' ou 'sair'. ☒")
    
                print(f"\n ➤{username}, você está no patamar {patamar_usuario}. Você tem {pontos_usuario} pontos.")

                if pontos_usuario >= 200:
                    print('\n ▂▂▂ PRÊMIOS DO PATAMAR NOVATO DA TORCIDA ▔▔▔ \n')
                    for premio in premios_NT:
                        print(f"{premio} -200 PTS")
                    
                if pontos_usuario >= 500:
                    print('\n ▂▂▂ PRÊMIOS DO PATAMAR AMANTE DO FUTEBOL ▔▔▔ \n')
                    for premio in premios_AF:
                        print(f"{premio} -500 PTS")
                
                if pontos_usuario >= 800:
                    print('\n ▂▂▂ PRÊMIOS DO PATAMAR LENDA LOCAL ▔▔▔ \n')
                    for premio in premios_LL:
                        print(f"{premio} -800 PTS")
                
                if pontos_usuario >= 1000:
                    print('\n ▂▂▂ PRÊMIOS DO PATAMAR ÍDOLO NACIONAL ▔▔▔ \n')
                    print('⤴ 14: 2 INGRESSOS PARA QUALQUER JOGO A SUA ESCOLHA -1000 PTS')

                resgate_de_premios(index, caminho_pontos, pontos_usuario, premios_NT, premios_AF, premios_LL)
            else:
                print(f"\n ➤{username}, você não possui pontos cadastrados.")


def resgate_de_premios(index, caminho_pontos, pontos_usuario, premios_NT, premios_AF, premios_LL):
    premio_to_cost = {
        **{str(i + 1): 200 for i in range(len(premios_NT))},  
        **{str(i + 4): 500 for i in range(len(premios_AF))},  
        **{str(i + 9): 800 for i in range(len(premios_LL))},  
        '14': 1000  
    }

    while True:
        escolha_de_premios = input("\n▶ Qual prêmio você deseja resgatar? (informe um número de 1 a 14): ")

        if escolha_de_premios in premio_to_cost:
            custo_pontos = premio_to_cost[escolha_de_premios]
            
            if pontos_usuario >= custo_pontos:
                pontos_usuario -= custo_pontos
                print(f"\n ☑ Prêmio {escolha_de_premios} resgatado com sucesso! Você gastou {custo_pontos} pontos. ☑")
                print(f"\n ➤ Seus pontos restantes: {pontos_usuario} pontos.")
                
                with open(caminho_pontos, "r") as file_pontos:
                    pontos = file_pontos.read().splitlines()
                
                pontos[index] = str(pontos_usuario)
                
                with open(caminho_pontos, "w") as file_pontos:
                    for ponto in pontos:
                        file_pontos.write(f"{ponto}\n")
                
                cupom = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
                
                with open("cupom.txt", "a") as file_cupom:
                    file_cupom.write(f"{cupom}\n")
                
                print(f" ――――Seu cupom é: {cupom}―――― ")
                
                break
            else:
                print(f"\n ☒  Você não possui pontos suficientes para resgatar este prêmio. Tente novamente. ☒")
        else:
            print("\n ☒  Escolha inválida. Informe um número que você possa resgatar ☒")

    return pontos_usuario
            
def criar_cadastro():
    caminho_username = "username.txt"
    caminho_senhas = "senhas.txt"
    caminho_pontos = "pontos.txt"

    if not os.path.exists(caminho_username):
        with open(caminho_username, "w") as file:
            pass  
    if not os.path.exists(caminho_senhas):
        with open(caminho_senhas, "w") as file:
            pass  
    if not os.path.exists(caminho_pontos):
        with open(caminho_pontos, "w") as file:
            pass  

    while True:

        username = input("\n▶ Digite um nome de usuário (até 8 caracteres): ")

        if len(username) > 8:
            print("\n ☒  Nome de usuário não possui 8 caracteres. Tente novamente. ☒")
            continue
        

        with open(caminho_username, "r") as file_username:
            usernames = file_username.read().splitlines()
            if username in usernames:
                print("\n ☒  O nome de usuário já existe. Tente novamente. ☒")
                continue
        
        password = input("\n▶ Digite uma senha com 4 números: ")

        if len(password) != 4 or not password.isdigit():
            print("\n ☒  Senha inválida. Deve conter exatamente 4 números. Tente novamente. ☒")
            continue
        
        # Verificar se a senha já existe no arquivo
        with open(caminho_senhas, "r") as file_senhas:
            senhas = file_senhas.read().splitlines()
            if password in senhas:
                print("\n ☒  A senha já existe. Tente novamente. ☒")
                continue

        print("\n ☑ Cadastro criado com sucesso! ☑")

        with open(caminho_username, "a") as file_username:
            file_username.write(f"{username}\n")
        with open(caminho_senhas, "a") as file_senhas:
            file_senhas.write(f"{password}\n")
        with open(caminho_pontos, "a") as file_pontos:
            file_pontos.write("0\n")
            
        verificar_login()
        break

def main():
    print('\n          ****************\n          *** 𝑬𝑪𝑶𝑨𝑹𝑬𝑵𝑨 ***\n          ****************\n')

    while True:
        ja_tem_cadastro = input("▶  Você já tem cadastro? (sim ou não): ").strip().lower()
        
        if ja_tem_cadastro == "sim":

            verificar_login()
        elif ja_tem_cadastro == "não" or ja_tem_cadastro == "nao":

            criar_cadastro()
        else:

            print("\n⌦  Resposta inválida. Por favor, responda com 'sim' ou 'não'. ⌫ \n")


main()
