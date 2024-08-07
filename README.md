# descripción:
El script tiene como propósito traer los datos de la API  [Art Institute of Chicago](https://api.artic.edu/docs/). Así mismo, se ha añadido la opción de insertar una imagen en el PDF.
# Previo
* Instalar las dependencias necesarias del proyecto. Estar ubicado en la raíz del proyecto y ejecutar ```pip install -r requirements.txt``` o ```py -m pip install -r requirements.txt```
* Crear un archivo .env (utilizando el archivo .env.example como referencia) e ingresar el correo del remitente y una [contraseña de aplicación](https://profinomics.com/crear-contrasena-de-aplicacion-gmail/#:~:text=Para%20generar%20una%20contrase%C3%B1a%20de%20aplicaci%C3%B3n%20en%20Gmail%2C,en%20%E2%80%9CAcceder%20a%20contrase%C3%B1as%20de%20aplicaci%C3%B3n%E2%80%9D.%20M%C3%A1s%20elementos) generada de Gmail.
* Tener activado el doble factor de autenticación en el correo remitente.
* # Banderas:
* ```--id```: filtra el artwork con el identificador [Número]
* ```--search/-s```: Filtra los artworks [Palabra]
* ```--fields/-f```: Muestra solo los campos especificados. [id, title, _score, image_id]
* ```--artworks/-a```: Cantidad de artworks a observar [Número]
*  ```--mail/-m ```: Correo electrónico del destinatario al que se enviará el PDF
# Reglas:
* Campos que acepta el script ` [id, title, _score, image_id] `
* El campo _score solo aparece cuando se realizan búsquedas mediante el comando ```--search/-s```
* No se puede usar las banderas ```--id``` (artwork específico) y ```--search/-s``` (conjunto de artworks) de manera simultánea, debido a que generaría un conflicto en la API. En caso de uso simultáneo, se ignoraría la bandera ```--search``` para dar prioridad a ```--id```.
* No se puede usar las banderas ```--id``` (artwork específico) y --artworks/-a (filtra un conjunto de artworks) de manera simultánea, debido a que generaría un conflicto en la API. En caso de uso simultáneo, se ignoraría la bandera --artworks para dar prioridad a ```--id```
# Ejemplos de comandos:
* ```py script-Art-Institute-of-Chicago-API.py```  --> Trae todos los datos
* ```py script-Art-Institute-of-Chicago-API.py --id 129884``` --> Trae el artwork con el identificador especificado.
* ```py script-Art-Institute-of-Chicago-API.py --search war``` --> Trae los artworks que contengan la palabra war.
* ```py script-Art-Institute-of-Chicago-API.py -a 2 -f id,title_``` -->Muestra los dos primeros artworks con los campos titulos e IDs.
* ```py script-Art-Institute-of-Chicago-API.py -s war -f id,image_id,_score``` --> Muestra los IDs de los artworks filtrados por la palabra 'war'.
  
