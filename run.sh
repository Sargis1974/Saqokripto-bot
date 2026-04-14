#!/bin/bash

cd ~/saqo_core

echo "🚀 SAQO FULL AUTO START"

while true
do
    python3 saqo_kripto_bot.py >> bot.log 2>&1
    echo "⚠️ Restarting bot..."
    sleep 5
done
