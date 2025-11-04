import requests

def get_crypto_prices():
    # This is the CoinGecko API endpoint we'll use
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # We can tell the API exactly what we want.
    # Let's ask for Bitcoin and Ethereum prices in USD.
    params = {
        'ids': 'bitcoin,ethereum,solana',
        'vs_currencies': 'usd'
    }
    
    try:
        # Make the GET request to the API
        response = requests.get(url, params=params)
        
        # This line will raise an error if the request failed (e.g., 404, 500)
        response.raise_for_status() 
        
        # Convert the response text into a Python dictionary
        data = response.json()
        
        print("✅ Success! Here's the data we got from the API:")
        print(data)
        
        # Now we can access the prices easily
        btc_price = data['bitcoin']['usd']
        eth_price = data['ethereum']['usd']
        sol_price = data['solana']['usd']
        
        print(f"\n--- Simple Prices ---")
        print(f"Bitcoin: ${btc_price}")
        print(f"Ethereum: ${eth_price}")
        print(f"Solana: ${sol_price}")
        
    except requests.exceptions.RequestException as e:
        # Handle any errors during the request
        print(f"❌ Error fetching data: {e}")

# This makes the script run when you call it from the terminal
if __name__ == "__main__":
    get_crypto_prices()