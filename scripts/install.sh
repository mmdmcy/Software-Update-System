#!/bin/bash

# This script automates the installation of dependencies and setup for the project.

# Update package list
sudo apt-get update

# Install Python and pip if not already installed
sudo apt-get install -y python3 python3-pip

# Install required Python packages
pip3 install -r ../requirements.txt

# Additional setup commands can be added here
echo "Installation completed successfully."