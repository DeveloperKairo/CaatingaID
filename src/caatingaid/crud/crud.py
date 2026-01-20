import json
import os
from pathlib import Path

from caatingaid.classes.angiosperma import Angiosperma
from caatingaid.classes.gimnosperma import Gimnosperma
from caatingaid.classes.pteridofita import Pteridofita
from caatingaid.classes.briofita import Briofita

class CrudPlantas:
    def __init__(self, nome_arquivo="banco_plantas.json"):

        pasta_atual = Path(__file__).resolve().parent
        
        pasta_raiz = pasta_atual.parent.parent.parent
        
        self.arquivo_db = pasta_raiz / nome_arquivo
        
        print(f"📂 Banco de dados localizado em: {self.arquivo_db}")

        self._plantas = []
        self._carregar_dados()

    def adicionar_planta(self, planta):
        self._plantas.append(planta)
        self._salvar_dados()
        print(f"✅ {planta.nome_popular} salva no banco de dados!")

    def listar_plantas(self):
        return [p.to_dict() for p in self._plantas]
    
    def buscar_por_nome(self, nome_popular):
        for p in self._plantas:
            if p.nome_popular.lower() == nome_popular.lower():
                return p
        return None

    def remover_planta(self, nome_popular):
        planta_encontrada = self.buscar_por_nome(nome_popular)
        if planta_encontrada:
            self._plantas.remove(planta_encontrada)
            self._salvar_dados()
            print(f"🗑️ {nome_popular} removida com sucesso.")
            return True
        print(f"⚠️ Planta {nome_popular} não encontrada.")
        return False
  
    def _salvar_dados(self):
        dados_para_salvar = [p.to_dict() for p in self._plantas]
        try:
            with open(self.arquivo_db, 'w', encoding='utf-8') as f:
                json.dump(dados_para_salvar, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f" Erro ao salvar arquivo: {e}")

    def _carregar_dados(self):
        if not self.arquivo_db.exists():
            return
    
        try:
            with open(self.arquivo_db, 'r', encoding='utf-8') as f:
                dados_brutos = json.load(f)

            self._plantas = []
            for item in dados_brutos:
                self._reconstruir_objeto(item)
            
            # Debug para você ver carregando
            if self._plantas:
                print(f" Carregadas {len(self._plantas)} plantas do arquivo.")

        except json.JSONDecodeError:
            print("Arquivo de banco de dados corrompido ou vazio. Iniciando novo.")
        except Exception as e:
            print(f"Erro ao ler banco: {e}")

    def _reconstruir_objeto(self, item_dict):
        tipo = item_dict.get("tipo")
        bio = item_dict.get("biometria", {})
        especifico = item_dict.get("caracteristicas_especificas", {})

        try: 
            nova_planta = None

            if tipo == "Angiosperma":
                nova_planta = Angiosperma(
                    nome_cientifico=item_dict["cientifico"],
                    nome_popular=item_dict["popular"],
                    regiao_ceara=item_dict["habitat"],
                    altura_media=bio.get("altura_media_metros"),
                    comportamento_folhas=bio.get("folhagem"),
                    tipo_fruto=especifico.get("tipo_fruto"),
                    cor_flor=especifico.get("cor_flor"),
                    forma_copa=especifico.get("forma_copa")
                )
            elif tipo == "Gimnosperma":
                nova_planta = Gimnosperma(
                    nome_cientifico=item_dict["cientifico"],
                    nome_popular=item_dict["popular"],
                    regiao_ceara=item_dict["habitat"],
                    altura_media=bio.get("altura_media_metros"),
                    comportamento_folhas=bio.get("folhagem"),
                    tipo_folha=especifico.get("tipo_folha"),
                    formato_semente=especifico.get("formato_semente")
                )
            elif tipo == "Pteridofita":
                nova_planta = Pteridofita(
                    nome_cientifico=item_dict["cientifico"],
                    nome_popular=item_dict["popular"],
                    regiao_ceara=item_dict["habitat"],
                    altura_media=bio.get("altura_media_metros"),
                    comportamento_folhas=bio.get("folhagem"),
                    tipo_caule=especifico.get("tipo_caule"),
                    tamanho_fronde=especifico.get("tamanho_fronde") 
                )
            elif tipo == "Briofita":
                nova_planta = Briofita(
                    nome_cientifico=item_dict["cientifico"],
                    nome_popular=item_dict["popular"],
                    regiao_ceara=item_dict["habitat"],
                    altura_media=bio.get("altura_media_metros"),
                    comportamento_folhas=bio.get("folhagem"),
                    substrato=especifico.get("substrato"),
                    aparencia_textura=especifico.get("aparencia_textura")
                )
            
            if nova_planta:
                self._plantas.append(nova_planta)

        except KeyError as e:
            print(f" Erro ao reconstruir {item_dict.get('popular')}: Faltando campo {e}")