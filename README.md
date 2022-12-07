# Criminal Recognition and Tracking system

## Team Members :

### 1 Nilay Shirke
### 2 Pratham More
### 3 Saurabh Patil

## Team Mentor :

### 1 Prof.A.R.Surve


## Problem Statements :

### Daily Increase in Robbery, Kidnapping and other Crimes
### Manual CCTV Monitoring
### Keeping Track Records of Criminals
### Preventive Security Measures


## Tech Stack :

### Face Detection using OpenCV and MTCNN library
### Face Recognition using SVC,  SKLearn,  Keras
### GPU using Google Colab, Tensorflow
### Alert notification using SMTP
### Criminal Data storage using Firebase Database

## Requirement 
### Python version 3.6


## Procedure to add camera :

### Move to folder 'Criminal-Detection-and-Tracking' using command 'cd Criminal-Detection-and-Tracking'
### To start GUI run command 'python ./Code.py'
### Here you can create account of Organization and add CCTV camera details
   - Location : IP address of camera
   - Lattitude, Longitude of camera
   - CCTV camera Incharge Name
   - Email address of Guards
   - Email address of nearby Police Station


## Procedure to start Django website for location tracking and criminal details(Only for police officers) :

### Move to folder 'CRpro' using command 'cd CRpro'
### To start Django website run command 'python manage.py runserver'
### Here you can track location of criminal and view criminal profile


## Procedure to start Camera using IP address :
### To start running criminal recognition run command 'python startCam.py'

## Procedure to take multiple images of criminal :
### Run command 'python data_collect.py'

## Procedure to create dataset for criminal recignition :
### Add criminal images in dataset folder with proper id of criminal
### Run command 'python train_test.py'
### Run command 'python train_test_embeddings.py'







