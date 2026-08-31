# -*- coding: utf-8 -*-
import os

def criar_painel():
    os.system("clear")
    
    # 1. EXIBE TODAS AS INFORMAÇÕES E REDES SOCIAIS ENQUANTO RODA O SCRIPT
    print "\033[31m  ______             _                    \033[0m"
    print "\033[33m |  ____|           | |                   \033[0m"
    print "\033[32m | |__ __ _ _ __ ___| |_ __ _ _ __ ___    \033[0m"
    print "\033[36m |  __/ _` | '__/ __| __/ _` | '_ ` _ \\   \033[0m"
    print "\033[34m | | | (_| | |  \\__ \\ || (_| | | | | | |  \033[0m"
    print "\033[35m |_|  \\__,_|_|  |___/\\__\\__,_|_| |_| |_|  \033[0m"
    print "\033[1;36m       M O D I F I C A D O R              \033[0m"
    print "--------------------------------------------------"
    print "\033[1;33mCriador: gagadev and fantasma team\033[0m"
    print "--------------------------------------------------"
    print " [i] Discord dos desenvolvedores: https://discord.gg/szcg2ZaA5"
    print " [i] Canal do YT (oficial): https://www.youtube.com/@gagadv2"
    print " [i] TikTok dos desenvolvedores: tiktok.com/@fantasmahub"
    print " [i] Roblox do desenvolvedor: https://www.roblox.com/share?code=65e7b03d3bb7974086b1af442cd5c6ab&type=Profile&source=ProfileShare&stamp=1788154189471"
    print "--------------------------------------------------"
    print " [!] Se tiver algum problema no painel, abre o ticket"
    print "     no Discord do desenvolvedor!"
    print "--------------------------------------------------"
    print ""
    
    # Pergunta os dados ao usuário
    usuario_custom = raw_input("Digite o nome de usuario desejado (ex: fantasma): ")
    host_custom = raw_input("Digite o nome da maquina/host desejado (ex: localhost): ")
    
    # Pergunta sobre o robô/arte adicional
    quer_robo = raw_input("Quer colocar um robo/arte (sim ou nao)? ").strip().lower()
    tipo_robo = ""
    if quer_robo in ["sim", "s", "y", "yes"]:
        print "\nTipos disponiveis: [android] / [kali] / [fantasma]"
        tipo_robo = raw_input("Qual tipo de robo voce quer? ").strip().lower()

    home_dir = os.environ.get("HOME", "/data/data/com.termux/files/home")
    bashrc_path = os.path.join(home_dir, ".bashrc")
    motd_path = os.path.join(home_dir, "../usr/etc/motd")

    # Define o desenho do robô/arte com base na escolha
    arte_robo = ""
    if tipo_robo == "android":
        arte_robo = """\033[32m       \\x\\x\\x/x/x/       \n       [o]   [o]       \n      /   \\_/   \\      \n     |           |     \n     |___|   |___|     \n     \\_|_|   |_|_/     \033[0m\n"""
    elif tipo_robo == "kali":
        arte_robo = """\033[37m         /\\                               \n        /  \\  /\\                          \n       / /\\ \\/  \\                         \n      / /  \\/\\   \\                        \n     /_/      \\___\\                       \033[0m\n"""
    elif tipo_robo == "fantasma":
        arte_robo = """\033[37m       .-.        \n      (o.o)       \n       |=|        \n      /   \\       \n     (_/ \\_)      \033[0m\n"""

    # 2. CONTEÚDO FIXO PARA O TOPO DO TERMUX (MOTD) COM O BANNER E O ROBÔ ESCOLHIDO
    motd_conteudo = """\033[31m  ______             _                    \033[0m
\033[33m |  ____|           | |                   \033[0m
\033[32m | |__ __ _ _ __ ___| |_ __ _ _ __ ___    \033[0m
\033[36m |  __/ _` | '__/ __| __/ _` | '_ ` _ \\   \033[0m
\033[34m | | | (_| | |  \\__ \\ || (_| | | | | | |  \033[0m
\033[35m |_|  \\__,_|_|  |___/\\__\\__,_|_| |_| |_|  \033[0m
\033[1;36m       M O D I F I C A D O R              \033[0m
--------------------------------------------------
\033[1;33mCriador: gagadev and fantasma team\033[0m
--------------------------------------------------
""" + arte_robo

    # 3. PROMPT TOTALMENTE RGB (COLORIDO EM TODAS AS PARTES E NO TEXTO QUE VOCÊ DIGITA)
    # Usa códigos ANSI para colorir o usuário, o host, o diretório e o caractere de comando ($)
    ps1_config = 'export PS1="\\[\\e[1;31m\\](%s\\[\\e[1;33m\\]@%s)\\[\\e[1;32m\\]-\\[\\e[1;36m\\][\\w]\\[\\e[0m\\]\\n\\[\\e[1;35m\\$\\e[0m \\e[1;37m"' % (usuario_custom, host_custom)

    try:
        with open(motd_path, "w") as f:
            f.write(motd_conteudo)

        with open(bashrc_path, "w") as f:
            f.write(ps1_config + "\n")

        print ""
        print "\033[1;32m[+] Sucesso! Painel com robo e RGB total configurado com sucesso!\033[0m"
        print "Abra uma nova aba no Termux para conferir o resultado!"
    except Exception as e:
        print "Erro ao salvar configuracao:", e

if __name__ == "__main__":
    criar_painel()
    
