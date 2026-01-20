import os
import sys
import time
from pathlib import Path

# --- GARANTE QUE O PYTHON ACHE O PROJETO ---
# Adiciona a pasta 'src' ao caminho do Python
caminho_src = Path(__file__).resolve().parent.parent
sys.path.append(str(caminho_src))

# --- IMPORTS CORRIGIDOS (Baseados no seu Print) ---
# Note a mudança: de 'dominio' para 'classes'
from caatingaid.classes.angiosperma import Angiosperma
from caatingaid.classes.gimnosperma import Gimnosperma
from caatingaid.classes.pteridofita import Pteridofita
from caatingaid.classes.briofita import Briofita

# Note a mudança: de 'infraestrutura' para 'crud'
from caatingaid.crud.crud import CrudPlantas

# Mantemos services, pois no print a pasta se chama services
from caatingaid.services.gemini_api import BotanicoAI

# --- CORES E VISUAL ---
class Cores:
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    VERMELHO = '\033[91m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    limpar_tela()
    print(f"{Cores.VERDE}{Cores.NEGRITO}")
    print(r"""
   ______            __  _                   ________ 
  / ____/___ _____ _/ /_(_)___  ____ _____ _/  _/ __ \
 / /   / __ `/ __ `/ __/ / __ \/ __ `/ __ `// // / / /
/ /___/ /_/ / /_/ / /_/ / / / / /_/ / /_/ // // /_/ / 
\____/\__,_/\__,_/\__/_/_/ /_/\__, /\__,_/___/_____/  
                             /____/                   
    """)
    print(f"   🌵 SISTEMA CAATINGAID - ESTRUTURA CORRIGIDA{Cores.RESET}")
    print(f"{Cores.VERDE}   --------------------------------------------------{Cores.RESET}\n")

# --- MENUS ---
def menu_principal():
    cabecalho()
    print(f"{Cores.AZUL}[1]{Cores.RESET} 🔍 Identificar Planta (via IA)")
    print(f"{Cores.AZUL}[2]{Cores.RESET} 🌿 Cadastrar Nova Planta")
    print(f"{Cores.AZUL}[3]{Cores.RESET} 📋 Listar Inventário")
    print(f"{Cores.AZUL}[4]{Cores.RESET} 🗑️  Remover Planta")
    print(f"{Cores.AZUL}[0]{Cores.RESET} ❌ Sair")
    return input(f"\n{Cores.AMARELO}Escolha: {Cores.RESET}")

def fluxo_cadastro(crud):
    cabecalho()
    print("CADASTRO DE NOVA ESPÉCIE\n")
    print("1. Angiosperma (Flores/Frutos)")
    print("2. Gimnosperma (Pinheiros)")
    print("3. Pteridófita (Samambaias)")
    print("4. Briófita (Musgos)")
    tipo = input("\nTipo: ")
    
    try:
        nome_pop = input("Nome Popular: ")
        nome_ci = input("Nome Científico: ")
        regiao = input("Região/Habitat: ")
        altura = float(input("Altura Média (m): "))
        folhas = input("Comportamento Folhas: ")
    except ValueError:
        print("Erro: Altura deve ser número.")
        time.sleep(2)
        return

    nova_planta = None
    if tipo == '1':
        nova_planta = Angiosperma(nome_ci, nome_pop, regiao, altura, folhas, 
                                  input("Fruto: "), input("Cor Flor: "), input("Copa: "))
    elif tipo == '2':
        nova_planta = Gimnosperma(nome_ci, nome_pop, regiao, altura, folhas, 
                                  input("Tipo Folha: "), input("Semente: "))
    elif tipo == '3':
        nova_planta = Pteridofita(nome_ci, nome_pop, regiao, altura, folhas, 
                                  input("Caule: "), input("Fronde: "))
    elif tipo == '4':
        nova_planta = Briofita(nome_ci, nome_pop, regiao, altura, folhas, 
                               input("Substrato: "), input("Textura: "))
    
    if nova_planta:
        crud.adicionar_planta(nova_planta)
        print(f"\n{Cores.VERDE}Sucesso!{Cores.RESET}")
        time.sleep(1)

def fluxo_identificacao(crud, ia):
    cabecalho()
    plantas = crud.listar_plantas()
    if not plantas:
        print("Banco vazio. Cadastre algo primeiro.")
        time.sleep(2)
        return

    print(f"O banco tem {len(plantas)} plantas para comparação.")
    print(f"{Cores.AZUL}Iniciando o Botânico Virtual...{Cores.RESET}")
    
    sucesso, msg = ia.iniciar_identificacao(plantas)
    if not sucesso:
        print(f"Erro: {msg}")
        return

    print(f"{Cores.AMARELO}IA Pronta! Descreva a planta (digite 'sair' para voltar).{Cores.RESET}\n")

    while True:
        try:
            texto = input(f"{Cores.VERDE}Você: {Cores.RESET}")
            if texto.lower() in ['sair', 'voltar', 'exit']:
                break
            
            if not texto.strip():
                continue

            print(f"{Cores.AZUL}Botânico:{Cores.RESET}", end=" ", flush=True)
            resposta = ia.enviar_mensagem(texto)
            print(resposta + "\n")
            
        except KeyboardInterrupt:
            break
            
    input("\nSessão encerrada. Enter para voltar...")

def main():
    try:
        crud = CrudPlantas()
        
        try:
            botanico_ia = BotanicoAI()
            print("IA Conectada.")
        except Exception as e:
            botanico_ia = None
            print(f"IA Offline: {e}")
            time.sleep(1)

        while True:
            op = menu_principal()
            if op == '1':
                if botanico_ia: fluxo_identificacao(crud, botanico_ia)
                else: 
                    print("Erro: IA não configurada (.env).")
                    time.sleep(2)
            elif op == '2': fluxo_cadastro(crud)
            elif op == '3': 
                print(crud.listar_plantas())
                input("Enter...")
            elif op == '4':
                nome = input("Nome para remover: ")
                crud.remover_planta(nome)
            elif op == '0': break
            
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()