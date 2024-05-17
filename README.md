# Device Price Prediction API

This project is a Spring Boot application for managing devices and predicting their price range using a machine learning model served by a Python Flask API. The application includes RESTful endpoints for creating, retrieving, and predicting device prices.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Running the Project](#setup-and-running-the-project)
  - [Prerequisites](#prerequisites)
  - [Running the Spring Boot Application](#running-the-spring-boot-application)
  - [Running the Flask API](#running-the-flask-api)
- [API Endpoints](#api-endpoints)
- [Testing the API](#testing-the-api)

## Project Overview

This project aims to provide a RESTful API for managing a collection of devices, allowing users to create new devices, retrieve existing ones, and predict their price range. The price prediction is handled by a machine learning model exposed through a Python Flask API.

## Features

- **Create a new device**
- **Retrieve all devices**
- **Retrieve a specific device by ID**
- **Predict the price range of a device**

## Technologies Used

- **Spring Boot**: For building the RESTful API.
- **Python Flask**: For serving the machine learning model.
- **scikit-learn**: For  the machine learning model.

## Setup and Running the Project

### Prerequisites

- **Java JDK 17**
- **Python 3.8** or higher

### Running the Spring Boot Application

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MaherSirajaddin/Devices-Price-Classification.git
   cd Devices-Price-Classification
2. **Running the Flask API:**
   ```bash
   cd AI
   pip install -r requirements.txt
   python flask_api.py
3. **Running the SpringBoot API:**
   ```bash
   cd backend
   # build the app
   ./mvnw clean install

   # run the app 
   ./mvnw spring-boot:run
   
### API Endpoints
#### Device Endpoints
- POST /api/devices: Create a new device.
- GET /api/devices: Retrieve a list of all devices.
- GET /api/devices/{id}: Retrieve details of a specific device by ID.
- POST /api/devices/predict/{deviceId}: Predict the price range of a specific device by ID.

### Testing the API
- #### **You can use Postman or curl to test the API endpoints.**
1. **Example: Create a New Device:**
   ```bash
    curl -X POST http://localhost:8080/api/devices \
    -H "Content-Type: application/json" \
    -d '{
            "battery_power": 1322,
            "blue":false,
            "clock_speed":1.7,
            "dual_sim":true,
            "fc":6,
            "four_g":false,
            "int_memory":7,	
            "m_dep":0.8,	
            "mobile_wt":140,	
            "n_cores":3,	
            "pc":9,	
            "px_height":177,	
            "px_width":1990,	
            "ram":1418,	
            "sc_h":19,	
            "sc_w":17,	
            "talk_time":12,	
            "three_g":false,	
            "touch_screen":true,	
            "wifi":false
        }'

2. **Example: Predict the Price Range of a Device:**
   ```bash
    curl -X POST http://localhost:8080/api/devices/predict/1

- #### **You can use the python script created for testing multiple records from test dataset**
    ```bash
    python testing.py
    