from flask import Flask,jsonify,request
from forex_python.converter import CurrencyRates


app = Flask("currency_App")

c = CurrencyRates()

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    source_currency = data['source_currency']
    target_currency = data['target_currency']
    amount = float(data['amount'])
    exchange_rate = c.get_rate(source_currency, target_currency)
    converted_amount = exchange_rate * amount
    result = {'source_currency': source_currency, 'target_currency': target_currency,'amount':amount,'converted_amount':converted_amount}
    return jsonify(result)
    


if __name__ == '__main__':
    
    app.run(debug = True)
