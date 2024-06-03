#!/bin/bash

echo "Choose one tool:"
echo "1. Invert Files"
echo "2. Invert Words"
echo "3. Convert temperature units"
echo "4. Fibonnaci Number testing and sequence"
echo "5. Bmi calculator"
echo "Just type a number and press Enter:"
read command_option
if [[ $command_option -eq 1 ]]; then
  echo "Choose a file path and name:"
  read file_name
  python3 inverta_arquivos.py $file_name
elif [[ $command_option -eq 2 ]]; then
  python3 inverta_palavras.py
elif [[ $command_option -eq 3 ]]; then
  python3 temperature_conversion.py
elif [[ $command_option -eq 4 ]]; then
  python3 fibonacci_test.py
elif [[ $command_option -eq 5 ]]; then
  python3 bmi_calc.py
fi