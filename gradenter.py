#importing the essential libraries 
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
df=pd.read_csv('./Admission_Predict_Ver1.1.csv',index_col=0) 
#independent or explanatory variables 
feature_cols=['GRE Score','TOEFL Score','LOR','CGPA','Research']
X=np.array(df[feature_cols],dtype=np.float64)
#dependent or response variable
y=np.array(df['Chance of Admit'],dtype=np.float64)
#cross validation; splitting dataset into training and testing data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)
#Linear Regression model
lr=LinearRegression(n_jobs=-1)
#fitting the model
lr.fit(X_train,y_train,sample_weight=None)
y_pred=lr.predict(X_test) #predicting using the test dataset
accuracy=lr.score(X_test,y_test) #R squared shows how the data fit the model 
print("R^2 or Accuracy : " , round(accuracy,2))

v1=302;v2=102;v3=1.5;v4=8;v5='0';
pred_n=np.array([v1,v2,v3,v4,v5],dtype=np.float64)
pred_n=pred_n.reshape(1,-1)
pred_ad=lr.predict(pred_n)
print('\n ===Records entered===')
print(' GRE Score : ', v1, '\n TOEFL Score : ', v2, '\n LOR : ', v3, '\n CGPA : ', v4)
if(v5=="1"):
    print (' Research : Yes')
elif(v5=="0"):
    print(' Research : No')
elif(v5>"1"):
    print(' Research : Invalid input')
else:
    print(' Research : Invalid input')

pre_ad_round=np.round(np.array(pred_ad*100),2)
predict_admissions = str(pre_ad_round)[1:-1]
print(' Your chance of admission is', predict_admissions,'%')
if(pre_ad_round > 55.5):
    print (" Congratulations!!! of admission")
else :
    print (" Whooops!!! You did not reach!")
print(" ==========\n Thank you\n ==========")