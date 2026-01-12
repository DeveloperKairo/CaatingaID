import json
import os
from caatingaid.classes.angiosperma import Angiosperma
from caatingaid.classes.gimnosperma import Gimnosperma
from caatingaid.classes.pteridofita import Pteridofita
from caatingaid.classes.briofita import Briofita

class CrudPlantas:
  def __init__(self, arquivo_db="banco_pantas.json"):
    self.arquivo_db = arquivo_db
    self._plantas = []
    self._carregar_dados()

  def adicionar_planta(self, planta):
    self._plantas.append(planta)
    self._salvar_dados()
    print(f"{planta.nome_popular} salva no banco de dados!")

  def listar_plantas(self):
    return [p.to_dict() for p in self._plantas]
  
  def remover_planta(self, nome_popular):
    planta_encontrada = self.buscar_por_nome(nome_popular)
    if planta_encontrada:
      self._plantas.remove(planta_encontrada)
      self._salvar_dados()
      print(f"{nome_popular} removida com sucesso.")
      return True
    return False
  
  def _salvar_dados(self):
    dados_para_salvar = [p.to_dict() for p in self._plantas]
    with open(self.arquivo_db, 'w', encoding='utf-8') as f:
      json.dump(dados_para_salvar, f, ensure_ascii=False, indent=4)

  def _carregar_dados(self):
    if not os.path.exists(self.arquivo_db):
      return
    
    try:
      with open(self.arquivo_db, 'r', encoding='utf-8') as f:
        dados_brutos = json.load(f)

      self._plantas = []
      for item in dados_brutos:
        self._reconstruir_objeto(item)

    except json.JSONDecodeError:
      print("Erro ao ler o banco de dados. Iniciando sem dados")

  def _reconstruir_objto(self, item_dict):
    tipo = item_dict.get("tipo_botanico")

    bio = item_dict.get("biometria", {})
    especifico = item_dict.get("caracteristicas_especificas", {})

    try: 
      if tipo == "Angiosperma":
        nova_planta = Angiosperma(
          nome_cientifico=item_dict["nome_cientifico"],
          nome_popular=item_dict["nome_popular"],
          regiao_ceara=item_dict["habitat"],
          altura_media=bio.get("altura_media_metros"),
          comportamento_folhas=bio.get("folhagem"),
          tipo_fruto=especifico.get("tipo_fruto"),
          cor_flor=especifico.get("cor_flor"),
          forma_copa=especifico.get("forma_copa")
        )
      elif tipo == "Gimnosperma":
        nova_planta = Gimnosperma(
          nome_cientifico=item_dict["nome_cientifico"],
          nome_popular=item_dict["nome_popular"],
          regiao_ceara=item_dict["habitat"],
          altura_media=bio.get("altura_media_metros"),
          comportamento_folhas=bio.get("folhagem"),
          tipo_folha=especifico.get("tipo_folha"),
          formato_semente=especifico.get("formato_semente")
        )
      elif tipo == "Pteridofita":
        nova_planta = Pteridofita(
        nome_cientifico=item_dict["nome_cientifico"],
        nome_popular=item_dict["nome_popular"],
        regiao_ceara=item_dict["habitat"],
        altura_media=bio.get("altura_media_metros"),
        comportamento_folhas=bio.get("folhagem"),
        tipo_caule=especifico.get("tipo_caule"),
        tamanho_fronde=especifico.get("tamanho_fronde") 
        )
      elif tipo == "Briofita":
        nova_planta = Briofita(
          nome_cientifico=item_dict["nome_cientifico"],
          nome_popular=item_dict["nome_popular"],
          regiao_ceara=item_dict["habitat"],
          altura_media=bio.get("altura_media_metros"),
          comportamento_folhas=bio.get("folhagem"),
          substrato=especifico.get("substrato"),
          aparencia_textura=especifico.get("aparencia_textura")
        )
      else:
        print(f"Tipo desconhecido no banco: {tipo}")
        return
      
      self._plantas.append(nova_planta)

    except KeyError as e:
      print(f"Erro ao reconstruir {item_dict.get('nome_popular')}: Faltando campo {e}")