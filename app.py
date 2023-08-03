import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the pre-trained model using pickle
model = joblib.load('lmodel_filename.joblib')

@app.route('/', methods=['GET', 'POST'])
def loan_prediction():
    if request.method == 'POST':
        gender = request.form['Gender']
        martial = request.form['Martial']
        dependents = request.form['dependent']
        education = request.form['education']
        employed = request.form['selfEmployed']
        applicant_income = int(request.form['aincome'])
        coapplicant_income = float(request.form['caincome'])
        loan_amount = float(request.form['loanamount'])
        loan_term = float(request.form['loanterm'])
        credit_history = request.form['creditHistory']
        property_area = request.form['propertyArea']


        g={'Female':0,'Male':1}
        gender=g[gender]
        m={'No':0,'Yes':1}
        martial=m[martial]
        d={'0':0,'1':1,'2':2,'3+':3}
        dependents=d[dependents]
        e={'graduate':0,'notGraduate':1}
        education=e[education]
        se={'No':0,'Yes':1}
        employed=se[employed]
        c={'No':0.0,'Yes':1.0}
        credit_history=c[credit_history]
        pa={'semiurban':1,'urban':2,'rural':0 }
        property_area=pa[property_area]
        
        # Predict the loan status using the loaded model
        loan_status =model.predict([[gender, martial,dependents, education, employed, applicant_income,
                    coapplicant_income, loan_amount, loan_term, credit_history, property_area]])
        loan_status=int(loan_status[0])

        if loan_status == 1:
            loan_result_message = "Loan approved."
        else:
            loan_result_message = "Loan Not Approved."

        return render_template('r.html', loan_result_message=loan_result_message)

    return render_template('h.html')


if __name__ == '__main__':
    app.run(debug=True)


