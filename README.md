# 🏠 Bangalore House Price Prediction

A machine learning project that predicts house prices in Bangalore, India using Ridge Regression. The project includes a complete data preprocessing pipeline and an interactive web application built with Streamlit.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preprocessing](#data-preprocessing)
- [Model Performance](#model-performance)
- [Results](#results)
- [Future Improvements](#future-improvements)

## 🎯 Overview

This project predicts house prices in Bangalore based on key property features such as location, total square footage, number of bedrooms (BHK), and bathrooms. The model was trained on a dataset of over 13,000 properties and achieves an R² score of approximately 0.82.

## ✨ Features

- **Interactive Web Application**: User-friendly Streamlit interface for price predictions
- **Data Cleaning Pipeline**: Comprehensive preprocessing including outlier removal and feature engineering
- **Multiple Model Comparison**: Evaluated Linear Regression, Lasso, and Ridge Regression models
- **Location-based Predictions**: Supports predictions for various locations across Bangalore
- **Real-time Predictions**: Instant price estimates based on property features

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning library
  - Ridge Regression
  - OneHotEncoder
  - StandardScaler
  - Pipeline
- **Matplotlib** - Data visualization
- **Pickle** - Model serialization

## 📁 Project Structure

```
Bangalore House Price Prediction/
│
├── app.py                              # Streamlit web application
├── Bangalore_House_Price_Prediction.ipynb  # Jupyter notebook for data analysis and model training
├── Bengaluru_House_Data.csv           # Original raw dataset
├── Cleaned_data.csv                   # Preprocessed dataset
├── RidgeModel.pkl                     # Trained Ridge Regression model
├── requirements.txt                   # Python dependencies
├── Description.pdf                    # Project description document
├── README.md                          # Project documentation
└── .streamlit/                        # Streamlit configuration directory
    └── config.toml                    # Streamlit app configuration
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Bangalore House Price Prediction"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Web Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Access the application**
   - The app will automatically open in your default web browser
   - Default URL: `http://localhost:8501`

3. **Make Predictions**
   - Select the property location from the dropdown menu
   - Enter the total square footage
   - Specify the number of bedrooms (BHK)
   - Enter the number of bathrooms
   - Click "Predict Price" to get the estimated price

### Using the Jupyter Notebook

1. **Open the notebook**
   ```bash
   jupyter notebook Bangalore_House_Price_Prediction.ipynb
   ```

2. **Run all cells** to reproduce the data preprocessing and model training pipeline

## ☁️ Streamlit Cloud Deployment

### Prerequisites

1. **GitHub Repository**: Push your project to a GitHub repository
2. **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io)

### Deployment Steps

1. **Ensure Required Files are Present**
   - `app.py` (main application file)
   - `requirements.txt` (dependencies)
   - `RidgeModel.pkl` (trained model)
   - `Cleaned_data.csv` (data file)

2. **Connect Repository**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Select the branch (usually `main` or `master`)
   - Set the main file path to `app.py`

3. **Deploy**
   - Click "Deploy"
   - Wait for the build process to complete

### Troubleshooting Deployment Issues

If you encounter errors during deployment:

1. **Check File Structure**
   - Ensure `requirements.txt` is in the root directory
   - Verify all required files (`RidgeModel.pkl`, `Cleaned_data.csv`) are committed to the repository

2. **Requirements.txt Format**
   - The file should have one package per line
   - No trailing spaces or empty lines
   - Use simple package names (Streamlit Cloud will resolve compatible versions)

3. **File Path Issues**
   - Ensure file paths in `app.py` match the actual file names
   - Use relative paths (e.g., `'RidgeModel.pkl'` not `'./RidgeModel.pkl'`)

4. **Common Errors**
   - **"Invalid requirement"**: Check `requirements.txt` format and ensure it's in the root directory
   - **"File not found"**: Verify all required files are committed to the repository
   - **"Non-zero exit code"**: Check the build logs for specific package installation errors

5. **File Size Limits**
   - Streamlit Cloud has file size limits
   - If `RidgeModel.pkl` or `Cleaned_data.csv` are too large, consider:
     - Compressing the model file
     - Using a smaller sample of the data for deployment
     - Storing large files in cloud storage (S3, etc.) and loading them at runtime

## 🔧 Data Preprocessing

The data preprocessing pipeline includes the following steps:

1. **Data Cleaning**
   - Removed unnecessary columns (area_type, availability, society, balcony)
   - Handled missing values in location, size, and bath columns

2. **Feature Engineering**
   - Extracted BHK from the 'size' column
   - Converted range values in 'total_sqft' (e.g., "1133-1384") to mean values
   - Created 'price_per_sqft' feature for outlier detection

3. **Outlier Removal**
   - Removed properties where `total_sqft/bhk < 300` (unrealistic properties)
   - Removed outliers in `price_per_sqft` using statistical methods (mean ± std)
   - Removed BHK outliers based on location-wise analysis

4. **Location Consolidation**
   - Grouped locations with ≤10 properties into "other" category
   - Reduced location categories for better model performance

5. **Data Transformation**
   - Applied OneHotEncoding to categorical 'location' feature
   - Standardized numerical features using StandardScaler

## 📊 Model Performance

The project compares three regression models:

| Model | R² Score | MAE (Lakhs) | RMSE (Lakhs) |
|-------|----------|-------------|--------------|
| **Ridge Regression** | **0.8234** | **18.17** | **35.60** |
| Linear Regression | 0.8234 | 18.18 | 35.60 |
| Lasso Regression | 0.8128 | 19.46 | 36.65 |

**Ridge Regression** was selected as the final model due to its best performance and regularization benefits.

### Model Metrics Explanation

- **R² Score**: Coefficient of determination (~0.82 means the model explains ~82% of the variance)
- **MAE (Mean Absolute Error)**: Average prediction error (~18.17 Lakhs)
- **RMSE (Root Mean Squared Error)**: Penalizes larger errors (~35.60 Lakhs)

## 📈 Results

- **Training Data**: 5,888 properties
- **Testing Data**: 1,473 properties
- **Total Locations**: 240+ unique locations
- **Price Range**: Varies by location and property features
- **Model Accuracy**: ~82% (R² score)

## 🔮 Future Improvements

- [ ] Hyperparameter tuning for Ridge Regression
- [ ] Feature engineering (e.g., distance to city center, nearby amenities)
- [ ] Ensemble methods (Random Forest, Gradient Boosting)
- [ ] Model deployment to cloud platforms (Heroku, AWS, etc.)
- [ ] Real-time data updates from property websites
- [ ] Additional features (parking, floor number, age of property)
- [ ] Interactive data visualizations in the web app
- [ ] Model explainability features (SHAP values)

## 📝 Notes

- Prices are predicted in **Lakhs** (1 Lakh = ₹100,000)
- The model is trained on historical data and predictions should be used as estimates
- Actual prices may vary based on market conditions, property condition, and other factors not included in the model

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Created as part of a machine learning project for Bangalore house price prediction.

---

**Note**: Make sure all required files (`RidgeModel.pkl`, `Cleaned_data.csv`) are present in the project directory before running the application.
