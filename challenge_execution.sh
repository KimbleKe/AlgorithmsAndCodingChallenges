#!/bin/bash

# Check if argument is provided
if [ $# -eq 0 ]; then
  echo "Error: Please provide the challenge folder name"
  echo "Usage: ./challenge_execution.sh <FolderName>"
  exit 1
fi

CHALLENGE_NAME=$1
INPUT_FILE="CodingChallengeSolutions/$CHALLENGE_NAME/input.txt"
PYTHON_SCRIPT="CodingChallengeSolutions/$CHALLENGE_NAME/solution_debug.py"

# Check if files exist
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Error: Python script not found at $PYTHON_SCRIPT"
  exit 1
fi

if [ ! -f "$INPUT_FILE" ]; then
  # Execute the Python script without a input file
  python3 "$PYTHON_SCRIPT"
else
  # Execute the Python script with the input file
  python3 "$PYTHON_SCRIPT" "$INPUT_FILE"
fi
