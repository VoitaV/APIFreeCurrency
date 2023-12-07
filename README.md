# FreeCurrency API Program

This program uses the FreeCurrency API to convert a base currency into multiple other currencies. It utilizes the requests library to make HTTP requests and retrieve data from the API.

## Setup

To use this program, you will need to obtain an API key from FreeCurrency. Once you have your API key, replace CUR_KEY with your actual API key in the program.

CUR_KEY = 'your_api_key_here'

## Usage

The program allows you to input a base currency and then converts it into multiple other currencies. The available currencies for conversion are specified in the CURRENCIES list.

CURRENCIES = ['USD', 'CAD', 'EUR']

To run the program, simply execute the Python script. You will be prompted to input a base currency. Type q and press Enter to quit the program.

$ python freecurrency.py
Input the base currency (q for quit): USD
CAD, 1.25
EUR, 0.85
Input the base currency (q for quit): Q

If an invalid currency is entered, an error message will be displayed and you will be prompted to input another base currency.

## Functionality

The convert_currency function takes a base currency as input and retrieves conversion rates for that currency into multiple other currencies using the FreeCurrency API. It then prints out the converted values for each currency.

If an error occurs during the request or parsing of data, an error message is displayed and None is returned.

## Disclaimer

Please note that this program relies on an external API (FreeCurrency) and its availability and functionality are not guaranteed by this README or its authors. Any changes or issues with the FreeCurrency API may affect the functionality of this program.
