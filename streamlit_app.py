import streamlit
import pandas
streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3')
streamlit.text('🥑🍞Avocado toast')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") "dataframe"
streamlit.dataframe(my_fruit_list)
