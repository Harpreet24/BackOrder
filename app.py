#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
from flask import request,Flask,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('BackOrder.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
     if request.method == 'POST':
        national_inv = int(request.form['national_inv'])
        lead_time = int(request.form['lead_time'])
        in_transit_qty = int(request.form['in_transit_qty'])
        min_bank = int(request.form['min_bank'])
        local_bo_qty = int(request.form['local_bo_qty'])
        data = np.array([[national_inv,lead_time,in_transit_qty,min_bank,local_bo_qty]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

#@app.route("/predict_api",methods=['POST'])
#def predict_api():
 #   data = request.get_json(force=True)
 #   prediction = model.predict([np.array(list(data.values()))])
 

 #   output=prediction[0]
  #  return jsonify(output)



if __name__ == "__main__":
    app.run(port = 5000,debug=True)
