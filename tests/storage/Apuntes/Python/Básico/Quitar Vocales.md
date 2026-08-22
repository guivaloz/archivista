## Quitar Vocales

Las funciones se definen con la palabra clave def, seguida del nombre de la función y sus parámetros.

El valor devuelto en las funciones con def será el dado con la instrucción return.

```python
def quitar_vocales(nombre):
    nombre_sin_vocales = ''
    for numero in range(0, len(nombre)):
        letra = nombre[numero].lower()
        if letra not in vocales:
            nombre_sin_vocales = nombre_sin_vocales + letra
    return(nombre_sin_vocales)
```

Ejecute la función

```python
print(quitar_vocales('Tim Berners-Lee'))
print(quitar_vocales('Richard Matthew Stallman'))
print(quitar_vocales('Linus Benedict Torvalds'))
```
