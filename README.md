#  Financial Market Tracker

A full-stack Streamlit web application that allows users to search stock tickers, view company information, visualize historical price data, and generate 30-day ARIMA forecasts. Users can also save and manage their favorite tickers with login/signup authentication, all backed by a MySQL database.

---

## 🔧 Features

- 🔐 User authentication (Sign up / Log in / Log out)
- 🔍 Ticker search (e.g., AAPL, TSLA)
- 📝 Company info and previous close display
- 📈 Historical price + 30-day ARIMA forecast plot
- 💾 Save/Delete tickers to user profile
- 🐳 Dockerized for easy deployment
- ☁️ Polygon.io integration for real-time financial data

---

## 📦 Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend**: Python (custom logic + REST-like actions)  
- **Database**: MySQL  
- **Forecasting**: `pmdarima` (ARIMA)  
- **Deployment**: Docker + Docker Compose  
- **API**: [Polygon.io](https://polygon.io)

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/financial-market-tracker.git
cd financial-market-tracker


2️⃣ Set Up .env File
Create a .env file in the root directory and include your configuration:

env
Copy code
# MySQL Config
DB_HOST=db
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name

# Polygon API
API_KEY=your_polygon_api_key
📝 Replace values with your actual credentials and API key.

3️⃣ Run with Docker Compose
Before you start, make sure MySQL is not already running locally on your device (e.g., from a previous install or service). Docker will run its own MySQL container, and port conflicts on 3306 will cause errors.

Build and launch the app:

bash
Copy code
docker-compose up --build
Streamlit app will be live at: http://localhost:8501

MySQL will be running inside the container at: localhost:3306

To stop and clean up containers:

bash
Copy code
docker-compose down
