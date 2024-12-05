import pickle
import pandas as pd

#load data
def load_data():
    new_data=pd.DataFrame([[0.01, 0.05, 0.08, 0.06]])
    return new_data

#load_model
def load_model():
    with open("trained_classifier.pkl", "rb") as file:
        model = pickle.load(file)
    return model

#make predictions
def make_predictions(data, model):
    return model.predict(data)

#write results
def write_results(predictions):
    print(predictions)

#orchestrate
def run():
    new_data = load_data()
    model=load_model()
    predictions=make_predictions(data=new_data, model=model)
    write_results(predictions=predictions)

if __name__ == "__main__":
    run()