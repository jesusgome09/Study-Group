# Crear repositorio en GH, clonarlo a la pc, modificarlo y volver a subirlo: 
  
 1. Crear repo en GH con Readme 
 2. Copiar url del repo 
 3. En consola, en la carpeta destino: 
      git clone <url> 
 4. Al terminar de trabajar en los archivos: 
      git status (muestra archivos modificados/agregados) 
 5. Agregar los archivos modificados que se van a subir al repo 
      git add <nombre archivo> <nombre archivo> /o/ git add . (todos) 
 6. Crear el commit con la descripción: 
      git commit -m "Se modificaron los archivos..." 
 7. Chequear que el nombre de remote sea origin: 
      git remote (debe devolver origin) 
 8. Enviar los archivos a GitHub: 
         git push origin main  
  
 --Repositorio actualizado--

# Subir proyecto creado en PC a nuevo repositorio en GH: 
 1. En consola ir a la carpeta y hacerla un repo git: 
         git init 
 2. Ver lista de archivos que se pueden subir: 
         git status 
 3. Agregar los archivos que se van a subir al repo: 
         git add <nombre archivo> <nombre archivo> /o/ git add . (todos) 
 4. Revisar que los archivos están preparados correctamente: 
         git status 
 5. Crear el commit: 
         git commit -m "Descripción del commit" 
 6. Ir a GH, crear el repo SIN README y copiar URL 
 7. Crear enlace de remote con la carpeta local: 
         git remote add origin <URL> 
 8. Subir los archivos a GH: 
         git push origin master 
  
 --Repositorio actualizado--

 # Modificar el proyecto remoto y actualizar el local: 
 1. Modificar el proyecto, guardarlo con su commit 
 2. En consola, revisar que no haya commits pendientes: 
         git status 
 3. En consola ir a la carpeta origen y ejecutar: 
         git pull origin main (o la rama que sea) 
  
 --El proyecto local esta sincronizado con el remoto--

 # Modificar el proyecto local y actualizar el remoto: 
 1. Una vez concretadas las modificaciones, en consola ir  
 a la carpeta raiz y ver el estado de los archivos: 
         git status 
 2. Agregar los archivos modificados que se van a subir al repo 
         git add <nombre archivo> <nombre archivo> /o/ git add . (todos) 
 3. Crear el commit con la descripción: 
         git commit -m "Se modificaron los archivos..." 
 4. Chequear que el nombre de remote sea origin: 
         git remote (debe devolver origin) 
 5. Chequear que la rama sea "Master" o "Main" o las que haya: 
         git branch 
 6. Enviar los archivos a GitHub: 
         git push origin main (o master, segun punto anterior) 
  
 --Repositorio actualizado--

 # Eliminar archivos en equipo local via CMD y actualizar online 
  
 1. Abrir CMD 
 2. Ir a la ubicacion del archivo 
 3. Ejecuta 
         git rm archivo1.txt 
 4. Agregar un comentario por la eliminacion (opcional) 
         git commit -m "Se eliminó por innecesario" 
 5. Ejecuta para enviar los cambios al repositorio remoto 
         git push
