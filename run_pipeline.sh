#!/bin/bash
echo "Running data preprocessing..."
python preprocess.py

echo "Training models..."
python train.py

echo "Evaluating models..."
python evaluate.py

echo "Pipeline execution complete!"
