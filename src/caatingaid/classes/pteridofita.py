from caatingaid.classes.planta import Planta

class Pteridofita(Planta):
  def __init__(self, nome_cientifico, nome_popular, regiao_ceara, altura_media, comportamento_folhas, tipo_caule, tamanho_fronde):
    super().__init__(nome_cientifico, nome_popular, regiao_ceara, altura_media, comportamento_folhas)
    self.tipo_caule = tipo_caule
    self.tamanho_fronde = tamanho_fronde

  def descrever_caracteristicas(self):
    return f"Caule tipo {self.tipo_caule} e frondes {self.tamanho_fronde}."
  
  def to_dict(self):
    dados = super().to_dict()
    dados["caracteristicas_especificas"] = {
      "tipo_caule": self.tipo_caule,
      "tamanho_fronde": self.tamanho_fronde
    }
    return dados