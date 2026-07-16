import pandas as pd
import numpy as np
import matplotlib.pylab as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score



def Advertising(Datapath):
    Border="_"*40
#------------------------------
#Step one l: load dataset
#------------------------------
    print(Border)
    print("step one :load dataset")
    print(Border)

    df = pd.read_csv(Datapath)

    print("few records from dataset:")

    print(df.head())

#-------------------------------
#Step one 2: remove unwanted columns
#------------------------------
    
    print(Border)
    print("step two :remove unwanted columns")
    print(Border)

    print("shape of dataset before removal :",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("shape of dataset after removal :",df.shape)

    print(Border)

    print("clean dataset is :")
    print(Border)

    print(df.head())

#------------------------------
#Step 3: check missing values
#-------------------------------

    print(Border)
    print(" step 3 : check missing values")
    print(Border)

    print("missing values count :\n",df.isnull().sum())

#-------------------------------------
#Step 4: Display statistical summary
#-------------------------------------

    print(Border)
    print(" step 4 : Display statistical summary")
    print(Border)

    print(df.describe())

#-------------------------------------------
#Step 5: Display corelation between column
#-------------------------------------------

    print(Border)
    print(" step 5 : Display corerelation between columns")
    print(Border)   
     
    print("corelation matrix")
    print(df.corr())

#----------------------------------------------------------------
#Step 6: split dataset into independant and dependant variables
#----------------------------------------------------------------

    print(Border)
    print("Step 6: split dataset into independant and dependant variables")
    print(Border)   

    X=df[['TV','radio','newspaper']]
    
    Y=df['sales']

    print("independant variable :",X.shape)
    print("dendependant variable :",Y.shape)

#--------------------------------------------
#Step 7: split dataset for  training nd testing
#------------------------------------------------

    print(Border)
    print("Step 7: split dataset for  training nd testing")
    print(Border)   


    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train:",X_train.shape)
    print("X_test:",X_test.shape)
    print("Y_train:",Y_train.shape)
    print("Y_train:",Y_train.shape)

#------------------------------
#Step 8: create the model
#-------------------------------

    print(Border)
    print("#Step 8: create & train the model")
    print(Border)   


    model = LinearRegression()

    model.fit(X_train,Y_train)


#------------------------------
#Step 9:  test the model
#-------------------------------

    print(Border)
    print("Step 9 : test he model")
    print(Border)   


    y_pred = model.predict(X_test)

#------------------------------
#Step 10:  evaluate the model
#-------------------------------

    print(Border)
    print("Step 10 : evaluate he model")
    print(Border)


    MSE = mean_squared_error(Y_test,y_pred)

    RMSE= np.sqrt(MSE)

    R2= r2_score(Y_test,y_pred)


    print("mean squared error:",MSE)
    print("root mean squared error :",RMSE)

    print("R square value ", R2)  
#-------------------------------------------------
#Step 11:  evaluate the model
#-------------------------------------------------

    print(Border)
    print("step 11: calculate model coefficient")
    print(Border)
    for column , value in zip(X.columns,model.coef_):
        print(f"{column}:{value}")

    print("intercept :",model.intercept_)    
 
#-------------------------------------------------
#Step 12:  Compare the Actual nd Predicted values 
#-------------------------------------------------
    print(Border)
    print("step 12: compare the Actual and Predicted values")
    print(Border)

    Result = pd.DataFrame({'Actual sale':Y_test.values,
                           'predicted sale ':y_pred
                          })
    

    print(Result.head())
#-------------------------------------------------
# Step 13:  plot actual vs predicted
#-------------------------------------------------

    print(Border)



    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,y_pred)

    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Actual sales vs Predicted")
    plt.grid(True)
    plt.show()

    

def main():

    Advertising("Advertising.csv")


if __name__=="__main__":
    main()    