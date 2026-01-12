from abc import ABC, abstractmethod

class Planta(ABC):
  def __init__(self, nome_cientifico:str, nome_popular:str, regiao_ceara:str, altura_media: float, comportamento_folhas: str):
    self._nome_cientifico = nome_cientifico
    self._nome_popular = nome_popular
    self._regiao_ceara = regiao_ceara
    self._altura_media = altura_media
    self._comportamento_folhas = comportamento_folhas

  @property
  def nome_popular(self):
    return self._nome_popular
  
  @abstractmethod
  def descrever_caracteristicas(self):
    pass

  def to_dict(self):
    return {
      "tipo": self.__class__.__name__,
      "cientifico": self._nome_cientifico,
      "popular": self._nome_popular,
      "habitat": self._regiao_ceara,
      "biometria": {
        "altura_media_metros": self._altura_media,
        "folhagem": self._comportamento_folhas
      },
      "detalhes_especificos": self.descrever_caracteristicas()
    }