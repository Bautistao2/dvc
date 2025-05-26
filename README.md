# ML + DVC + Docker Demo

Este repositorio muestra cómo entrenar un modelo de ML, guardar el resultado con `joblib`, y versionarlo usando **DVC**. El entorno completo está contenido en Docker para máxima portabilidad.

## Requisitos

- Docker
- Git
- (opcional) DVC instalado localmente para `dvc push/pull`

## Cómo usar

### 1. Construir la imagen Docker
```bash
docker build -t ml-dvc-demo .
```

### 2. Ejecutar el contenedor
```bash
docker run --name ml-demo -v $(pwd)/models:/app/models ml-dvc-demo
```

En Windows PowerShell, usa:
```powershell
docker run --name ml-demo -v ${PWD}/models:/app/models ml-dvc-demo
```

### 3. Verificar los resultados
Después de ejecutar el contenedor, se creará un modelo en la carpeta `models/` y se versionará con DVC.

### 4. (Opcional) Inspeccionar el contenedor
Si deseas entrar al contenedor para verificar el estado de DVC o ejecutar comandos adicionales:
```bash
docker exec -it ml-demo /bin/bash
```

## Solución de problemas

Si encuentras problemas con permisos de acceso a los archivos montados, asegúrate de que Docker tenga los permisos necesarios para acceder al directorio donde se encuentra el proyecto.
