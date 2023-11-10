#!/bin/bash

# Get the current directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Add the project's root directory to the Python path
export PYTHONPATH="$DIR:$PYTHONPATH"