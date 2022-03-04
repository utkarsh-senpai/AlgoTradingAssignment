import math
from binance.futures import Futures 

client = Futures()
time = client.time()['serverTime']
print(client.time())
print(time)
mark_price = float(client.mark_price('BTCUSDT')['markPrice'])
print(mark_price)
client = Futures(key='0aa6d29a91b778130aaeb925a7504c9a67d6b7f28c1efd064b61f1077b71463b', secret='d3cc55242b9811642ae45701662e038442cfc248aacc171c3855529522c4aec9',base_url="https://testnet.binancefuture.com")
params = {
    'symbol': 'BTCUSDT',
    'origClientOrderId': "ALGOINTERN_OID1"
    }
print(client.query_order(**params))
entryPrice = client.query_order(**params)['avgPrice']
i = 1
ID = "ALGOINTERN_SL_OID{id}".format(id = i+1)
print("***********************************")
print(ID)
print("***********************************")
params = {
'symbol': 'BTCUSDT',
'side': 'SELL',
'type': 'STOP',
'quantity': 0.001,
'price': float(entryPrice),
'stopPrice': math.ceil(0.995*float(entryPrice)),
# 'callbackRate':0.5,
'newClientOrderId': ID,
'timestamp': time,
# 'closePosition': True,
'timeInForce': 'GTC',
'X-MBX-APIKEY': '0aa6d29a91b778130aaeb925a7504c9a67d6b7f28c1efd064b61f1077b71463b'
}
response = client.depth(**params)
print(response)
response = client.new_order(**params)
print(response)
# for i in range(0,3):
#     ID = "ALGOINTERN_SL_OID{id}".format(id = i+1)
#     print("***********************************")
#     print(ID)
#     print("***********************************")
#     params = {
#     'symbol': 'BTCUSDT',
#     'side': 'SELL',
#     'type': 'TRAILING_STOP_MARKET',
#     'quantity': 0.01,
#     # 'price': int(mark_price),
#     # 'stopPrice': round(mark_price,2),
#     'callbackRate':0.5,
#     'newClientOrderId': ID,
#     'timestamp': time,
#     'reduceOnly': True,
#     'timeInForce': 'GTC',
#     'X-MBX-APIKEY': '0aa6d29a91b778130aaeb925a7504c9a67d6b7f28c1efd064b61f1077b71463b'
#     }
#     response = client.depth(**params)
#     print(response)
#     response = client.new_order(**params)
#     print(response)