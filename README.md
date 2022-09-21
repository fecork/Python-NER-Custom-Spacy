# ENTRENAR CUSTOM MODEL NER en SPACY

_El presente código tiene las utilidades para realizar un entrenamiento de un NER usando Spacy_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

Entorno de trabajo virtual con Pipenv, instalar.

```
pip install pipenv
```

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

instalar librerías

```
pipenv install
```

iniciar entorno

```
pipenv shell
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Preparar datos ⚙️

en data en la carpeta 01_raw, van los datos crudos, ejecutamos

```
python sort_data_to_tag.py
```

para generar el archivo txt que etiquetaremos, para más información sobre las
etiquetas
revisar [Wiki](https://fecork.notion.site/Entrenar-un-Custom-NER-Model-con-Spacy-b0380909219641a58fdb79cade31ea75)

## Entrenar Modelo ⌨️

Ejecutar el archivo en Notebook para realizar el entrenamiento en Google Colab

## Probar Modelo

Ejecutar

    python test_model.py

o ejecutar el archivo guardado en Notebook

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

- [Spacy](https://spacy.io/usage/spacy-101) - NLP

## Wiki 📖

revisar [Wiki](https://fecork.notion.site/Entrenar-un-Custom-NER-Model-con-Spacy-b0380909219641a58fdb79cade31ea75)

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

- **Wilberth Ferney Córdoba Canchala** - _Trabajo Inicial_ - [LinkenId](https://github.com/villanuevand)

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

- Comenta a otros sobre este proyecto 📢
- Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
- Da las gracias públicamente 🤓.
- etc.
