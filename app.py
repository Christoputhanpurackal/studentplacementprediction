from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("D:\wistora\ml\studentplacement (2).pkl", "rb"))

# Model feature order
FEATURES = [
    "CGPA",
    "Major Projects",
    "Workshops/Certificatios",
    "Mini Projects",
    "Skills",
    "Communication Skill Rating",
    "Internship",
    "Hackathon",
    "12th Percentage",
    "10th Percentage",
    "backlogs",
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Read form data
        data = {
            "CGPA": float(request.form["CGPA"]),
            "Major Projects": int(request.form["MajorProjects"]),
            "Workshops/Certificatios": int(request.form["Workshops"]),
            "Mini Projects": int(request.form["MiniProjects"]),
            "Skills": int(request.form["Skills"]),
            "Communication Skill Rating": float(request.form["CommSkill"]),
            "Internship": int(request.form["Internship"]),
            "Hackathon": int(request.form["Hackathon"]),
            "12th Percentage": float(request.form["P12"]),
            "10th Percentage": float(request.form["P10"]),
            "backlogs": int(request.form["Backlogs"]),
        }

        df = pd.DataFrame([data])
        df = df[FEATURES]  # Ensure correct order

        prediction = model.predict(df)[0]
        return render_template("result.html", prediction=prediction)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
