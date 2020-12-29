#importing libraries
from flask import Flask ,render_template,url_for,request,flash,redirect
import pickle
import pandas as pd
import sklearn
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key="."
y_label=None

Type={'rice': 0, 'wheat': 1, 'Mung Bean': 2, 'Tea': 3, 'millet': 4, 'maize': 5, 'Lentil': 6,\
     'Jute': 7, 'Coffee': 8, 'Cotton': 9, 'Ground Nut': 10, 'Peas': 11, 'Rubber': 12, \
         'Sugarcane': 13, 'Tobacco': 14, 'Kidney Beans': 15, 'Moth Beans': 16,\
             'Coconut': 17, 'Black gram': 18, 'Adzuki Beans': 19, 'Pigeon Peas': 20,\
                  'Chickpea': 21, 'banana': 22, 'grapes': 23, 'apple': 24, 'mango': 25,\
                       'muskmelon': 26, 'orange': 27, 'papaya': 28, 'pomegranate': 29, 'watermelon': 30}
Crop={v:k for k,v in Type.items()} 

# Loading the model and scaler using pickle
model=pickle.load(open('./static/CropPredictsvm.pkl', 'rb'))
scaler=pickle.load(open('./static/CropScaler.pkl', 'rb'))

# HAndling the requests made to root page   
@app.route("/",methods=["GET","POST"])


def index():
    if request.method=="POST":
        temperature=request.form['temperature']
        humidity=request.form['humidity']
        ph=request.form['ph']
        rainfall=request.form['rainfall']
        data={'temperature':[temperature],'humidity':[humidity],'ph':[ph],'rainfall':[rainfall],}
        df=pd.DataFrame(data=data)
        scaled_data=scaler.transform(df)
        y_label=model.predict(scaled_data)
        prediction=Crop[y_label[0]].upper()
        
        return render_template("prediction.html",\
            temperature=temperature,humidity=humidity,ph=ph,rainfall=rainfall,prediction=prediction)
        

    return render_template("index.html")


if __name__=="__main__":
    app.run(threaded=True,port=5000) 