import streamlit as st
import currencies
from convertor import get_exchange_rate, convert_currency

st.title(":dollar: Currency Converter")
st.markdown("""This tool allows you to convert currencies using real-time exchange rates.""")
src_currency = st.selectbox("Source Currency (base)", currencies.MONEY_FORMATS.keys())
dst_currency = st.selectbox("Destination Currency (target)", currencies.MONEY_FORMATS.keys())
amount = st.number_input("Amount", min_value=1)

if st.button("Convert"):
    exchange_rate = get_exchange_rate(src_currency, dst_currency)
    result = convert_currency(amount, exchange_rate)
    if result:
        st.success(f"{amount} {src_currency} = {result} {dst_currency}")
    else:
        st.error("Conversion failed.")

st.markdown("---")
st.markdown("""
### About
This is a real-time currency converter application built with Streamlit which is able to:
- Fetch live exchange rates
- Convert between multiple currencies
- Provide a user-friendly interface
""")

st.markdown("Made with ❤️ by [themohammadreza](https://github.com/themohammadreza)")