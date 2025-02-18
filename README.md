1. Project Overview
This project will use a Convolutional Neural Network (CNN) to analyze and classify workout exercises using the WorkoutFitness Video Dataset from Kaggle. The goal is to develop a model that can detect and assess exercise form, helping users receive feedback on their performance.

2. Objectives
Train a CNN model to classify different workout exercises.

Detect key movement patterns and analyze exercise form.

Provide real-time feedback on user performance.

Deploy the model for easy access via a web or mobile interface.


4. Dataset & Data Preprocessing

Dataset: WorkoutFitness Video Dataset

Feature Extraction: Utilizing OpenCV and MediaPipe for keypoint detection.

Labeling: Ensuring proper class labels for training.


7. Model Development
   
Base Model: Pre-trained mediapipe for feature extraction.

CNN Architecture: Custom-built layers to classify exercises.

Training: Using TensorFlow/Keras with augmentation techniques.

Evaluation Metrics: Accuracy, precision, recall, and F1-score.



updates:

1) I created a script and tested the mediapipe model and got it to run. I tested it on a video from the dataset. I output a new video with the key points added from mediapipe. 
   
2) Created a compute instance in Azure Machine Learning
   
3) Set up Azure Storage for dataset uploads

  
Next steps: 
1)Connect GitHub repo to Azure ML for automated workflows

2) Extract Keypoint Data and Save as CSV

   Write a script to extract joint positions per frame.
   
   Save this data in a structured format (CSV or JSON).

3)Engineer Features for Training
   Compute joint angles, speed, and repetitions.

4)Train the CNN Model
   Use TensorFlow/PyTorch to train a CNN on extracted pose data.

Current Output: a video with key features tracked, that saves the new video in a folder called processed videos. 

Goal: Extract the aforementioned features, and use them to train a CNN to classify which exercise is being performed.


running the code: 

run the following in powershell as admin (this is obviously my file path, change based on yours. Yes thats my gamertag/username)

cd "C:\Users\LongboyLog\DataAnalyticsCaptstone"

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python test_mediapipe.py


