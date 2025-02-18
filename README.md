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

5. Model Development
Base Model: Pre-trained mediapipe for feature extraction.
CNN Architecture: Custom-built layers to classify exercises.
Training: Using TensorFlow/Keras with augmentation techniques.
Evaluation Metrics: Accuracy, precision, recall, and F1-score.

6. Challenges & Next Steps
Dataset Limitations: Expanding data through augmentation.
Generalization: Ensuring the model performs well across diverse users and video qualities.
Deployment Considerations: Optimizing for speed and accuracy.
Future Enhancements: Adding pose correction suggestions and form grading.


updates:

1) I created a script and tested the mediapipe model and got it to run. I tested it on a video from the dataset.
2) Created a compute instance in Azure Machine Learning
3) Set up Azure Storage for dataset uploads

  
Next steps: 
1)Connect GitHub repo to Azure ML for automated workflows
2)update the script to pull the XYZ coordinates from the videos in the dataset 
3)Store that data
4)Learn how to incorporate /// use that data to assist the CNN model 


running the code: 
run the following in powershell as admin (this is obviously my file path, change based on yours. Yes thats my gamertag/username)
cd "C:\Users\LongboyLog\DataAnalyticsCaptstone"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python test_mediapipe.py

