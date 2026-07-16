# 📊 Advertising Sales Prediction using Linear Regression

This project demonstrates how to build and evaluate a **Linear Regression model** using the classic *Advertising dataset*.  
The dataset contains advertising spend across **TV, Radio, and Newspaper** channels, and the goal is to predict **Sales**.

---

## 🚀 Project Workflow

The script follows a clear step-by-step pipeline:

1. **Load Dataset**  
   Reads the `Advertising.csv` file into a Pandas DataFrame.

2. **Data Cleaning**  
   Removes unwanted columns (like `Unnamed: 0`).

3. **Missing Values Check**  
   Ensures there are no null values.

4. **Statistical Summary**  
   Displays descriptive statistics of the dataset.

5. **Correlation Analysis**  
   Prints correlation matrix to understand relationships between features.

6. **Feature Selection**  
   Independent variables: `TV`, `radio`, `newspaper`  
   Dependent variable: `sales`

7. **Train-Test Split**  
   Splits dataset into training (80%) and testing (20%).

8. **Model Training**  
   Fits a **Linear Regression** model using scikit-learn.

9. **Model Testing**  
   Predicts sales on the test dataset.

10. **Model Evaluation**  
    - Mean Squared Error (MSE)  
    - Root Mean Squared Error (RMSE)  
    - R² Score

11. **Model Coefficients**  
    Displays feature coefficients and intercept.

12. **Results Comparison**  
    Shows a DataFrame comparing actual vs predicted sales.

13. **Visualization**  
    Plots **Actual vs Predicted Sales** using Matplotlib.

---

## 📂 Project Structure

Advertising-Regression/
│── Advertising.csv        # Dataset
│── advertising_model.py   # Main script
│── README.md              # Project documentation


---

## 🛠️ Requirements

Install dependencies before running the script:

```bash
pip install pandas numpy matplotlib scikit-learn seaborn

git clone https://github.com/AbhijeetGorale/Advertising-Regression.git
cd Machine-Learning

To Run the Script
python advertising_model.py

📊 Sample Output
Dataset summary and correlation matrix

Model evaluation metrics:

MSE, RMSE, R²

Coefficients for TV, Radio, Newspaper

Scatter plot of Actual vs Predicted Sales

🔮 Future Improvements
Add heatmap visualization for correlation.

Include Mean Absolute Error (MAE) for better interpretability.

Try other models (e.g., Ridge, Lasso, Random Forest) for comparison.

Deploy as a simple Flask/Django web app with interactive predictions.

📜 License
This project is licensed under the MIT License.
Feel free to use, modify, and share!

👨‍💻 Author
Abhijeet Gorale
Passionate about Data Science, Machine Learning, and building end-to-end projects.



