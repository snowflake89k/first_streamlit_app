import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3')
streamlit.text('🥑🍞Avocado toast')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 

# code a drop-down list
my_fruit_list = my_fruit_list.set_index('Fruit') 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# ----------------------------------------------------------------------------------------------------------------------#
# alternatives
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
#streamlit.dataframe(my_fruit_list)
#streamlit.dataframe(fruits_selected)
# ----------------------------------------------------------------------------------------------------------------------#

# new section to display fruityvice api response
streamlit.header('Fruityvice fruit advice!')

# import requests
# define a function:
def get_fruityvice_data (this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruitvice_normalized = pandas.json_normalize(fruityvice_response.json())
   #streamlit.dataframe(fruitvice_normalized)
    return fruitvice_normalized

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about')
    if not fruit_choice:
       streamlit.error("Please select a fruit to get more information")
    else:
        response_val = get_fruityvice_data (fruit_choice)
        streamlit.dataframe(response_val)
except URLError as e:
    streamlit.error()
    
# ----------------------------------------------------------------------------------------------------------------------#
# alternatives
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.write('The user entered', fruit_choice)
# ----------------------------------------------------------------------------------------------------------------------#

# import snowflake.connector
# snowflake related functions:
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("Select * from fruit_load_list")
         return my_cur.fetchall()

        
# Add button to load the fruit
if streamlit.button('Get Fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()  
   streamlit.dataframe(my_data_rows) 


#do not run anything beyond this line.
#streamlit.stop()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)


# Allow the end user to add fruit to the list

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('from streamlit')")
         return "Thanks for adding" + new_fruit
    
if streamlit.button('What fruit would you like to add'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(Kedu_fruit)  
   streamlit.dataframe(back_from_function) 
    
#add_my_fruit = streamlit.text_input('What fruit would you like to add')
#insert_row_snowflake(add_my_fruit)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

