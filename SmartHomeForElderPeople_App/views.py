from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        location = request.POST['location']
        time = request.POST['time']
        object = request.POST['object']
        posture = request.POST['posture']
        duration = request.POST['duration']
        activity = request.POST['activity']

        result = getResult(location, time, object, posture, duration, activity)

        if result == "Unusual":
            messages.error(request, "Dont Worry!!! All Good !") 
            return redirect('/index')
        else:
            messages.success(request, "Dont Worry!!! All Good !") 
            return redirect('/index')

    else:
        return render(request, 'index.html')
    
    
def getResult(location, time_of_day, object_name, posture, duration, activity):
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier

    # Load the dataset
    dataset = pd.read_csv("static/csv/updated_smart_home_dataset.csv")

    # Drop rows with missing values
    dataset = dataset.dropna()

    # Split the dataset into features (X) and target variable (y)
    X = dataset.drop("Result", axis=1)
    y = dataset["Result"]

    # Convert categorical variables into numerical using one-hot encoding
    X_encoded = pd.get_dummies(X)

    # Train the Random Forest classifier
    classifier = RandomForestClassifier(random_state=42)
    classifier.fit(X_encoded, y)


    # Create a dataframe from user input
    user_input = pd.DataFrame([[location, time_of_day, object_name, posture, duration, activity]], 
                            columns=X.columns)

    # Encode user input using one-hot encoding
    user_encoded = pd.get_dummies(user_input)

    # Realign the columns to match the training data
    user_encoded = user_encoded.reindex(columns=X_encoded.columns, fill_value=0)

    # Make predictions
    prediction = classifier.predict(user_encoded)

    # Map the predicted class to "Usual" or "Unusual"
    output = "Usual" if prediction[0] == "Usual" else "Unusual"

    # Display the output
    print("Output:", output)

    return(output)