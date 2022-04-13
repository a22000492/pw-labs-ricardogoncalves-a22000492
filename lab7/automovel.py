class Automovel:
  def __init__(self, capacidade_combustivel, quant_combustivel, consumo):
    self.capacidade_combustivel = capacidade_combustivel
    self.quant_combustivel = quant_combustivel
    self.consumo = consumo

  def combustivel(self):
    return self.quant_combustivel

  def autonomia(self):
    return self.quant_combustivel / self.consumo

  def abastece(self, n_litros):
    if self.quant_combustivel + n_litros <= self.capacidade_combustivel:
      self.quant_combustivel += n_litros
      return self.quant_combustivel
    return "Excedeu o máximo"

  def percorre(self, n_km):
    if self.quant_combustivel / self.consumo >= n_km:
      self.quant_combustivel -= self.consumo * n_km
      return self.quant_combustivel
    return "Não é possível percorrer a distância"
    
