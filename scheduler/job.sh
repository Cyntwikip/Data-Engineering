#!/bin/bash

cd ~/Documents/Github/Data-Engineering/scheduler/

# Log file path
LOG_FILE="etl_pipeline.log"

# Log the start time
echo "$(date '+%Y-%m-%d %H:%M:%S') - Start running the ETL pipeline" | tee -a $LOG_FILE

# Save the current directory
ORIGINAL_DIR=$(pwd)

# Change to the directory containing orchestrator.py
cd ../basic_etl

# Activate the conda base environment
source ~/anaconda3/bin/activate base

# Run the ETL pipeline
python3 orchestrator.py

# Return to the original directory
cd "$ORIGINAL_DIR"

# Check if the script ran successfully
if [ $? -eq 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Done running the ETL pipeline" | tee -a $LOG_FILE
else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ETL pipeline failed" | tee -a $LOG_FILE
fi