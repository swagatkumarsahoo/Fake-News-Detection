
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:45:40 2024

@author: Swagat
"""

import pickle

#doc_new = ['obama is running for president in 2016']

user_input = input("Please enter the news text you want to verify (max 500 characters): ")


# Removed the print statement for user input



#function to run for prediction
def detecting_fake_news(user_input):  
    if len(user_input) > 500:
        print("Input text is too long. Please limit to 500 characters.")
    if not user_input:
        print("Input cannot be empty.")
        return

        return

#retrieving the best model for prediction call
    try:
        load_model = pickle.load(open('final_model.sav', 'rb'))  # Corrected line
    except FileNotFoundError:
        print("Model file not found.")
        return
    except pickle.UnpicklingError:
        print("Failed to load the model. The file may be corrupted.")
        return







    prediction = load_model.predict([user_input])  

    if prediction[0] == 1:
        result = "Fake"
    else:
        result = "Real"

    prob = load_model.predict_proba([user_input])


    return (print("The given statement is ", result),

        print("The truth probability score is ",prob[0][1]))


if __name__ == '__main__':
    result = detecting_fake_news(user_input)
    if result is not None:
        print(f"The given statement is {result['result']}")
        print(f"The truth probability score is {result['probability']}")
