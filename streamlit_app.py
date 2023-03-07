import streamlit
import pandas
streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3')
streamlit.text('🥑🍞Avocado toast')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list = my_fruit_list.set_index('Fruit') 

# code a drop-down list
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
