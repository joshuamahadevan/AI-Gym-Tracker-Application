
from flask import *
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


app = Flask(__name__)

counter = 0
stage = None
set_count = 0

@app.route('/')
def home():
      return render_template('index.html')

@app.route('/gym_tracker')
def gym_tracker():
    return render_template('gym_tracker.html')    
      
@app.route('/nutrition_suggestion')
def nutrition_suggestion():
    return render_template('nutrition_suggestion.html')

@app.route( '/exercise_data', methods=['POST'] )
def exercise_data():
    print( request.json['time'])
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/calculate', methods=['GET','POST'])
def calculate_bmi():
    bmi=None
    result = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        
        bmi = weight / (height/100)**2
        
        if bmi < 18.5:
            result = "Underweight"
        elif bmi >= 18.5 and bmi < 24.9:
            result = "Normal weight"
        elif bmi >= 25.0 and bmi < 30.0:
            result = "Overweight"
        else:
            result = "Obese"
        
        # return render_template('result.html', bmi=bmi, result=result)
    
    return render_template('nutrition_suggestion.html',bmi=bmi,result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

