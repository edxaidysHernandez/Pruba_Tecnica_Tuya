# HTML Image Processor

Script en Python que recorre archivos HTML, extrae las imágenes 
de los tags `<img>`, las convierte a Base64 y genera un archivo 
nuevo sin modificar el original.

## ¿Qué hace?

- Recibe archivos HTML o directorios (incluyendo subdirectorios)
- Detecta todas las imágenes con tag `<img>`
- Convierte cada imagen a Base64
- Genera un archivo nuevo `index_base64.html` sin tocar el original
- Retorna un reporte con las imágenes exitosas y las que fallaron

## Estructura
```
html_processor/
├── main.py            # punto de entrada
├── file_finder.py     # busca archivos HTML
├── html_parser.py     # extrae los <img>
├── image_encoder.py   # convierte a Base64
└── html_processor.py  # orquesta el proceso
```

## Cómo ejecutar

## Cómo ejecutar

Edita las rutas en `main.py` y ejecuta:
```python
paths = ["tu/carpeta", "archivo.html"]
```
```bash
python main.py
```
## Resultado
```python
{
    "success": {
        "images/foto.png": "ruta/completa/foto.png"
    },
    "fail": {
        "images/missing.png": "FileNotFoundError: No such file..."
    }
}
```
