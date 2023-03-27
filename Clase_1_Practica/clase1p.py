"""

def retirar_dinero(saldo,retirar):
    saldob=saldo-retirar
    while saldob<=0:
        return 0
    return saldob
print(retirar_dinero(1000,1100))

def retirar_dinero(saldo,monto):
    return max(saldo-monto,0)
print(retirar_dinero(1000,10))



from xmlrpc.client import boolean

#ej6
def dia_de_la_semana_favorito(dia):
    return dia=="sabado"
print(dia_de_la_semana_favorito("sabado"))

#ej11
def param(palabra):
    if palabra[0]=="h":
        return len(palabra)
    else:
        return ("NOOO")
print(param("Holograma"))
"""
def ej13(parametro):
    return parametro.startswith("Buenos") or parametro.startswith("Bueno")
print(ej13("Buenos dias"))