import streamlit as st
from scraper import scrape_data
import pandas as pd

st.set_page_config(page_title="Web Scraper", page_icon=":mag:", layout="wide")

df = pd.DataFrame()  # Initialize empty DataFrame globally

def app():
  st.title("Khelmart Sports Product Scraper")
  # Set a background image
#   background_image = st.empty()
#   background_image.markdown("""
#   <style>
#     body {
#       background-image: url("C:/ShouvikDey/DSc_PW/Data_Collection/images/pngtree-colorful-sports-theme-background-material-image_944423.jpg");
#       background-repeat: no-repeat;
#       background-attachment: fixed;
#       background-position: center;
#       background-size: cover; /* Adjust background size as needed */
#       opacity: 0.8;  /* Adjust opacity between 0 (fully transparent) and 1 (fully opaque) */
#     }
#   </style>
#   """, unsafe_allow_html=True)

  # Add a title and input elements
  query = st.text_input('Enter your query:', key="query_input")  # Use key for reusability
  sort_option = st.selectbox('Sort by:', ['None', 'Discount %', 'Old Price', 'Special Price'], key="sort_select")

  # Scrape button and display results
  if st.button('Scrape', key="scrape_button"):
    df = scrape_data(query)
    if sort_option == 'Discount %':
      df.sort_values(by='Discount %', ascending=False, inplace=True)
    if sort_option == 'Old Price':
      df.sort_values(by='Old Price', ascending=False, inplace=True)
    if sort_option == 'Special Price':
      df.sort_values(by='Special Price', ascending=False, inplace=True)

    st.write(df, key="data_table")  # Use key for reusability

  # Download CSV button
  if st.button('Download CSV', key="download_button"):
    if not df.empty:
      csv_content = df.to_csv(index=False).encode('utf-8')
      st.write(csv_content, mimetype='text/csv', data=csv_content, download_name="scraped_data.csv")

if __name__ == '__main__':
  app()
