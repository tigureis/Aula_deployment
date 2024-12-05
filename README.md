# Iris Flower Classifier

This project demonstrates a simple machine learning pipeline for classifying iris flowers using the famous Iris dataset and a Decision Tree Classifier. To be used as a base for others machininbg learning projects.

## Overview

The project is divided into two main parts, implemented in separate Python files:

1.  **Training (`train.py`):** This script extracts data from the Iris dataset, prepares features, trains a Decision Tree Classifier, and saves the trained model to a file (`trained_classifier.pkl`).
2.  **Prediction (`predict.py`):** This script loads the trained model, loads new data, makes predictions on the new data using the loaded model, and prints the predictions.

## How to Run

1.  **Install Dependencies:** Make sure you have the following libraries installed:
 
2.  **Training:** Execute the `train.py` script to train the model and save it:

 3.  **Prediction:** Execute the `predict.py` script to load the trained model, make predictions on new data, and print the results:

 
## File Structure

-   `train.py`: Python script for training the model.
-   `predict.py`: Python script for making predictions.
-   `trained_classifier.pkl`: This file stores the trained Decision Tree Classifier model.

## Functionality

**`train.py`:**

-   `extract_data()` : Loads the Iris dataset from scikit-learn.
-   `preparing_features()` : Creates a Pandas DataFrame for features (X) and target (y).
-   `train_model()` : Trains a Decision Tree Classifier with a maximum depth of 2.
-   `serialize_object()` : Saves the trained model to a file using pickle.
-   `run()` : Orchestrates the training pipeline.

**`predict.py`:**

-   `load_data()` : Loads new data for prediction.
-   `load_model()` : Loads the trained model from the file.
-   `make_predictions()` : Makes predictions on the new data using the loaded model.
-   `write_results()` : Prints the predictions.
-   `run()` : Orchestrates the prediction pipeline.


2.  **Training:** Execute the `train.py` script to train the model and save it:
