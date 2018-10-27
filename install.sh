#!/usr/bin/env bash
echo -e "\e[95mInstalling Compressy...\e[0m"

# Install dependencies
echo "Installing required dependencies..."
pip3 install colored terminaltables
echo -e "\e[92mSuccessfully installed all dependencies!\e[0m"

# Set execute permissions
echo "Setting execute permissions..."
chmod +x ./compressy.py

echo -e "You may now run \e[1m./compressy.py\e[0m."
