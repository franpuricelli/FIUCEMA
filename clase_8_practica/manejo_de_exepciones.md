_TIPOS DE ERRORES_

## ERROR DE SINTAXIS ##

1) SyntaxError:

    - Ocurre cuando Python encuentra un error de sintaxis. Es decir, cuando encuentra una instrucción que no sigue las reglas de sintaxis del lenguaje.
    
    - Ejemplo:
>>> print(Hola mundo')
  File "<stdin>", line 1
    print(Hola mundo')
               ^
SyntaxError: invalid syntax

## EXCEPCIONES ## 

2) NameError:

    - Ocurre cuando Python encuentra un nombre que no puede asociar con ningún objeto.

    - Ejemplo:
>>> print(divisor)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

NameError: name 'divisor' is not defined

3) TypeError:

    - Ocurre cuando Python encuentra un operador o función que se aplica a un objeto de tipo inadecuado.

    - Ejemplo:
>>> 0 + "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

4) ZeroDivisionError:

    - Ocurre cuando se intenta dividir un número por cero.

    - Ejemplo:
>>> 3 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ZeroDivisionError: division by zero

## PREVEER EXCEPCIONES PARA QUE NO SE INTERRUMPA LA EJECUCUÓN ## 

Bueno, para el manejo de excepciones Python nos provee palabras reservadas, que nos permiten manejar las excepciones que puedan surgir y tomar acciones que evitan la interrupción del programa o permitan especificar información adicional antes de interrumpir el programa. Una de las palabras reservadas es try, esta nos permite "encapsular" un bloque de código para interceptar e identificar excepciones. Si se produce un error dentro de la declaración try-except, se omite una excepción y se ejecuta el bloque de código que maneja la excepción.

try:
    # aquí ponemos el código que puede lanzar excepciones
except:
    # entrará aquí en caso que se haya producido una excepción