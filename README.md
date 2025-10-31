# Proyecto RAG

## Configurar proyecto

### Inicializar proyecto
> Versión de python 3.12.11

```
cd <ruta_donde_guardar>

git clone https://github.com/garycdev/rag_bibliotecas

cd rag_bibliotecas
```

### Instalar entorno
```
python3 -m venv env
```

### Activar entorno
```
source env/bin/activate
```

### Instalar modulos necesarios (pesa algo de 8gb 😬🙃)
```
# Crear una carpeta temporal para la instalacion de dependencias
mkdir .tmp

# Usar esa carpeta como cache
export TMPDIR="$(pwd)/.tmp"

# Instalar las dependencias necesarias
pip install -r requirements.txt
```

### Configurar entorno post instalación
```
cp .env.copy .env
```
> Configurar variables

### Nota
- La instalación puede tardar
- Pesa alrededor de 8gb (dependencias para langchain, huggingface y OpenAI)

## Ejecutar con pm2
```
chmod +x start.sh

pm2 start start.sh --name fastapi-rag
```