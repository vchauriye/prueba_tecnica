## Entrevista Tecnica

### Modo de Uso

* Para inicializar el proyecto, ubicarse en el directorio de \pokemon_data\frontend y utilizar el comando `npm install`, luego  ubicarse en el directorio de \pokemon_data\ y correr los comandos `python .\manage.py makemigrations`, `python .\manage.py migrate`. 

* Para correr el servidor de backend, ubicarse en el direcorio \pokemon_data y utilizar el comando `python .\manage.py runserver`

* Para correr el servidor de frontend, ubicarse en el directorio de \pokemon_data\frontend  y utilizar el comando `npm run server`

* Se utiliza el archivo pokemon_data\api\management\commands\migrate_data.py para poblar la base de datos con todos los pokemon. Para correr este comando se utiliza `python .\manage.py migrate_data` desde el directorio de \pokemon_data para poblar la base de datos con los pokemon

* Se debe ir a la url que se indica al correr el comando `python .\manage.py runserver`. Esta usualmente es http://127.0.0.1:8000/

Las librerias instaladas fueron:

* styled-components
* react-data-table-component
* @babel/core, @babel/preset-env, @babel/preset-react, babel-loader 
* react, react-dom, react-router-dom, webpack webpack-cli
* @mui/material, @emotion/react, @emotion/styled (instalados agregando el sufijo --legacy-peer-deps)
* npm install @mui/icons-material (instalados agregando el sufijo --legacy-peer-deps)
* django djangorestframework