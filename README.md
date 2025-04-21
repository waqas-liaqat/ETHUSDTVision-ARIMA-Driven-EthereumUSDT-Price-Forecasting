# **ETHUSDTVision: ARIMA-Driven Ethereum (ETH/USDT) Price Forecasting**

## **Project Overview**

This project, **ETHUSDTVision**, focuses on forecasting Ethereum (ETH/USDT) prices using time series analysis with ARIMA-based models (ARIMA, SARIMA, and SARIMAX). The project spans data collection, exploratory data analysis (EDA), model development, evaluation, and deployment of an interactive web application using Streamlit. Historical Ethereum price data from Yahoo Finance (2017-11-09 to 2025-04-17) is used to build and evaluate the forecasting models, with the best model being a SARIMA(2,1,1)(1,1,1,7) configuration (RMSE: 1191.46, MAPE: 34.05%).

### **Key Achievements**
- **Data**: Collected and preprocessed 2,717 days of ETH/USDT OHLC data.
- **EDA**: Identified weekly seasonality (period=7) and non-stationarity, addressed via differencing (d=1).
- **Modeling**: Tested 36 ARIMA/SARIMA/SARIMAX variants, selecting SARIMA(2,1,1)(1,1,1,7) as the optimal model.
- **Forecasting**: Generated 30-day forecasts with 95% confidence intervals.
- **Deployment**: Built an interactive Streamlit web app for price forecasting and visualization.
- **Insights**: Model is best suited for short-term (7-30 days) trading strategies, with volatility impacting long-term accuracy.

## **Project Structure**

```
ETHUSDTVision-ARIMA-Driven-EthereumUSDT-Price-Forecasting/
│
├── Artifacts/
│   ├── arima_model_comparison.csv      # Model performance comparison
│   ├── model_eth_20250419.pkl          # Best SARIMA model artifact
│   └── model_metadata_20250419.json    # Metadata for the best model
│
├── Data/
│   ├── eth_usdt_data_clean.csv         # Cleaned dataset (forward-filled)
│   └── eth_usdt_data.csv               # Raw dataset from Yahoo Finance
│
├── Notebooks/
│   ├── Data_Collection.ipynb           # Data collection and preprocessing
│   ├── EDA.ipynb                       # Exploratory data analysis
│   └── Model_Building.ipynb            # Model development and evaluation
│
├── Reports/
│   ├── Ethereum_ARIMA_Presentation (1).pptx  # Project presentation
│   └── Report.docx                     # Detailed project report
│
├── app.py                              # Streamlit web app
├── .gitignore                          # Git ignore file
├── README.md                           # Project documentation (this file)
└── requirements.txt                    # Dependencies
```

## **Prerequisites**

To run this project locally, ensure you have the following installed:
- Python 3.8 or higher
- Git (for cloning the repository)

## **Setup Instructions**

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/waqas-liaqat/ETHUSDTVision-ARIMA-Driven-EthereumUSDT-Price-Forecasting.git
   cd ETHUSDTVision-ARIMA-Driven-EthereumUSDT-Price-Forecasting
   ```

2. **Create a Virtual Environment** (optional but recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   Install the required Python packages listed in `requirements.txt`.  
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Data**  
   The `Data/` folder already contains the preprocessed dataset (`eth_usdt_data.csv`). If you wish to collect fresh data, run the `Data_Collection.ipynb` notebook.

## Usage

### **1. Explore the Notebooks**
- **Data Collection**: Run `Notebooks/Data_Collection.ipynb` to collect and preprocess ETH/USDT data using the Yahoo Finance API.
- **Exploratory Data Analysis (EDA)**: Run `Notebooks/EDA.ipynb` to analyze price trends, seasonality, volatility, and stationarity.
- **Model Building**: Run `Notebooks/Model_Building.ipynb` to develop, evaluate, and save the best ARIMA/SARIMA/SARIMAX model.

### **2. Run the Streamlit Web App**
Launch the interactive forecasting app using the following command:  
```bash
streamlit run app.py
```
- The app allows you to:
  - Adjust forecast periods (7-90 days).
  - Toggle confidence intervals.
  - View model performance metrics.
  - Visualize historical data and forecasts.

### **3. Review the Report and Presentation**
- The detailed project report is available in `Reports/Report.docx`.
- The presentation summarizing the project is in `Reports/Ethereum_ARIMA_Presentation (1).pptx`.

## **Model Details**

### **Best Model**
- **Type**: SARIMA(2,1,1)(1,1,1,7)
- **Performance**:
  - RMSE: 1191.46
  - MAPE: 34.05%
  - AIC: 24880.74
- **Cross-Validation**:
  - Mean CV RMSE: 757.62 ± 500.53

### **Forecasting**
- 30-day forecasts are generated with 95% confidence intervals.
- Example projections:
  - 7-day forecast: $1,631 ± $142
  - 30-day forecast: $1,635 ± $210

### **Limitations**
- High volatility reduces accuracy beyond 30 days.
- No exogenous variables (e.g., news, BTC correlation) are included.
- Fixed seasonal period (7 days) may not capture all market cycles.

## **Recommendations for Future Work**
1. **Hybrid Models**: Combine ARIMA with LSTM for better long-term forecasting.
2. **Exogenous Variables**: Incorporate on-chain metrics, sentiment analysis, or BTC prices.
3. **Volatility Modeling**: Integrate GARCH models to handle Ethereum's volatility.
4. **Real-time Data**: Build a pipeline for live data updates.

## **Contributing**
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **Contact**
**Author**: Muhammad Waqas  
**Email**: waqasliaqat630@gmail.com  
**GitHub**: [waqas-liaqat](https://github.com/waqas-liaqat)
