cliente --> consume (info, datos, etc, demanda)  --> frontend
sevidor --> aporta (informacion, datos, etc, oferta/escucha) --> backend

Este protocolo de comunicación empleado en la Web tiene ciertas características que debemos tener en cuenta: \

    Pedido-Respuesta: se abre una conexión por cada pedido, que surge del cliente, y el servidor la cierra cuando ha enviado la respuesta

    Stateless: el protocolo per-sé no maneja ninguna noción de memoria de pedidos anteriores

    Textual: se intercambian mensajes de sólo texto

    Basado en códigos de respuesta: incluso para los flujos de error; no hay memoria compartida, continuaciones, excepciones ni eventos

WebApp --> persistir informacion (guardar) en Base de Datos. 
Pagina Web --> estatico, no guarda informacion. No tiene asociada una BD. Archivo HTML expuesto en la nube
Sitio Web --> parecido a webapp. 

* Diferenciar Aplicacion rest de los demas --> la URL debe mapear los recursos
* HTTP --> protocolo // HTTP*S* es de security


