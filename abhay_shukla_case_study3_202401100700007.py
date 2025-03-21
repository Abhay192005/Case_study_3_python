# -*- coding: utf-8 -*-
"""Abhay_Shukla_case_study3_202401100700007.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TEOqBtEFrNXvfn7kEiOq3TmldR7PKbxF
"""

import random
import time
def monitor_temperature(threshold=30):
  while True:
    temperature = random.uniform(20, 40)
    print(f"Current temperature: {temperature:.1f}°C")
    if temperature > threshold:
      print(f"ALERT: Temperature exceeded {threshold}°C!")
    time.sleep(2)
if __name__ == "__main__":
  monitor_temperature()