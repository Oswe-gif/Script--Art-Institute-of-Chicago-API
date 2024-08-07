# descripción:
El script tiene como propósito traer los datos de la API  [Art Institute of Chicago](https://api.artic.edu/docs/). Así mismo, se ha añadido la opción de insertar una imagen en el PDF.
# Previo
* Instalar las dependencias necesarias del proyecto. Estar ubicado en la raíz del proyecto y ejecutar ```pip install -r requirements.txt``` o ```py -m pip install -r requirements.txt```
* Crear un archivo .env (utilizando el archivo .env.example como referencia) e ingresar el correo del remitente junto con su contraseña.
# Reglas:
* No se puede usar las banderas --id (artwork específico) y --search/-s (conjunto de artworks) de manera simultánea, debido a que generaría un conflicto en la API. En caso de uso simultáneo, se ignoraría la bandera --search para dar prioridad a --id.
* No se puede usar las banderas --id (artwork específico) y --artworks/-a (filtra un conjunto de artworks) de manera simultánea, debido a que generaría un conflicto en la API. En caso de uso simultáneo, se ignoraría la bandera --artworks para dar prioridad a --id
# Banderas:
* --id: El identificador de los artworks
* --search/-s: Filtra los artworks
* --fields/-f: Muestra solo los campos especificados.
* --artworks/-a: Cantidad de artworks a observar
# Ejemplos de comandos:
* py script-Art-Institute-of-Chicago-API.py  --> Trae todos los datos
* py script-Art-Institute-of-Chicago-API.py --id --> Trae el artwork con el identificador especificado.
* py script-Art-Institute-of-Chicago-API.py --search war --> Trae los artworks que contengan la palabra war.
* py script-Art-Institute-of-Chicago-API.py -a 2 -f id,title -->Muestra los dos primeros artworks con los campos titulos e IDs.
* py script-Art-Institute-of-Chicago-API.py -s war -f id --> Muestra los IDs de los artworks filtrados por la palabra 'war'.
* 
