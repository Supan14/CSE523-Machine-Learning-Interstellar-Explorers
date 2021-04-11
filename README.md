## Exoplanet Classification using Machine Learning Algorithms

[You can visit the live webiste here!](http://interstellar-explorers-app.herokuapp.com/)

[Here is the youtube link of a working site!](https://www.youtube.com/watch?v=mEqn2KPAOjg)

### Team Interstellar Explorer's project for CSE523 Machine Learning Course

#### Team members: Supan Shah, Rudri Jani, Riya Shah, Dhaval Deshkar

### Let's get started how this project is built!

The project trying to identify whether the given planet is livable planet or not using classification algorithms. 

#### How the data is coming around???

### Collecting Data:
The data is collected from NASA's [live API](https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html).

The calling of API can be found from the code.

The final dataset on which the model is being trained can be found in the ```/Dataset``` folder.

#### Now let's explore what's happening in the code.

### About The Code:

The public URL of the code can be found [here](https://colab.research.google.com/drive/182VPMbN5D1EqTFl1pVQuHR91KJ6MsP3t?usp=sharing)

First the data is extracted using NASA's API. After some EDA and data cleaning and preprocessing, the feature selection is done. Using those features three classification models are implemented. Logistic Regression, Support Vector Machine and XGBoost is used to classify whether the planet is an exoplanet or not. 



#### Now let's test the model.  

The trained model is deployed on the IBM cloud. It returns the probability of a planet being an exoplanet. 


#### Deployment on Heroku

The whole project is deployed on heroku. So it is live and anyone can test it by setting the different inputs.


