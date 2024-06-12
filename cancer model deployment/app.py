# Import necessary libraries and packages 

from flask import Flask, render_template, request # Flask object
import pandas as pd
import joblib # package to load the model.pkl

# Instantiate Flask
app = Flask(__name__) 

# Map URL to function
@app.route("/")

# Index function mapping to index.html
def index():
    return render_template('/index.html')
    
# Map predict.html to predict function
@app.route('/predict', methods=['GET','POST'])

# Predict function receives user input as dictionary
# Calls another function to predict the student's output
# Sends the result user
def predict():
    
    if request.method == "POST":
        #Get input data
        to_predict_list = request.form.to_dict() 
        to_predict_list = {a: int(x) for a, x in to_predict_list.items()}

         # Open trained model
        scaler_file = open(r"C:\Users\msteel\OneDrive - Holland & Barrett\Documents\Python\cancer model deployment\scaler.pkl","rb")
    
        # Load trained model
        input_data = {k:[v] for k,v in to_predict_list.items()}  
        input_data = pd.DataFrame(input_data)

        scaler = joblib.load(scaler_file)
        input_data = scaler.transform(input_data)

        #Call preprocessDataAndPredict function and pass inputs
        try:
            prediction = preprocessDataAndPredict(input_data)

            #Pass prediction to prediction template
            return render_template('/predict.html', prediction = prediction)
   
        except ValueError:
            return "Please Enter valid values"
  
        pass
    pass

# preprocessDataAndPredict function recieves the input
# converts input to dataframe
# makes the prediction using trained model
# returns prediction results

def preprocessDataAndPredict(input_data):
    
    # Convert input to dataframe
    test_data = input_data
    print(test_data)
    
    # Open trained model
    file = open(r"C:\Users\msteel\OneDrive - Holland & Barrett\Documents\Python\cancer model deployment\model.pkl","rb")
    
    # Load trained model
    trained_model = joblib.load(file)
    
    # Get prediction results
    predict = trained_model.predict(test_data)
    print(predict)
    return predict
    
    pass
if __name__ == '__main__':
    app.run(debug=True)