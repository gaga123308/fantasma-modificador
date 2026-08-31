# -*- coding: utf-8 -*-
import os

def criar_painel():
    os.system("clear")
    
    print "\033[1;36m=== CONFIGURACAO DO FANTASMA MODIFICADOR ===\033[0m\n"
    usuario_custom = raw_input("Digite o nome de usuario desejado (ex: fantasma): ")
    host_custom = raw_input("Digite o nome da maquina/host desejado (ex: localhost): ")
    
    print "\nEscolha a cor do seu prompt:"
    print "1 - Cores fixas (vermelho, verde, amarelo, azul, ciano, branco)"
    print "2 - RGB / Colorido"
    tipo_cor = raw_input("Digite 1 ou 2: ")

    codigo_cor = "32"
    usar_rgb_prompt = False

    if tipo_cor == "2":
        usar_rgb_prompt = True
    else:
        cor_prompt = raw_input("Qual sera a cor fixa (ex: red, green, blue, cyan)? ")
        cores = {
            "vermelho": "31", "red": "31",
            "verde": "32", "green": "32",
            "amarelo": "33", "yellow": "33",
            "azul": "34", "blue": "34",
            "magenta": "35", "purple": "35",
            "ciano": "36", "cyan": "36",
            "branco": "37", "white": "37"
        }
        codigo_cor = cores.get(cor_prompt, "32")

    home_dir = os.environ.get("HOME", "/data/data/com.termux/files/home")
    bashrc_path = os.path.join(home_dir, ".bashrc")
    motd_path = os.path.join(home_dir, "../usr/etc/motd")

    # Mensagem colorida que fica estampada no topo sempre que abrir o Termux
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
 [i] Discord dos desenvolvedores: https://discord.gg/szcg2ZaA5
 [i] Canal do YT (oficial): https://www.youtube.com/@gagadv2
 [i] TikTok dos desenvolvedores: tiktok.com/@fantasmahub
 [i] Roblox do desenvolvedor: https://www.roblox.com/share?code=65e7b03d3bb7974086b1af442cd5c6ab&type=Profile&source=ProfileShare&stamp=1788154189471
--------------------------------------------------
 [!] Se tiver algum problema no painel, abre o ticket
     no Discord do desenvolvedor!
--------------------------------------------------
"""

    if usar_rgb_prompt:
        ps1_config = 'export PS1="\\[\\e[31m\\](%s@%s)-\\[\\e[32m\\][\\w]\\[\\e[0m\\]\\n\\$ "' % (usuario_custom, host_custom)
    else:
        ps1_config = 'export PS1="\\[\\e[1;%sm\\](%s@%s)-\\[\\e[0m\\]\\[\\e[1;34m\\][\\w]\\[\\e[0m\\]\\n\\$ "' % (codigo_cor, usuario_custom, host_custom)

    try:
        with open(motd_path, "w") as f:
            f.write(motd_conteudo)

        with open(bashrc_path, "w") as f:
            f.write(ps1_config + "\n")

        print ""
        print "\033[1;32m[+] Sucesso! Banner arco-íris configurado para aparecer sempre!\033[0m"
        print "Abra uma nova aba no Termux para conferir!"
    except Exception as e:
        print "Erro ao salvar configuracao:", e

if __name__ == "__main__":
    criar_painel()
    
