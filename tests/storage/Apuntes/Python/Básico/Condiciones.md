## Condiciones

Una sentencia condicional if ejecuta su bloque de código interno solo si se cumple cierta condición. Se define usando la palabra clave if seguida de la condición, y el bloque de código. Condiciones adicionales, si las hay, se introducen usando elif seguida de la condición y su bloque de código. Todas las condiciones se evalúan secuencialmente hasta encontrar la primera que sea verdadera, y su bloque de código asociado es el único que se ejecuta. Opcionalmente, puede haber un bloque final (la palabra clave else seguida de un bloque de código) que se ejecuta solo cuando todas las condiciones fueron falsas.

```python
fruta_1 = 'manzana'
fruta_2 = 'MANZANA'

if fruta_1 == fruta_2:
    print('Son iguales')
else:
    print('Son diferentes')
    if len(fruta_1) > len(fruta_2):
        print('Tiene más letras el primero')
    elif len(fruta_1) == len(fruta_2):
        print('Tienen la misma cantidad de letras')
    else:
        print('Tiene más letras el segundo')

if fruta_1.lower() == fruta_2.lower():
    print('Si las cambio a minúsculas ¡SON IGUALES!')
```
