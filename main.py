poder = ""
cabelo_cor = ""
roupa_p = ""
nome_p  = ""
hp_p = 0
atk_p = 0
mana = 0
opcao_classe = ""
# Tela de Login
print("teste")

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
    opcao_func = int(input("[1] - Iniciar/Continuar Jogo\n[2] - Configurações\n[100] - Sair",))