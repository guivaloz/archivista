## Tablas de Multiplicar

Crear una tabla de multiplicar del dos

```python
factor = 2
for numero in [1, 2, 3, 4, 5]:
    print(' {} x {} = {} '.format(numero, factor, numero * factor))
```

Crear muchas tablas de multiplicar

```python
for factor in range(1, 5):
    print(f'Tabla del {factor}')
    print()
    for numero in range(1, 5):
        print(f' {numero} x {factor} = {numero * factor} ')
    print()
```
