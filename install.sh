#!/bin/bash

if [[ "$VIRTUAL_ENV" != "" ]]
then
    echo "Already in virtual environment: $VIRTUAL_ENV"
else
    echo "Creating and activating virtual environment"
    pip install virtualenv
    virtualenv env
    source env/bin/activate

    echo "Python version"
    python --version
fi


pip install -r requirements.txt