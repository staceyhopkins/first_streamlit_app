import streamlit
import pandas as pd

streamlit.title("Stacey's diner")
streamlit.header('Breakfast Faves')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruit_csv = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_csv = fruit_csv.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(fruit_csv.index)['Grapes','Banana'])
streamlit.dataframe(fruit_csv)
