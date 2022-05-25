#importing libraries
from flask import Flask ,render_template,url_for,request,flash,redirect
import pickle
import pandas as pd
import sklearn
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key="."
y_label=None


# Loading the model and scaler using pickle
model=pickle.load(open('./static/knn.pickle', 'rb'))

# HAndling the requests made to root page   
@app.route("/",methods=["GET","POST"])


def index():
    if request.method=="POST":
        petal_length=request.form['petal_length']
        petal_width=request.form['petal_width']
        sepal_length=request.form['sepal_length']
        sepal_width=request.form['sepal_width']
       
        data={'PetalLengthCm':[petal_length],'PetalWidthCm':[petal_width],'SepalLengthCm':[sepal_length],'SepalWidthCm':[sepal_width]}
        df=pd.DataFrame(data=data)
        y_label=model.predict(df)
        prediction=y_label[0].upper()
        
        return render_template("prediction.html",\
            petal_length=petal_length,petal_width=petal_width,sepal_length=sepal_length,sepal_width=sepal_width,prediction=prediction)
        

    return render_template("index.html")


if __name__=="__main__":
    app.run(threaded=True,port=5000) 