# Imports
import os

# Características do personagem
poder = ""
cabelo_cor = ""
roupa_p = ""
nome_p  = ""
hp_p = 0
atk_p = 0
mana = 0
opcao_classe = ""
# Tela de Login

# Características dos inimigos
nome_orc = "Orc Abissal"
hp_orc = 20
atk_orc = 5

nome_sli = "Slime"
hp_sli = 5
atk_sli = 10
##############################

opcao_func = 0 # Opção Funcionalidade

while(opcao_func != 100):
    while(nome_p == ""):
        print("|====================================|")
        print("|  Bem vindo(a) à Reino de Etéria!   |")
        print("|____________________________________|")
        nome_p = str(input("Nome do usuário: "))

        print("Personalize seu personagem: ")
        print("Qual será a cor do seu cabelo: ")
        cabelo_cor = str(input("Cor: "))
        roupa_p = str(input("Descreva a roupa do personagem: "))
    os.system("cls")
    opcao_func = int(input("[1] - Iniciar/Continuar Jogo\n[2] - Configurações\n[100] - Sair",))
    if(opcao_func == 1):
        os.system("cls")
        print("Começar história") # Fazer introdução da história
        print("Iniciando batalha: ")
        while hp_sli > 0:
            opcao_acao = 0
            print("o que você fará: [1] - Atacar ")
            while opcao_acao != 1:
                print("o que você fará: [1] - Atacar ")
            
    elif(opcao_func == 2):
        os.system("cls")
        print("Abrir configurações") # Mostrar info do player
        print("Informações do jogador")
        print("Nome do jogador: ", nome_p)
        print("HP: ", hp_p, " | ", "ATK: ", atk_p)
    elif(opcao_func == 100):
        os.system("cls")
        print("Fechando jogo") # Manter assim