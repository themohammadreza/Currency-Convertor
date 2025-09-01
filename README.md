# Currency Converter

<img src="assets/picture.png" alt="Currency Converter" width="400"/>

## Project Description

This is a simple, real-time currency converter application built using Streamlit. It fetches live exchange rates from the ExchangeRate-API and allows users to convert amounts between various currencies through a user-friendly web interface. The application caches exchange rates for efficiency (with a 3-hour TTL) and supports a predefined list of currencies via the `currencies` library.

## Table of Contents

- [Project Description](#project-description)
- [Project Tree Structure](#project-tree-structure)
- [Features](#features)
- [Requirements](#requirements)
- [How to Install](#how-to-install)
- [How to Clone and Use the Project](#how-to-clone-and-use-the-project)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Project Tree Structure

```
Currency-Convertor/
├── assets
│   └── picture.png
├── LICENSE
├── README.md
└── src
    ├── convertor.py        # Core module for fetching exchange rates and performing conversions
    ├── dashboard.py        # Streamlit dashboard for the user interface
    ├── requirements.txt    # List of dependencies
```

## Features

- **Real-Time Exchange Rates**: Fetches live rates from [ExchangeRate-API](https://www.exchangerate-api.com/) with caching to reduce API calls (cached for 3 hours using `cachetools`).
- **Currency Conversion**: Converts amounts from a source currency to a destination currency using the fetched rates.
- **User-Friendly Interface**: Built with Streamlit, featuring dropdowns for currency selection, a number input for amounts, and a conversion button that displays results or errors.
- **Supported Currencies**: Uses a predefined list from the `currencies` library (e.g., USD, EUR, etc., based on `MONEY_FORMATS.keys()`).
- **Error Handling**: Displays success messages for conversions and error messages if the conversion fails (e.g., due to API issues).

## Requirements

The project requires Python 3.9+ and the following dependencies (as specified in `requirements.txt`):

- `streamlit==1.28.2`: For building the web interface.
- `currencies==2020.12.12`: For handling currency formats and lists.
- `cachetools==5.3.2`: For caching exchange rate data.
- `requests==2.32.5`: For making HTTP requests to the API.

## How to Install

1. Ensure you have Python installed (version 3.12 or compatible).
2. Install the dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## How to Clone and Use the Project

1. Clone the repository:

   ```
   git clone https://github.com/themohammadreza/Currency-Convertor.git
   cd Currency-Convertor
   ```

2. Install the requirements as described above.

3. Run the Streamlit application:

   ```
   streamlit run src/dashboard.py
   ```

   This will launch a local web server (typically at `http://localhost:8501`). Open it in your browser to use the converter.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push to your fork and submit a pull request.

Please ensure your code follows Python best practices, and add tests if applicable. For major changes, open an issue first to discuss.

## Author

Mohammadreza Naseri  
GitHub: [themohammadreza](https://github.com/themohammadreza)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.