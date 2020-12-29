# crop-recommender-deploy
## Deploying ML app using flask
### Deployed at https://ml-crop-recommender.herokuapp.com/
### This is a deployment of model trained view at https://github.com/czyum/Multiclass_Classification-Crop-Dataset

## How to use?

### 1)Download or pull the repository (including venv)
### 2)Make sure you have python installed.You can install it at https://www.python.org/downloads
### 3)In the command prompt do the following:
#### -->Change the path the folder containing all the files
#### -->Change the path once again to venv example:cd venv
#### -->Enter the command <b>Scripts\activate</b>.This starts the virtual environment
#### -->Change the path once again nack to root directory <b>cd ../</b>
#### -->Start the server using <b>python app.py</b>.Your website will be running on port <b>5000</b>

## You can use the same code as a boilerplate to deploy other ML models

### Just serialize your model using pickle or joblib which you can use as a persistent model and load it in the deployment server

## How to deploy this on to heroku ? 
#### view all the steps at https://stackabuse.com/deploying-a-flask-application-to-heroku
