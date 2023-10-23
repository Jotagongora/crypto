from django.http import JsonResponse
from config import PRIVATE_KEY_PATH
from config import PRIVATE_KEY_PASSWORD
import ccxt
import pdb


def get_binance_market_data(request):
    if not PRIVATE_KEY_PATH:
        raise Exception("PRIVATE_KEY_PATH no encontrada.")

    private_key_path = PRIVATE_KEY_PATH
    private_key_password = PRIVATE_KEY_PASSWORD

    pdb.set_trace()

    try:
        exchange = ccxt.binance()
        exchange.apiKey = None

        with open(private_key_path, 'rb') as f:
            private_key_data = f.read()

        exchange.options['private_key'] = {
            'pem': private_key_data,
            'password': private_key_password
        }

        # Obtiene datos de mercado de un par de trading específico, como BTC/USDT
        ticker = exchange.fetch_ticker('BTC/EUR')

        market_data = {
            'symbol': ticker['symbol'],
            'last_price': ticker['last'],
            'bid_price': ticker['bid'],
            'ask_price': ticker['ask'],
            'high_price': ticker['high'],
            'low_price': ticker['low'],
        }

        return JsonResponse(market_data)
    except ccxt.BaseError as e:
        return JsonResponse({'error': str(e)})
