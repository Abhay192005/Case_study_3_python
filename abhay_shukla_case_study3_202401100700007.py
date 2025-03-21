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
