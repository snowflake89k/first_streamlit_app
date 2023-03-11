import streamlit
import pandas
import snowflake.connector

streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3')
streamlit.text('🥑🍞Avocado toast')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 

# code a drop-down list
my_fruit_list = my_fruit_list.set_index('Fruit') 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#streamlit.dataframe(my_fruit_list)
#streamlit.dataframe(fruits_selected)
streamlit.dataframe(fruits_to_show)

# new section to display fruityvice api response
streamlit.header('Fruityvice fruit advice!')


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")


fruit_choice = streamlit.text_input('What fruit would you like information about')
streamlit.write('The user entered', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruitvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruitvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

my_cur.execute("Select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

