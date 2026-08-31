# -*- coding: utf-8 -*-
import os

def criar_painel():
    # Limpa a tela para o banner ocupar o topo
    os.system("clear")
    
    # Banner grande que ocupa bastante espaço na tela
    print "\033[1;36m"
    print "  ______             _                    "
    print " |  ____|           | |                   "
    print " | |__ __ _ _ __ ___| |_ __ _ _ __ ___    "
    print " |  __/ _` | '__/ __| __/ _` | '_ ` _ \\   "
    print " | | | (_| | |  \\__ \\ || (_| | | | | | |  "
    print " |_|  \\__,_|_|  |___/\\__\\__,_|_| |_| |_|  "
    print "       M O D I F I C A D O R              "
    print "\033[0m"
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
    
    # Pergunta o nome personalizado para o prompt
    usuario_custom = raw_input("Digite o nome de usuario desejado (ex: fantasma): ")
    host_custom = raw_input("Digite o nome da maquina/host desejado (ex: localhost): ")
    cor_prompt = raw_input("Qual sera a cor do seu prompt (ex: red, green, blue, cyan)? ")

    # Mapeamento de cores
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

    # Caminho do arquivo de configuração do bash no Termux
    home_dir = os.environ.get("HOME", "/data/data/com.termux/files/home")
    bashrc_path = os.path.join(home_dir, ".bashrc")
    motd_path = os.path.join(home_dir, "../usr/etc/motd")

    # Remove a mensagem de boas-vindas padrão do Termux
    try:
        if os.path.exists(motd_path):
            with open(motd_path, "w") as f:
                f.write("")
    except Exception as e:
        print "Aviso ao limpar o motd:", e

    # Cria o novo layout do prompt personalizado no .bashrc
    ps1_config = 'export PS1="\\[\\e[1;%sm\\](%s@%s)-\\[\\e[0m\\]\\[\\e[1;34m\\][\\w]\\[\\e[0m\\]\\n\\$ "' % (codigo_cor, usuario_custom, host_custom)

    try:
        with open(bashrc_path, "w") as f:
            f.write(ps1_config + "\n")
        print ""
        print "\033[1;32m[+] Sucesso! Painel configurado com as redes e prompt atualizado.\033[0m"
        print "Abra uma nova aba no Termux para conferir o resultado!"
    except Exception as e:
        print "Erro ao salvar configuracao:", e

if __name__ == "__main__":
    criar_painel()
    
