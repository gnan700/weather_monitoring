# Real-Time Data Processing System for Weather Monitoring

I developed the real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. 
The system will utilize data from the OpenWeatherMap API (https://openweathermap.org/). This application monitors real-time weather data using the OpenWeatherMap API, aggregates daily weather summaries, 
and provides alerting features based on user-defined thresholds. 

## Table of Contents
1) **Features**
2) **Dependencies**
3) **Setup Instructions**
4) **Usage**
5) **Running the Application**
6) **Testing**
7) **License**

## Features
1. Continuous retrieval of weather data for major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
2. Daily weather summary rollups, including average, maximum, and minimum temperatures, and dominant weather conditions.
3. User-configurable alerting thresholds for temperature and specific weather conditions.
4. Visualizations for daily weather summaries and alerts.


## Dependencies

To run this application, ensure you have the following installed:

1. Python 3.7 or later
2. Flask
3. Requests
4. PyYAML
5. Matplotlib (for visualizations, optional)
6. Unittest (for testing, included with Python)


### Install Dependencies

You can install the required Python packages using `pip`. It is recommended to create a virtual environment to avoid conflicts with other projects.

#Create a virtual environment (optional but recommended)

'python -m venv venv'

#Activate the virtual environment

'venv\Scripts\activate'

#Install the required packages

pip install Flask requests pyyaml matplotlib

## Setup Instructions
1. **Get an API Key:**

   Sign up at OpenWeatherMap and obtain your free API key.

2. **Configuration:**

Create a config.yaml file in the root directory of the project. Here’s a sample configuration:

api_key: your_valid_openweathermap_api_key

cities:

  - Delhi
    
  - Mumbai
    
  - Chennai
  - Bangalore
  - Kolkata
  - Hyderabad

interval: 300                         
#interval in seconds for fetching data

alert_threshold: 35.0                  
#temperature alert threshold in Celsius

## Usage'
To run the application, you need to have your configuration set up properly. You can start the application with:

'python main.py'

## Running the Application
1. After starting the application, open your web browser and navigate to http://127.0.0.1:5000 to access the web interface.
2. The application will automatically fetch weather data at the specified interval and provide visualizations based on the aggregated data.

## Testing
To run the tests, execute the following command in the terminal:

'python -m unittest discover tests'

This command will discover and run all tests in the tests directory.

## License
This project is licensed under the MIT License.

### Key Sections Explained

1. **Features**: Lists what the application does.
2. **Dependencies**: Specifies the required libraries and Python version needed to run the application.
3. **Setup Instructions**: Guides users through getting an API key and setting up configuration files.
4. **Usage**: Provides commands to run the application.
5. **Running the Application**: Explains how to access the web interface.
6. **Testing**: Instructions for running unit tests to ensure the application is functioning correctly.
7. **License**: Mentions the licensing details.

### Final Touches
Make sure to:

- Replace `your_valid_openweathermap_api_key` with instructions on how to get their own API key.
- Adjust any details specific to your project.
- Add or modify sections as necessary to fit your application's requirements.


**Thank You**
