<h1 align=center> PROYECTO INDIVIDUAL Nº1 </h1>
# <h2 align=center>Machine Learning Operations (MLOps)</h1>
# <h3 align=center>AUTOR: GAZZIRO EDUARDO GAMAL</h1>
<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>

## **OBJETIVOS DEL PROYECTO:**

+ Contexto y rol:
Debemos realizar un modelo de recomendación entrenado dando unas buenas métricas. El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos, hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos. Nuestro objetivo tambien es desarrollar y practicar las habilidades necesarias para montar un proyecto de MLOps. 

**'REALIZAR UN PROCESO DE ETL'**

+ Procedemos primero con una limpieza de los Datos. Para ello instalamos las librerias pandas y numpy, vamos revisando cada una de las columnas para conocer que valores tiene, cuantos valores nulos tienen y que tipos de datos para finalmente poder realizar una limpieza bajo las especificaciones dadas.

**'DESARROLLAR QUERIES'**

+ Redactamos el codigo de la queries utilizando las librerias fastapi y pandas en el archivo main.py, estas fueron redactadas solo con lengiaje python y se utilizaron funciones de pandas que se encargan de filtrar el dataframe recibido hasta obtener los resultados que se piden.

**"MONTAR API's"**

+ Para montar la API se decidio utilizar fastapi disponibilizando el codigo del archivo y Deta (una nube personal) para hacer el deployment de la app sin necesidad de dockerizacion.

+['Deta Space']: https://deta.space/discovery/r/imdee19pww7a1qif

**'REALIZAR UN EDA'**

+ El análisis exploratorio de datos es el tratamiento estadístico al que se someten las muestras recogidas durante un proceso de investigación. Para mayor rapidez y precisión, todo el proceso suele realizarse por medios informáticos, con aplicaciones específicas para el tratamiento estadístico. Utilizamos la librerias de matplotlib y pandas para poder obtener graficos a partir de los dataframes que nos permitan transformar en información.
 

**'DESARROYAR UN MODELO DE MACHINE LEARNING'**

+ Machine Learning es una disciplina del campo de la Inteligencia Artificial que, a través de algoritmos, dota a los ordenadores de la capacidad de identificar patrones en datos masivos y elaborar predicciones. Para desarrollar este modelo necesitamos de datos numericos en un dataframe que esten limpios y completos. Luego de esto uilizamos las librerias de pandas, sklearn, math y matplotlib para escribir el codigo que nos permita ejecitar el modelo de machine learning.

## **LIBRERIAS UILIZADAS:**

+ squldf: implementa lenguaje SQL en Python
+ pandas: permite el manejo de DataFrames 
+ numpy: permite el manejo de arrays numericos
+ fastapi: permite montar una API
+ matplotlib: permite desarrollar graficas
+ sklearn: permite contruir un modelo de entrenamiento para machine learning
+ math: proporciona acceso a las funciones matemáticas definidas

## Los Archivos .csv necsesarios se encuentran en el siguente link: 
https://drive.google.com/drive/folders/16zZ5dXUrL9dzJojhp91ePInOQh9Ip7F9?usp=sharing
 (se recomienda descargar los archivos y colocarlos en la misma carpeta)

## Estructura del proyecto
| Nombre archivo | Contenido|
|----------------|----------|
| **main.py** |  Código que se subio a Deta Space, con las Querys solicitadas |
| **Proyecto-1.ipynb** | Limpieza del set de datos de las Plataformas |
| **README.md** | Explicació del proyecto |
| **Modelo_ML** | Modelo de Machine Learning |
| **Unioncsv.ipynb** | Jupyter notebook con la limpieza de datos y el entrenamiento del modelo |
