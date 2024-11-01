class PrecioProductoDescuento:
    def calcular_precio_final(precio, descuento):
        if not isinstance(precio, (int, float)) or not isinstance(descuento, (int, float)):
            raise TypeError("El precio y el descuento deben ser numéricos.")
        if precio < 0 or descuento < 0:
            raise ValueError("El precio y el descuento deben ser positivos.")
        return precio*(1-descuento/100)

