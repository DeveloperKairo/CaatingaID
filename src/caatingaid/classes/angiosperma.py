from caatingaid.classes.planta import Planta

class Angiosperma(Planta):
  def __init__(self, nome_cientifico, nome_popular, regiao_ceara, altura_media, comportamento_folhas, tipo_fruto, cor_flor, forma_copa):
    super().__init__(nome_cientifico, nome_popular, regiao_ceara, altura_media, comportamento_folhas)
    self.tipo_fruto = tipo_fruto
    self.cor_flor = cor_flor
    self.forma_copa = forma_copa

  def descrever_caracteristicas(self):
    return (f"Árvore de copa {self.forma_copa}, com flores {self.cor_flor} e frutos do tipo {self.tipo_fruto}.")
    
  def to_dict(self):
    dados = super().to_dict()
    dados["caracteristicas_especificas"] = {
      "tipo_fruto": self.tipo_fruto,
      "cor_flor": self.cor_flor,
      "forma_copa": self.forma_copa
    }

    return dados