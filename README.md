1. Project Overview
This project leverages a Convolutional Neural Network (CNN) to analyze and classify workout exercises using the WorkoutFitness Video Dataset from Kaggle. The goal is to develop a model that can detect and assess exercise form, helping users receive feedback on their performance.

2. Objectives
Train a CNN model to classify different workout exercises.
Detect key movement patterns and analyze exercise form.
Provide real-time feedback on user performance.
Deploy the model for easy access via a web or mobile interface.
3. Dataset & Data Preprocessing
Dataset: WorkoutFitness Video Dataset
Data Cleaning: Handling missing or low-quality frames.
Feature Extraction: Utilizing OpenCV and MediaPipe for keypoint detection.
Labeling: Ensuring proper class labels for training.
4. Model Development
Base Model: Pre-trained InceptionV3 or ResNet for feature extraction.
CNN Architecture: Custom-built layers to classify exercises.
Training: Using TensorFlow/Keras with augmentation techniques.
Evaluation Metrics: Accuracy, precision, recall, and F1-score.

5. Challenges & Next Steps
Dataset Limitations: Expanding data through augmentation.
Generalization: Ensuring the model performs well across diverse users.
Deployment Considerations: Optimizing for speed and accuracy.
Future Enhancements: Adding pose correction suggestions and form grading.


updates:

1) I created a script and tested the mediapipe model and got it to run. I tested it on a video of me posing.
2) Created a compute instance in Azure Machine Learning
3) Set up Azure Storage for dataset uploads
4) Next steps: Connect GitHub repo to Azure ML for automated workflows  


running the code: 
run the following in powershell as admin (this is obviously my file path, change based on yours. Yes thats my gamertag/username)
cd "C:\Users\LongboyLog\DataAnalyticsCaptstone"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python test_mediapipe.py

