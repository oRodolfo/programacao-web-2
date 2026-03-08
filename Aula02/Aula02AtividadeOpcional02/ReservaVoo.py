class ReservaVoo:
    def calcular_passagem(self, valor_base, assento_especial = None):
        if assento_especial is None:
            return valor_base

        return valor_base + assento_especial