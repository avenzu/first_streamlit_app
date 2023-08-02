import streamlit
import pandas

streamlit.title("My Girlfriend's new Health Diner")
streamlit.header('Breakfastreamlit Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_listreamlit = pandas.read_csv("https://uni-lab-files.s3.us-westreamlit-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_listreamlit)
