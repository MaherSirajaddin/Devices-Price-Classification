import csv
import requests

# Define the endpoints
POST_ENDPOINT = "http://localhost:8080/api/devices"
PREDICT_ENDPOINT = "http://localhost:8080/api/devices/predict/{}"

# Read data from CSV file
def read_csv(file_path, num_samples):
    devices = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if len(devices) >= num_samples:
                break
            device = {}
            for key, value in row.items():
                if key in ["battery_power", "fc", "int_memory", "mobile_wt", "n_cores", "pc", "px_height", "px_width", "ram", "sc_h", "sc_w", "talk_time"]:
                    device[key] = int(value)
                elif key in ["clock_speed", "m_dep"]:
                    device[key] = float(value)
                elif key in ["blue", "dual_sim", "four_g", "three_g", "touch_screen", "wifi"]:
                    device[key] = value == '1'
            devices.append(device)
    return devices

# Post data to the API and get the ID
def post_device_data(device):
    response = requests.post(POST_ENDPOINT, json=device)
    if response.status_code == 200:
        return response.json().get("id")
    else:
        print(f"Failed to post device data: {response.text}")
        return None

# Get the price range using the ID
def get_price_range(device_id):
    response = requests.post(PREDICT_ENDPOINT.format(device_id))
    if response.status_code == 200:
        return response.json().get("price_range")
    else:
        print(f"Failed to get price range: {response.text}")
        return None

def main():
    file_path = "AI/model/data/test.csv" 
    Num_test_samples = 10
    devices = read_csv(file_path, Num_test_samples)
    
    
    for device in devices:
        device_id = post_device_data(device)
        if device_id:
            price_range = get_price_range(device_id)
            print(f"Device ID: {device_id}, Price Range: {price_range}")

if __name__ == "__main__":
    main()
