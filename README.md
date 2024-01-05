# Documentación de la API de Spread de Mercado

Este proyecto es una API web construida con Flask que permite obtener el spread de diferentes mercados de criptomonedas y establecer/obtener un "spread de alerta".

## Requisitos

- Python 3.6 o superior
- Flask
- Requests

## Instalación

1. Clonar este repositorio en la máquina local.
2. Instalar las dependencias. En la raíz del proyecto, ejecutar:

```bash
pip install -r requirements.txt
```
## Pruebas
Para probar la API, se puede usar herramientas como Postman o curl. Aquí hay ejemplos de cómo hacerlo:

- Para obtener el spread para todos los mercados:

curl -X GET http://localhost:5000/markets/spread

- Para obtener el spread para un mercado específico (por ejemplo, 'btc-clp'):

curl -X GET http://localhost:5000/markets/spread/btc-clp

- Para obtener el valor actual del "spread de alerta":

curl -X GET http://localhost:5000/alert/spread

- Para establecer el valor del "spread de alerta" (por ejemplo, a 1000):

curl -X POST -H "Content-Type: application/json" -d '{"spread":1000}' http://localhost:5000/alert/spread

## Pruebas Unitarias

Este proyecto incluye pruebas unitarias que verifican la funcionalidad de las funciones `get_market_data` y `calculate_spread`. Estas pruebas se encuentran en el archivo `test_main.py`.

Para ejecutar las pruebas unitarias, se puede usar el siguiente comando en la raíz del proyecto:

```bash
python -m unittest test_main.py
```