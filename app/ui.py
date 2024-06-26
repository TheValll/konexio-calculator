# Description: Streamlit app to calculate the distance between a company and its students.

# Importing the required libraries.
import streamlit as st
import pandas as pd
from set_data import set_data

# Function to set the page configuration.
def main():
    st.set_page_config(
        page_title="Entreprise Distance Calculateur", 
        layout="wide", 
        initial_sidebar_state="auto",
    )

# Main function to run the app.
if __name__ == "__main__":
    main()

# Hiding the Streamlit menu and footer.
padding_top = 0
hide_streamlit_style = f"""
<style>
#MainMenu {{visibility: hidden;}}
.appview-container .main .block-container{{padding-top: {padding_top}rem;}}
footer {{visibility: hidden;}}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Create 2 input fields for the user to upload a file and enter the company address.
uploaded_files = st.file_uploader("Choose a XLSX file", accept_multiple_files=False, type=['xlsx'])
entreprise_adresses = st.text_input("Entrez l'adresse de l'entreprise", placeholder="Exemple : 42 rue de la paix, 75002 Paris")

# Create a button to calculate the distance between the company and its students.
if st.button('Calculer la distance'):
    if uploaded_files:
        if entreprise_adresses:
            data = set_data(uploaded_files, entreprise_adresses)
        else:
            st.write("Veuillez entrer l'adresse de l'entreprise.")

        # Create a DataFrame to display the data.
        if data["nom"] and data["prenom"] and data["distances_voiture_list"] and data["temps_voiture_list"] and data["temps_velo_list"] and data["distances_velo_list"] and data["distances_transport_list"] and data["temps_transport_list"]:
            df = pd.DataFrame({
                'Nom': data["nom"],
                'Prénom': data["prenom"],
                'Distance transport': data["distances_transport_list"],
                'Temps transport': data["temps_transport_list"],
                'Distance voiture': data["distances_voiture_list"],
                'Temps voiture': data["temps_voiture_list"],
                'Distance vélo': data["distances_velo_list"],
                'Temps vélo': data["temps_velo_list"],
            })
            st.write(df)
        else:
            st.write("Aucune donnée trouvée ou une erreur s'est produite.")
    else:
        st.write("Aucun fichier téléchargé.")