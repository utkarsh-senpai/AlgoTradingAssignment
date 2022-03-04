from binance.futures import Futures 

client = Futures()
time = client.time()['serverTime']
print(client.time())
print(time)

client = Futures(key='0aa6d29a91b778130aaeb925a7504c9a67d6b7f28c1efd064b61f1077b71463b', secret='d3cc55242b9811642ae45701662e038442cfc248aacc171c3855529522c4aec9',base_url="https://testnet.binancefuture.com")

# Get account information
print("***********************************")
print("Account Details")
print("***********************************")
print(client.account())

# Post a new order
i = 1
ID = "ALGOINTERN_OID{id}".format(id = i+1)
print("***********************************")
print(ID)
print("***********************************")
params = {
    'symbol': 'BTCUSDT',
    'side': 'BUY',
    'type': 'MARKET',
    'quantity': 0.001,
    'newClientOrderId': ID,
    'timestamp': time,
    'X-MBX-APIKEY': '0aa6d29a91b778130aaeb925a7504c9a67d6b7f28c1efd064b61f1077b71463b'
}
response = client.depth(**params)
print(response)
response = client.new_order(**params)
print(response)