# UWIParkPiTracker
[UWI Park WebApp.](https://uwi-park-tracker.firebaseapp.com)

This project serves to facilitate our solution to the problem of parking in our university. The team comprises of myself, David Orr and Rachel Peters (github profiles will be linked). People who come to our university, be it as a student, staff or visitor my have found themselves struggling to find a parking spot. We decided to create a system to solve this problem

The system comprised of a raspberry pi with a camera. The camera would take pictures of a parking lot, perform image detection and count the amount of cars currently parked up in the parking lot. That information would then be sent to the web application to be processed and displayed for public viewing. We created the website in such a way as to help drivers make a decision on where would be the best place to go first to get a parking space. The vision for the future of the system is to be able to display a virtual representation of each carpark depicting which spaces are taken up so that drivers would know exactly where they would be able to park.

This repo holds the code for the raspberry pi the conduct the image recognition and change the information in Firebase accordingly.

## Libraries
* Tensorflow >= 1.4.0
* OpenCV >= 3.0
* Tensorflow Object Detection API (Set up for this found below)
* Firebase Admin
[Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)

## Running the image recognition
The code responsible for the image recognition is found in the file path object_detection/object_detection_tutorial.ipynb. This file needs to be run using Jupyter Notebooks. An alternative can be found in the file path object_detection/object_detection_tutorial.py.

## Running the Firebase Code
The file containing the code to change information on firebase can be found under the filename raspPi.py. This requires the firebase_admin ptyhon module installed.
