# Demostración

En este directorio se encuentra un directorio de nombre `deposito`
con insumos que demuestran cómo trabaja Archivista.

## Configuración

Vea el archivo `settings.ini`

Vea la plantilla `plantilla.md.jinja2`

Vea la configuración de Pelican `pelicanconf.py`

## Caso 1: Apuntes tiene archivos md en cada directorio

Pendiente.

## Caso 2: Manuales tiene directorios clasificados por fechas

Pendiente.

## Caso 3: Presentaciones con archivos PDF para que se genere un índice automático

Pendiente.

## Pasos de la demostración

Crear el entorno virtual; instalar Pelican, Markdown, Click y Archivista

```bash
pip install pelican
```

```bash
cd tests
```

```bash
pelican-quickstart
```

```
> Where do you want to create your new web site? [.]
> What will be the title of this web site? Demostracion de Archivista
> Who will be the author of this web site? guivaloz
> What will be the default language of this web site? [en] es
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) n
> What is your time zone? [Europe/Rome] America/Mexico_City
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) n
```

Ejecutar Archivista

Construir el sitio web con Pelican

Ver en el navegador de internet
