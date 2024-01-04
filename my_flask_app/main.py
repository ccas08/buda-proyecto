from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Spread de "alerta"
alert_spread = 0

def get_market_data(market):
    """
    Esta función toma un mercado como argumento, hace una solicitud GET a la API de Buda para obtener los datos del ticker del mercado y devuelve la respuesta en formato JSON.
    """
    response = requests.get(f'https://www.buda.com/api/v2/markets/{market}/ticker')
    response.raise_for_status()
    return response.json()

def calculate_spread(market_data):
    """
    Esta función toma los datos del mercado en formato JSON, extrae el precio de oferta más alto (`max_bid`) y el precio de demanda más bajo (`min_ask`), y calcula la diferencia (spread) entre ellos.
    """
    bid = float(market_data['ticker']['max_bid'][0])
    ask = float(market_data['ticker']['min_ask'][0])
    return ask - bid

@app.route('/markets/spread', methods=['GET'])
def get_all_markets_spread():
    """
    Esta ruta GET devuelve el spread para todos los mercados especificados en la lista `markets`.
    """
    markets = ['btc-clp', 'eth-clp', 'ltc-clp', 'bch-clp']  
    spreads = {market: calculate_spread(get_market_data(market)) for market in markets}
    return jsonify(spreads)

@app.route('/markets/spread/<market>', methods=['GET'])
def get_market_spread(market):
    """
    Esta ruta GET toma un parámetro de ruta, 'market', y devuelve el spread para ese mercado específico.
    Primero, obtiene los datos del mercado utilizando la función 'get_market_data(market)' y luego calcula el spread utilizando la función 'calculate_spread(market_data)'.
    Finalmente, devuelve el spread en formato JSON.
    """
    spread = calculate_spread(get_market_data(market))
    return jsonify({market: spread})

@app.route('/alert/spread', methods=['GET'])
def get_alert_spread():
    """
    Esta ruta GET devuelve el valor actual del "spread de alerta" en formato JSON.
    El "spread de alerta" es un valor global que se puede establecer mediante la ruta POST '/alert/spread'.
    """
    return jsonify({'alert_spread': alert_spread})

@app.route('/alert/spread', methods=['POST'])
def set_alert_spread():
    """
    Esta ruta POST establece el valor del "spread de alerta" a partir del cuerpo de la solicitud HTTP.
    El nuevo valor del "spread de alerta" se extrae del cuerpo de la solicitud con 'request.json.get('spread', 0)'.
    Si no se proporciona un nuevo valor, se establece en 0 por defecto.
    Finalmente, devuelve el nuevo valor del "spread de alerta" en formato JSON.
    """
    global alert_spread
    alert_spread = request.json.get('spread', 0)
    return jsonify({'alert_spread': alert_spread})

if __name__ == '__main__':
    app.run(debug=True)