import testing , MoneyStatus
import pickle
import json
import random
import time

class PredictionTree(object):
    def welcome(self):
        WELCOME_INTENT = ["Hello! I am CyberEye. How may I help you?\n",
                          "Hi! I am CyberEye. How may I help you?\n",
                          "Hey! I am CyberEye. How may I help you?\n"]
        print(random.choice(WELCOME_INTENT))
        time.sleep(2)
        x=input()
        print("Okay, Please let me know what exactly happened in detail")
        pc = PredictionTree()
        return pc.predict_crime(input())
     ##this is aboyt Wallet or no wallet , this is done 
    def predict_crime(self, query):
        #load model
        loaded_model = pickle.load(open(testing.filename, 'rb'))
        matrix = [0,0,0]
        # target_names = ['lottery', 'no_crime']
        # print("accuracy score: " + str(loaded_model.score(testing.X_test, testing.y_test)))
        tag = testing.model.predict([query])
        print(tag)
        print(matrix)
        moc = PredictionTree()
        print("Did you use any of the Email/SMS/Online Classifieds which offered loans at suspicious rates")
        input()
        return moc.money_status()
  

    def money_status(self):
        print("Did you send any money as transaction fees / advance fees or any other fees to get the loan amount?\n")
        query = input()
        loaded_model = pickle.load(open(MoneyStatus.filename, 'rb'))
        money = MoneyStatus.model.predict([query])
        time.sleep(2.0)
        if money == "yes" :
          print("You have been a victim of Loan Fraud")## call the response function which gives the information here
          time.sleep(1.0)
          print
        else:
            print("You are a probable victim of Loan Fraud")## call the response function which gives the information here
        

## create an instance of the class PredictionTree()
pt = PredictionTree()
print(pt.welcome())
