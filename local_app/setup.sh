#!/bin/bash

echo ""
echo "=================================================="
echo "         HIBA Local - One-Click Setup"
echo "=================================================="
echo ""

echo "[1/3] Installing Python dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install dependencies."
    echo "Make sure Python 3.10+ is installed."
    exit 1
fi

echo ""
echo "[2/3] Downloading HIBA model (4.5 GB)..."
echo "This may take a few minutes depending on your internet speed."
python download_model.py
if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to download model."
    exit 1
fi

echo ""
echo "[3/3] Setup complete! Starting HIBA..."
echo ""
python app.py
