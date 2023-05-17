import requests as rq, pandas as pd #request = pedido


#http --> requests --> python
#verbos HTTP --> disparan acciones particulares
# post --> verbo http asociado a percibir datos (De cero), generar nuevos datos de una entrada
# delete--> verbo asociado a http a borrar datos
# patch --> verbo asociado a reescribir datos

respuesta = rq.get("https://api.github.com/users/ajvelezrueda/orgs") # get --> verbo http asociado a las consultas
datos = respuesta.json()

#en cuantas orgs esta involucrados el usuario
print(len(datos))

#lista de nombres de las orgs en las q esta involucrado
print(respuesta.headers) #info asociada al request
print(respuesta.status_code) # status code de esta operacion es 403
"""
df= pd.DataFrame(datos)
print(df)
"""

