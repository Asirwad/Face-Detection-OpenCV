<h1 align='center'>Face Detection using openCV</h1>


![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-1.1.2-green?logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.2.54-red?logo=opencv&logoColor=white)


A web application for real-time face detection using Flask and OpenCV.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)

## Introduction
This web application captures video from your webcam and performs real-time face detection using the OpenCV library. It then displays the video feed with rectangles drawn around detected faces on a web page built with Flask.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Asirwad/Face-Detection-OpenCV.git
   cd Face-Detection-OpenCV

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    
4. For CLI version
   ```bash
   python main_CLI.py

5. For flask version
   ```bash
   python flask_main.py
   ```
   Then goto browser and open:
   ```bash
   http://127.0.0.1:5000/  
