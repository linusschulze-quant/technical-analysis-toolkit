# technical-analysis-toolkit

A modular, professional-grade Python framework for conducting systematic technical market analysis.

This repository provides reusable indicator functions and well-documented notebooks covering trend analysis, momentum indicators, volatility, risk-adjusted performance metrics, and multi-timeframe visualization techniques.

---

## 🚀 Features

- Price Trend Analysis (SMA & EMA)
- Momentum Indicators (MACD)
- Candlestick Charting (Short-Term Price Action)
- Risk-Adjusted Performance Metrics (Sharpe Ratio)
- Multi-Timeframe Analysis (1 Week, 1 Month, 1 Year, 3 Years)
- Comparative Benchmark Analysis (vs. S&P 500)
- Modular Indicator Functions (Reusable & Scalable)
- Visualization-Ready Chart Exporting

---

## 🧱 Project Structure

```text
technical-analysis-toolkit/
├── src/                        # Setup function
├── notebooks/
│   ├── Technical_Analysis/     # Indicator notebooks (EMA, MACD, SMA, Candlesticks) & Sharpe Ratio
│   └── Performance_Analysis/   # Benchmark comparison
├── figures/                    # Exported charts & visual outputs
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/linuschulze-quant/technical-analysis-toolkit.git
cd technical-analysis-toolkit
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Set the ticker and parameters in `src/technical_setup.py`.
2. Run the notebooks in `notebooks/` in numerical order.
3. Review indicator calculations and visual outputs directly in the notebooks.
4. Optional: Export charts automatically to the `figures/` directory.

---

## 📊 Data Sources

Market data is sourced from:

- **[Yahoo Finance via yfinance](https://pypi.org/project/yfinance/)**  
- **[mplfinance](https://github.com/matplotlib/mplfinance)** for candlestick visualization  

> All datasets are used for research and educational purposes only.

---

## 🎯 Project Goals

- Build a transparent and reproducible technical analysis framework.  
- Separate indicator logic from visualization and experimentation.  
- Enable scalable, multi-asset market analysis workflows.  
- Support both discretionary and systematic trading research.  

---

## 👥 Target Audience

- Quantitative traders  
- Technical analysts  
- Finance students  
- Researchers building trading or signal-generation pipelines  

---

## ⚠️ Disclaimer

This project is for educational and research purposes only and **does not constitute financial advice**.
All data, charts, and analyses are provided "as is" and should be **independently verified** before making any financial decisions.  
Users are responsible for their own actions and interpretations.  

---

## 📬 Contributions

Pull requests and feedback are welcome. This project is under active development.
