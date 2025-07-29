markdown
# Global Ethereum Price Index - GEX

## Overview

The Global Ethereum Price Index (GEX) is an advanced mcp server that provides comprehensive and up-to-date Ethereum price data. Powered by a reliable price index, GEX ensures accuracy and consistency in delivering Ethereum pricing information. This service is designed to cater to various needs, from financial reporting and analysis to integration with diverse software applications.

## Key Features

- **Up to 1-second Refresh Rate:** Enjoy real-time Ethereum price updates, ensuring you always have the latest information at your fingertips.
- **Support for 165+ Currencies:** Access Ethereum prices in over 165 currencies, providing flexibility for users worldwide.
- **Daily and Live Rates:** Choose between daily rates at a preferred lock-in time or real-time live rates to suit your requirements.
- **Historical Data:** Access historical daily rates dating back to 2010, perfect for trend analysis and historical comparison.
- **Flexible Formats:** Retrieve data in JSON or CSV formats, allowing easy integration and analysis.

## Available Tools

GEX offers a suite of powerful tools designed to provide detailed Ethereum pricing data:

### Custom Ticker
- **Description:** Generate a custom index in a specific currency. You can choose to include or exclude specific exchanges as needed.
- **Parameters:** 
  - `exchanges` (optional): Comma-separated list of exchanges to include or exclude.

### Ticker Per Symbol
- **Description:** Retrieve ticker data for a specified symbol.
- **Parameters:**
  - `market`: Specifies the market type (global or local).
  - `symbol`: The Ethereum symbol paired with a valid ISO currency (e.g., ETHUSD, ETHEUR).

### Short Ticker
- **Description:** Access basic ticker information including the last and daily average price for all symbols.
- **Parameters:**
  - `crypto` (optional): Valid value is ETH.
  - `fiats` (optional): Specify fiat currencies to filter the ticker data (e.g., ETHUSD, ETHEUR).

### Ticker Changes
- **Description:** Obtain ticker values and price changes for a specified market and symbol.
- **Parameters:**
  - `market`: Specifies the market type (global or local).
  - `symbol`: The Ethereum symbol paired with a valid ISO currency (e.g., ETHUSD).

### All Ticker Data
- **Description:** Retrieve ticker data for every supported symbol. Specify fiat currencies to narrow down the results.
- **Parameters:**
  - `crypto` (optional): Valid value is ETH.
  - `fiat` (optional): Comma-separated list of ISO currency codes (e.g., USD, EUR).

## Conclusion

The Global Ethereum Price Index (GEX) is a robust and versatile mcp server, providing both real-time and historical Ethereum price data across a wide range of currencies. With its powerful tools and flexible data formats, GEX is ideal for users seeking reliable and comprehensive Ethereum pricing information for various applications.