from caatingaid.classes.planta import Planta

class Briofita(Planta):
  def __init__(self, nome_cientifico: str, nome_popular: str, regiao_ceara: str, altura_media: float, comportamento_folhas: str, substrato: str, aparencia_textura: str):
    super().__init__(nome_cientifico, nome_popular, regiao_ceara, altura_media, comportamento_folhas)
    self.substrato = substrato
    self.aparencia_textura = aparencia_textura

  def descrever_caracteristicas(self):
    return f"Cresce sobre {self.substrato}, textura {self.aparencia_textura}"
  
  def to_dict(self):
    dados = super().to_dict()
    dados["caracteristicas_especificas"] = {
      "substrato": self.substrato,
      "aparencia_textura": self.aparencia_textura
    }
    return dados
  