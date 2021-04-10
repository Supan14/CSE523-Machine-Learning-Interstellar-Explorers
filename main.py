import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import json
from ibm_watson_machine_learning import APIClient

def main():
	df = load_data()
	st.title('Interstellar Explorers')
	st.markdown("## Team: *Supan Shah, Rudri Jani, Riya Shah, Dhaval Deshkar*")
	st.markdown('##')
	st.text('You can view the data to look at some values that you might like to test. The final column will show if that row is of an exoplanet or not. 1 => exoplanet and 0 => Not exoplanet ')
	
	load_check = st.checkbox('View Data', value=False)
	if load_check:
		st.dataframe(df)

	st.text('Feel free to look at the decision tree by clicking below')
	feature_choice = st.checkbox('Show Decision Tree Logic', value=False)
	if feature_choice:
		image = Image.open('xgboost.png')
		st.image(image, caption='XGBoost Decision Tree Diagram',use_column_width=True)

	st.title('Random prediction from dataset')
	random_pred  = st.button('Get a random prediction')
	if random_pred:
		get_random_prediction()
	
	st.title('Custom Prediction')
	st.text('Enter custom values below or predict from any row from the dataset to test our model')
	Disposition_Score = st.slider('Disposition Score',
					  min_value=0.0,
					  max_value=1.0 ,
					  value=0.5,
					  step=0.01)

	Planet_Radius =  st.number_input('Planet Radius', value=17.56) 

	TCE_Planet_Number = st.slider('TCE Planet number',
					  min_value=1,
					  max_value=6,
					  value=1,
					  step=1)


	Stellar_Effective_Temperature =  st.number_input('Stellar Effective Temperature', value=112.7) 

	Transit_Signal_to_Noise = st.number_input('Transit Signal to Noise', value=42.5)

	
	do_prediction = st.button('Predict')

	if do_prediction:
		inp_data = [Disposition_Score, Planet_Radius,
					TCE_Planet_Number, Stellar_Effective_Temperature,
					Transit_Signal_to_Noise]
		exoplanet_probability = Prediction(inp_data)
		exoplanet_probability_rounded = np.round(exoplanet_probability, 3)
		st.text(f"There is {exoplanet_probability_rounded * 100} % chance of given planet being an exoplanet.")

@st.cache
def load_data():
	return pd.read_csv('./Dataset/full_data.csv')

@st.cache
def Prediction(x):
	with open('apikey.json') as handle:
		API_KEY = json.load(handle)['apikey']

	location = "eu-gb"

	wml_credentials = {
		"apikey": API_KEY,
		"url": 'https://' + location + '.ml.cloud.ibm.com'
	}

	client = APIClient(wml_credentials)
	client.set.default_space("0c2b26ba-067f-44a9-8041-94e1fb366bdc")
	scoring_payload = {"input_data": [{"values": [list(x)]}]}
	
	predictions = client.deployments.score("f4a9c694-eb4e-400c-9cf0-79ab027cc102", scoring_payload)
	exoplanet_probability = np.round(predictions['predictions'][0]['values'][0][0], 3)
	return exoplanet_probability  

def get_random_prediction():
	df = load_data()
	sample = df.sample(1)
	st.dataframe(sample)
	sample_x = sample.iloc[0,:-1]
	sample_y = sample.iloc[0,-1]

	st.text("Model Prediction:")
	exoplanet_probability = Prediction(sample_x)
	exoplanet_probability_rounded = np.round(exoplanet_probability, 3)
	st.text(f"There is {exoplanet_probability_rounded * 100} % chance of given planet being an exoplanet.")
	st.text("Reality:")
	if sample_y == 1:
		st.text('The planet is an exoplanet.')
	else:
		st.text('The planet is NOT an exoplanet.')

if __name__ == '__main__':
	main()