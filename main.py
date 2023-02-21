#API


from fastapi import FastAPI
import pandas as pd
app = FastAPI()

df = pd.read_csv("dfdef.csv")

@app.get("/")
def presentacion():
    return "Proyecto Individual 01 - Eduardo Gamal Gazziro. Gracias por Utilizar mi api!"

#QUERY NUMERO 1 GET_MAX_DURATION

@app.get("/get_max_duration/{year}/{platform}/{duration_type}")
def get_max_duration(anio: int, plataforma, tipo_de_duracion):
    # Recibe: una plataforma, duración en minutos o temporadas y anio de estreno

    # canal: guarda las filas del df que contienen en su columna 'id' la primer letra de la variable plataforma 
    canal= df[df['id'].str.contains(plataforma[0], case= False)]
    # filtro: guarda las filas de la variable canal en las que la columna 'relase_year' coincide con la variable anio
        # la columna type contiene el valor movie y duration_type es igual a tipo_de_duracion
    filtro= canal[(canal.release_year == anio) & (canal.type== 'movie') & (canal.duration_type == tipo_de_duracion)]
    # duracion: crea un dataframe con solo tres columnas de la variable filtro 
    #   y guarda solamente la pelicula con el numero mas alto en duration_init  
    duracion= filtro[['title','duration_int', 'duration_type']].loc[filtro.duration_int.idxmax()] 
    # pelucula: guarda la variable duracion y la tranforma en un diccionario
    pelicula= duracion.T.to_dict()
    return pelicula
    
#  QUERY 2

@app.get('/get_score_coun/{plataforma}/{puntaje}/{anio}') # tercera ruta
def get_score_count(plataforma, puntaje: int, anio: int):
    #canal: guarda las filas del df que contienen en su columna 'id' la primer letra de la variable plataforma 
    canal= df[df['id'].str.contains(plataforma[0], case= False)]
    #cantidad: guarda las filas guardadas en canal cuyo valor en la columna score es mayor a puntaje
        # y su valor en la columna release_year sea igual a anio 
        # y su valor en la columna type coresponda a 'movie'
    cantidad= canal[(canal.score > puntaje) & (canal.release_year == anio)& (canal.type== 'movie')]
    return (f'De la plataforma:{plataforma}, la cantidad de películas con un puntaje de {puntaje} o mas es:{len(cantidad)}')

    
# QUERY 3
    
@app.get("/get_count_platform/{plataforma}")
def get_count_platform(plataforma: str):
    #canal: guarda las filas del df que contienen en su columna 'id' la primer letra de la variable plataforma 
    canal= df[df['id'].str.contains(plataforma[0], case= False)]
    #filtro: guarda las filas de canal que en la columna type su valor es ugual a movie
    filtro= canal[(canal.type== 'movie')]
                                    # len(filtro) cuenta las filas del df filtro
    return(f'La Cantidad de Películas es {len(filtro)} Para la Plataforma {plataforma}')


#QUERY 4

@app.get("/get_actor/{platform}/{year}")
def get_actor(platform:str, year:int):
    #selected_df: guarda las filas del df que contienen en su columna 'id' la primer letra de la variable plataforma 
    selected_df= df[df['id'].str.contains(platform[0], case= False)]

    #df_year: guarda las filas que en la columna relase_year coinciden con year 
    df_year = selected_df[selected_df['release_year'] == year]
    
    #actor_counts: divide los nombres de los actores en una lista y cuenta las concurrencias de cada uno
    actor_counts = df_year['cast'].str.split(',').explode().str.strip().value_counts()
    
    #most_frequent_actor: devuelve el nombre del actor más frecuente
    most_frequent_actor = actor_counts.index[0]
    
    return (f"La persona que mas se repite es {most_frequent_actor}")