# Quantitative Crypto Trading & On-Chain Analytics

## Overview
A comprehensive Python-based research environment for developing, testing, and analyzing quantitative trading strategies in the cryptocurrency markets. This project bridges traditional algorithmic trading techniques with blockchain-native fundamental data, creating a multi-signal master strategy.

## Key Features
- **Multi-Factor Signal Generation:** Combines traditional technical indicators (RSI, MACD, Moving Averages) with on-chain fundamentals.
- **On-Chain Analytics:** 
  - **Whale Tracking:** Monitors high-net-worth wallet movements via the Etherscan API.
  - **Exchange Flows:** Analyzes Bitcoin inflow/outflow as a proxy for market buying/selling pressure.
  - **Network Congestion Anomalies:** Detects Ethereum gas spikes using Web3.py and Infura RPC as indicators for DeFi liquidations and extreme volatility.
  - **NVT Ratio:** Calculates the Network Value to Transactions ratio (the crypto equivalent of a traditional P/E ratio) to identify overbought/oversold network conditions.
- **Historical Backtesting:** Evaluates strategy performance against a standard Buy & Hold baseline, including specific performance metrics during Bull and Bear market regimes.

## Project Structure
The research is divided into sequential Jupyter Notebooks, covering the complete quantitative pipeline:
- `00` - `04`: Data ingestion, cleaning, and exploratory data analysis (EDA).
- `05`: Technical indicator generation and price-action signals.
- `06`: Volatility and risk-management modeling.
- `07`: On-Chain Alpha (Whale tracking, Exchange Flows, Gas Anomalies, NVT) and Master Signal integration.
- `/utils/`: Helper functions, configuration management, and API wrappers.

## Technology Stack
- **Data Manipulation & Analysis:** `pandas`, `numpy`
- **Blockchain Interaction:** `web3.py`, Etherscan API, Blockchain.com API, Infura RPC
- **Visualization:** `matplotlib`, `seaborn`

## License
This project is licensed under the MIT License.

## Disclaimer
*This project is for educational and research purposes only. It does not constitute financial advice, and the quantitative models provided do not guarantee future performance in live markets.*
