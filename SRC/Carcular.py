import math

class CalculosEstadisticos:

    def calculo_media(self, num):
        """Calcular la media de una lista de números"""
        if not num:
            return None
        return sum(num) / len(num)
    def calcular_desviacion_estandar(self, num):
        """Calcular la desviación estándar muestral de una lista de números"""
        if not num:
            return None
        media = self.calculo_media(num)
        # Dividimos por (n-1) en lugar de n para desviación estándar muestral
        var = sum((x - media) ** 2 for x in num) / (len(num) - 1)
        return math.sqrt(var)