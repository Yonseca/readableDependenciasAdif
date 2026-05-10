# ¿Qué es esto?
Este repositorio contiene un pequeño script en python que extrae los datos existentes de las dependencias de Adif en formato CSV, JSON y KML. Estos datos se proporcionan en el conjunto de datos "Tramificación común de ADIF", disponible [aquí](https://ideadif.adif.es/catalog/srv/spa/catalog.search#/metadata/28323796-c2ed-4bb2-bb85-4b6e93ea3334).

# ¿Dónde están los ficheros?
En la carpeta [files](https://github.com/Yonseca/readableDependenciasAdif/tree/main/files), en este mismo respositorio.

# ¿Cómo puedo usar los ficheros?
Como quieras. Recuerda mencionar la autoría de Adif. 

# ¿Quién es el autor de los datos?
© Administrador de infraestructuras ferroviarias
(Adif, dicho en corto)

# ¿Hay que citar a alguien si hago uso de los datos?
Según la web de donde salen los datos, sí. Añade un «© Administrador de infraestructuras ferroviarias» en algún sitio que se vea y úsalos como mejor te venga.

# ¿Cómo uso el script?
No hace falta: el resultado son los tres ficheros de la carpeta [files](https://github.com/Yonseca/readableDependenciasAdif/tree/main/files). Si aún así quieres meterle mano o lo queires ejecutar porque crees que hay datos más recientes, puedes:
1. Clonar el repositorio:  
        `git clone git@github.com:Yonseca/readableDependenciasAdif.git`
2. Entrar a la carpeta del proyecto y descarga las dependencias:  
        `pip install -r requirements.txt`
3. Ejecutar el script  
        `python get_dependencias_ideadif.py`

# ¿Con qué puedo abrir los ficheros?
Con un editor de texto o código normalito (Bloc de notas, Visual Studio Code, Gedit...). En el caso concreto del fichero CSV, se puede abrir directamente como hoja de cálculo, con Excel o LibreOffice. Si al abrir de pregunta cuál es la codificación de caracteres, es UTF-8.
