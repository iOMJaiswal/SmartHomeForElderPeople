# Smart Home For Elder People - Machine Learning Project

## Overview

The **Smart Home For Elder People** project is a machine learning-based system designed to identify usual and unusual activities of the aging population. The objective of this project is to provide supervision, reduce death rates, and offer a user-friendly system to support the independent living of elderly individuals. The aging population faces challenges, including physical limitations, memory loss, safety concerns, and social isolation. This smart home solution aims to address these issues and improve the quality of life for older adults.

## Features

- **GUI Framework**: The project utilizes Django and Bootstrap for creating an interactive and responsive graphical user interface.

- **Languages**: The implementation is done using Python, HTML/CSS, and Javascript, ensuring a robust and versatile development environment.

- **Implemented Libraries**: Pandas and Sklearn libraries are used to process and analyze the data, enabling efficient machine learning capabilities.

## Project Details

### Objective

The primary goals of the Smart Home For Elder People project are:
- **Supervision**: To provide continuous monitoring and support for elderly individuals in their homes.
- **Reduce Death Rate**: To minimize accidents and incidents that could potentially lead to fatalities.
- **User-Friendly System**: To create an intuitive and easy-to-use system that caters to the needs of older adults.

### Algorithm & Performance

The classification of activities as usual or unusual is achieved using the **Random Forest Algorithm**. The model demonstrates a remarkable accuracy of **96%**, indicating its overall correctness in predicting activity types.

### System Flow

The system's workflow can be summarized as follows:
1. **Input Features**: Data includes location, time of day, object posture, duration, and activity details.
2. **Data Preprocessing**: Data is processed and encoded using one-hot encoding to convert it into numerical format, making it suitable for machine learning.
3. **Training**: The Random Forest classifier is trained using the processed data.
4. **User Input**: User input is taken, encoded, and processed to predict the activity as usual or unusual.
5. **Prediction**: The trained classifier predicts the activity's nature based on the user's input.
6. **Result Display**: The result, whether the activity is usual or unusual, is displayed to the user.

### Conclusion

The Smart Home For Elder People project aims to create a secure, affordable, and user-friendly smart home solution for older adults. By effectively classifying activities as usual or unusual, the system enhances the independence and quality of life for elderly individuals. With a high accuracy rate of 96%, the proposed classification system demonstrates promising results in predictive analytics.

**Note**: The project is open to improvements and enhancements to optimize the model's performance and expand its capabilities to real-world scenarios.

## Installation and Usage

1. Clone the repository:

```bash
git clone https://github.com/iOMJaiswal/SmartHomeForElderPeople.git
```

2. Change into the project directory:

```bash
cd SmartHomeForElderPeople
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Access the web-app locally:

Open your web browser and go to `http://localhost:8000/`


---

Thank you for your interest in the Smart Home For Elder People project! We look forward to making a positive impact on the lives of older adults through this innovative machine learning-based solution. If you have any questions or feedback, feel free to reach out. Happy coding and empowering the elderly community! 
