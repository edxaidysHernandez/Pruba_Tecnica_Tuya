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

Edita las rutas en `main.py` y ejecuta:
```python
paths = ["tu/carpeta", "archivo.html"]
```
```bash
python main.py
```
## Resultado

## Ejemplo

**Antes — `index.html`**
```html
<html>
  <body>
    <img src="images/foto.png">
    <img src="images/logo.jpg">
  </body>
</html>
```

**Después — `index_base64.html`**
```html
<html>
  <body>
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwADhQGAWjR9awAAAABJRU5ErkJggg==">
    <img src="data:image/jpg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAABAAEDASIAAhEBAxEB/8QAFAABAAAAAAAAAAAAAAAAAAAACf/EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAUAQEAAAAAAAAAAAAAAAAAAAAA/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8AJQAB/9k=">
  </body>
</html>
```

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
