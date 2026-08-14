>>> class Empleado:
...     def __init__(self, nombre, salario_base):
...         self.nombre = nombre
...         self.salario_base = salario_base
...     def calcular_pago(self):
...         return self.salario_base
...
>>>
>>> class Desarrollador(Empleado):
...     def __init__(self, nombre, salario_base, lenguaje_favorito):
...        super().__init__(nombre, salario_base)
...        self.lenguaje_favorito = lenguaje_favorito
...
>>> class Gerente(Empleado):
...     def __init__(self, nombre, salario_base, bono):
...         super().__init__(nombre, salario_base)
...         self.bono = bono
...     def calcular_pago(self):
...         return self.salario_base + self.bono
...
...
>>> dev = Desarrollador("carlos", 2500000, "python")
>>> gerente = Gerente("maria", 4000000, 1500000)
>>> print(f"pago de {dev.nombre}: ${dev.calcular_pago()}")
pago de carlos: $2500000
>>> print(f"pago de {dev.nombre}: ${dev.calcular_pago()}")
pago de carlos: $2500000
>>> print(f"pago de {gerente.nombre}: ${gerente.calcular_pago()}")
pago de maria: $5500000