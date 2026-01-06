#!/bin/bash

# 1. Install Dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# 2. Train Models
echo "Generating data and training models..."
python scripts/generate_data_and_train.py

# 3. Run Tests
echo "Running tests..."
pytest tests/

# 4. Start Server
echo "Starting server..."
uvicorn app.main:app --reload
