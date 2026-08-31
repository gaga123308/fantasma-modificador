# -*- coding: utf-8 -*-

def criar_painel():
    print "===================================="
    print "       FANTASMA MODIFICADOR"
    print "===================================="
    
    mensagem = raw_input("O que você quer que apareça na sua tela permanente? \n> ")
    cor = raw_input("Qual será a cor da sua mensagem (ex: red, green, blue, yellow)? \n> ").lower()
    
    cores = {
        "vermelho": "31", "red": "31",
        "verde": "32", "green": "32",
        "amarelo": "33", "yellow": "33",
        "azul": "34", "blue": "34",
        "magenta": "35", "purple": "35",
        "ciano": "36", "cyan": "36",
        "branco": "37", "white": "37"
    }
    
    codigo_cor = cores.get(cor, "37")
    
    bloco_bash = """
# --- Inicio do Painel Fantasma ---
echo -e "\\033[1;%sm----------------------------------\\033[0m"
echo -e "\\033[1;%sm %s \\033[0m"
echo -e "\\033[1;%sm----------------------------------\\033[0m"
# --- Fim do Painel Fantasma ---
""" % (codigo_cor, codigo_cor, mensagem, codigo_cor)

    home_dir = os.environ.get("HOME", "/data/data/com.termux/files/home")
    bashrc_path = os.path.join(home_dir, ".bashrc")
    
    try:
        arquivo = open(bashrc_path, "a")
        arquivo.write(bloco_bash)
        arquivo.close()
        print "\n[Sucesso] Configuração aplicada com sucesso!"
        print "Feche e abra o Termux novamente para ver a mensagem."
    except Exception as e:
        print "\n[Erro] Não foi possível alterar o arquivo:", e

if __name__ == "__main__":
    criar_painel()
