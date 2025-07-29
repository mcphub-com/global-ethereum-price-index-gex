import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/blockchain-data-ltd-blockchain-data-ltd-default/api/global-ethereum-price-index-gex'

mcp = FastMCP('global-ethereum-price-index-gex')

@mcp.tool()
def custom_ticker(exchanges: Annotated[Union[str, None], Field(description='Comma separated list of exchanges.')] = None) -> dict: 
    '''This endpoint can be used to generate a custom index in a certain currency. The “inex” path parameter represents “include” or “exclude”, you can choose to generate an index removing specified exchanges, or only including the few that you require.'''
    url = 'https://bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com/indices/ticker/custom/include/ETHUSD'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'exchanges': exchanges,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ticker_per_symbol(market: Annotated[str, Field(description='Possible values: global, local')],
                      symbol: Annotated[str, Field(description='ETH, where is valid ISO currency (ex. ETHUSD, ETHEUR)')]) -> dict: 
    '''Returns ticker data for specified symbol'''
    url = 'https://bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com/indices/global/ticker/ETHUSD'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'market': market,
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def short_ticker(crypto: Annotated[Union[str, None], Field(description='Valid value: ETH')] = None,
                 fiats: Annotated[Union[str, None], Field(description="If fiats parameter is included then only the values for those fiats will be returned (ETHUSD and ETHEUR in this example). If it's missing, then the response will contain ticker values of all available fiats for ETH.")] = None) -> dict: 
    '''Returns basic ticker denoting last and daily average price for all symbols'''
    url = 'https://bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com/indices/global/ticker/short'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'crypto': crypto,
        'fiats': fiats,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ticker_changes(market: Annotated[str, Field(description='Possible values: global, local')],
                   symbol: Annotated[str, Field(description='Possible values: ETH where is valid ISO currency (ex. ETHUSD)')]) -> dict: 
    '''Returns ticker values and price changes for specified market and symbol.'''
    url = 'https://bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com/indices/local/ticker/ETHUSD/changes'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'market': market,
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def all_ticker_data(crypto: Annotated[Union[str, None], Field(description='valid value: ETH')] = None,
                    fiat: Annotated[Union[str, None], Field(description='Comma separated list of ISO currency codes (ex. USD,EUR)')] = None) -> dict: 
    '''If no query parameters are sent, then returns ticker data for every supported symbol. If fiat(s) are sent as parameters, then only the ticker for those values is sent.'''
    url = 'https://bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com/indices/local/ticker/all'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'crypto': crypto,
        'fiat': fiat,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
