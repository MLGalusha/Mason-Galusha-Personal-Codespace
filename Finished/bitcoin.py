import sys  # Import the 'sys' module for interacting with the Python interpreter
import requests  # Import the 'requests' module for making HTTP requests

# Check if the correct number of command-line arguments is provided
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])  # Attempt to convert the command-line argument to a float
    except:
        print("Command-line argument is not a number")  # Print an error message if the conversion fails
        sys.exit(1)  # Exit the script with an error code
else:
    print("Missing command-line argument")  # Print an error message if the expected command-line argument is missing
    sys.exit(1)  # Exit the script with an error code

try:
    # Make a request to the Coindesk API to get the current Bitcoin price in USD
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()  # Parse the JSON response
    bitcoin = response["bpi"]["USD"]["rate_float"]  # Extract the Bitcoin price from the response
    total_amount = bitcoin * value  # Calculate the total value in USD based on the provided value in Bitcoin
    print(f"${total_amount:,.4f}")  # Print the total amount in USD with formatting
except requests.RequestException:
    print("Request Exception")  # Print an error message if there is an exception during the HTTP request
    sys.exit(1)  # Exit the script with an error code
