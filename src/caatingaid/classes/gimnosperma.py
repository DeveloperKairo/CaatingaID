from caatingaid.classes.planta import Planta

class Gimnosperma(Planta):
  def __init__(self, nome_cientifico, nome_popular, regiao_ceara, altura_media, comportamento_folhas, tipo_folha, formato_semente):
    super().__init__(nome_cientifico, nome_popular, regiao_ceara, altura_media, comportamento_folhas)
    self.tipo_folha = tipo_folha
    self.formato_semente = formato_semente

  def descrever_caracteristicas(self):
    return f"Sementes nuas ({self.formato_semente}) e folhas {self.tipo_folha}."
  
  def to_dict(self):
    dados = super().to_dict()
    dados["caracteristicas_especificas"] = {
      "tipo_folha": self.tipo_folha,
      "formato_semente": self.formato_semente
    }
    return dados