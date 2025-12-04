# Student Placement Prediction

A machine learning-based web application that predicts whether a student will be placed or not based on their academic performance, skills, and extracurricular activities.

## Overview

This project uses a trained machine learning model to predict student placement outcomes. The prediction is based on various factors including CGPA, academic achievements, projects, certifications, internships, and communication skills. The application provides an intuitive web interface for users to input student data and receive placement predictions.

## Features

- **User-Friendly Web Interface**: Simple and responsive form for entering student data
- **Real-Time Predictions**: Instant placement prediction based on input parameters
- **Multiple Input Factors**: Considers 11 different factors for accurate predictions
- **Visual Feedback**: Color-coded results (green for placed, red for not placed)

## Input Parameters

The model uses the following features to make predictions:

1. **CGPA** - Cumulative Grade Point Average (decimal value)
2. **Major Projects** - Number of major projects completed
3. **Workshops/Certifications** - Number of workshops or certifications attended
4. **Mini Projects** - Number of mini projects completed
5. **Skills** - Number of technical skills possessed
6. **Communication Skill Rating** - Communication skill rating (decimal value)
7. **Internship** - Whether the student has done an internship (0 = No, 1 = Yes)
8. **Hackathon** - Participation in hackathons (0 = No, 1 = Yes)
9. **12th Percentage** - Percentage scored in 12th grade
10. **10th Percentage** - Percentage scored in 10th grade
11. **Backlogs** - Number of academic backlogs

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: Pickle (model serialization)
- **Data Processing**: Pandas
- **Frontend**: HTML5, CSS3
- **Deployment**: Python 3.x

## Project Structure

```
studentml/
├── app.py                          # Main Flask application
├── templates/
│   ├── index.html                  # Input form page
│   └── result.html                 # Prediction result page
├── studentplacement (2).pkl        # Trained ML model
└── README.md                       # This file
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd studentml
   ```

2. **Install required dependencies**:
   ```bash
   pip install flask pandas
   ```

3. **Ensure the model file is present**:
   - The application requires `studentplacement (2).pkl` in the project root directory

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Fill in the student details** in the form with the following information:
   - Academic scores (10th, 12th percentage, CGPA)
   - Number of projects and certifications
   - Communication skill rating
   - Internship and hackathon participation status
   - Number of backlogs

4. **Click "Predict"** to receive the placement prediction

5. **View the result** on the results page showing whether the student is likely to be placed or not

## How It Works

1. The user fills in student academic and activity information through the web form
2. Form data is processed and organized according to the model's feature order
3. A pandas DataFrame is created with the input features
4. The pre-trained machine learning model makes a prediction (1 = Placed, 0 = Not Placed)
5. The result is displayed with visual feedback on the results page

## Model Information

- **Model Type**: Classification model (Binary classification: Placed or Not Placed)
- **Model File**: `studentplacement (2).pkl`
- **Features**: 11 input features as listed above
- **Output**: Binary prediction (1 = Placed, 0 = Not Placed)

## Future Enhancements

- Add model accuracy metrics and confidence scores
- Implement data validation and error handling
- Add database functionality to store predictions
- Create an admin dashboard for model management
- Add feature importance visualization
- Implement API endpoints for programmatic access

## License

This project is part of the student placement prediction system.

## Author

Christoputhanpurackal

## Support

For issues or questions, please refer to the repository or contact the project maintainers.
