# ENTRENAR CUSTOM MODEL NER en SPACY

_El presente c贸digo tiene las utilidades para realizar un entrenamiento de un NER usando Spacy_

## Comenzando 馃殌

_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 馃搵

Entorno de trabajo virtual con Pipenv, instalar.

```
pip install pipenv
```

### Instalaci贸n 馃敡

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

instalar librer铆as

```
pipenv install
```

iniciar entorno

```
pipenv shell
```

_Finaliza con un ejemplo de c贸mo obtener datos del sistema o como usarlos para una peque帽a demo_

## Preparar datos 鈿欙笍

en data en la carpeta 01_raw, van los datos crudos, ejecutamos

```
python sort_data_to_tag.py
```

para generar el archivo txt que etiquetaremos, para m谩s informaci贸n sobre las
etiquetas
revisar [Wiki](https://fecork.notion.site/Entrenar-un-Custom-NER-Model-con-Spacy-b0380909219641a58fdb79cade31ea75)

## Entrenar Modelo 鈱笍

Ejecutar el archivo en Notebook para realizar el entrenamiento en Google Colab

## Probar Modelo

Ejecutar

    python test_model.py

o ejecutar el archivo guardado en Notebook

## Construido con 馃洜锔?

_Menciona las herramientas que utilizaste para crear tu proyecto_

- [Spacy](https://spacy.io/usage/spacy-101) - NLP

## Wiki 馃摉

revisar [Wiki](https://fecork.notion.site/Entrenar-un-Custom-NER-Model-con-Spacy-b0380909219641a58fdb79cade31ea75)

## Autores 鉁掞笍

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

- **Wilberth Ferney C贸rdoba Canchala** - _Trabajo Inicial_ - [LinkenId](https://github.com/villanuevand)

## Licencia 馃搫

Este proyecto est谩 bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 馃巵

- Comenta a otros sobre este proyecto 馃摙
- Invita una cerveza 馃嵑 o un caf茅 鈽? a alguien del equipo.
- Da las gracias p煤blicamente 馃.
- etc.
