#!/bin/bash

# Prompt the user to enter the name of the Python file
read -p "Enter the name of the Python file(if problem with DB_NAME==config problem): " filename

# Check if the file exists
if [ -f "$filename" ]; then
    
   if [ -f "config.env" ]; then
    echo "File found: config.env"
    set -a
    source "config.env"
    set +a

    # Run the Python file
    python3 "$filename"
   else
    echo "File not found: config.env"
   fi
    

else
    echo "File not found: $filename"
fi
