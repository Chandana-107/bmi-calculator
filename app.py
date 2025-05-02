from flask import Flask, render_template, request

app = Flask(__name__)

# Function to get health tip and CSS class based on BMI
def get_health_tip(bmi):
    if bmi < 18.5:
        return "You're underweight. Try to eat more balanced meals and gain some weight.", "underweight"
    elif 18.5 <= bmi < 25:
        return "You're in a healthy weight range. Keep up the good work!", "normal"
    elif 25 <= bmi < 30:
        return "You're slightly overweight. Incorporate more exercise and consider a balanced diet.", "overweight"
    else:
        return "You're in the obese range. It's important to speak with a healthcare provider for guidance.", "obese"

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    tip = None
    tip_class = None
    if request.method == "POST":
        # Get height (in cm) and weight (in kg) from the form
        height = float(request.form["height"]) / 100  # convert cm to meters
        weight = float(request.form["weight"])
        
        # Calculate BMI
        bmi = round(weight / (height ** 2), 2)
        
        # Get the health tip and CSS class based on BMI
        tip, tip_class = get_health_tip(bmi)
    
    return render_template("index.html", bmi=bmi, tip=tip, tip_class=tip_class)

if __name__ == "__main__":
    app.run(debug=True)
