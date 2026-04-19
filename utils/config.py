
# config.py — shared settings for all notebooks
# Edit these values here and they update everywhere

import os

# Project root (update this if your Drive path is different)
ROOT = "/content/drive/MyDrive/crypto_quant_project"

# Data paths
RAW_DATA      = f"{ROOT}/data/raw"
PROCESSED_DATA = f"{ROOT}/data/processed"
CACHE_DIR     = f"{ROOT}/data/cache"
RESULTS_DIR   = f"{ROOT}/results"
MODELS_DIR    = f"{ROOT}/models"

# Which crypto assets we're analyzing
COINS = ["bitcoin", "ethereum", "solana"]   # CoinGecko IDs
SYMBOLS = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]  # Exchange trading pairs

# How far back to pull historical data
LOOKBACK_DAYS = 365  # 1 year

# Ethereum node (using free public Infura endpoint for on-chain data)
# Sign up free at infura.io to get your own key later
ETH_RPC_URL = "https://cloudflare-eth.com"  # free, no key needed to start

print("✅ Config loaded")
