import json

# Function to calculate cost per second of power consumption
def cost_of_power_consumption(powerRating, cost_per_kwh):
    try:
        # Calculate energy consumption per second in kWh
        energy_consumption_per_second = float(powerRating) / 1000
        cost_per_kwh_per_second = cost_per_kwh / 3600
        # Calculate the cost per second
        cost_per_second = energy_consumption_per_second * float(cost_per_kwh_per_second)
        return round(cost_per_second, 10)
    except Exception as e:
        print(f"An error occurred during calculation: {e}")
        return None

# Function to get float input from user with error handling
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to append device data to a JSON file
def append_to_json(device, number_of_device, power_rating, cost, currency,cost_per_day, cost_per_month, filename="energy_data.json"):
    data = {
        "device": device,
        "number_of_device": number_of_device,
        "power_rating": power_rating,
        "currency": currency,
        "cost": cost,
        "cost_per_day" : cost_per_day,
        "cost_per_month": cost_per_month,
        
    }

    try:
        # Load existing data if the file exists
        try:
            with open(filename, 'r') as file:
                devices_data = json.load(file)
        except FileNotFoundError:
            devices_data = []  # If the file doesn't exist, start with an empty list

        # Append new data
        devices_data.append(data)

        # Write updated data back to the JSON file
        with open(filename, 'w') as file:
            json.dump(devices_data, file, indent=4)

    except Exception as e:
        print(f"Error writing to JSON file: {e}")

# Function to calculate total cost from the JSON file
def calculate_total_cost_from_json(filename="energy_data.json"):
    total_cost = 0
    try:
        with open(filename, 'r') as file:
            devices_data = json.load(file)
            for device in devices_data:
                print(f"{device['device']} : {device['cost']} per second")
                total_cost += device["cost"]  # Add the cost per second
    except FileNotFoundError:
        print("No data found. Start by adding some devices.")
    except Exception as e:
        print(f"Error reading from JSON file: {e}")
    
    return total_cost

# Main program
cost = None
consumption_per_hour = None

while True:
    print("\n1. Show consumption per second")
    print("2. Show consumption per hour")
    print("3. Show consumption per month")
    print("4. Calculate total cost of all devices")

    choice = input("Choose an option: ")

    if choice == '1':
        device = input("Enter device name: ")
        number_of_device = input("Enter number of this device: ")
        power_rating_watts = get_float_input("Enter the power rating of the device in watts (W): ")
        currency = input("Enter your currency: ")
        cost_per_kwh = get_float_input("Enter the cost of electricity per kilowatt-hour (kWh): ")

        # Calculate cost per second for the device
        cost = cost_of_power_consumption(power_rating_watts, cost_per_kwh)
        print(f"Using {device} costs {currency} {cost:.10f} per second.")

        # Append the data to the JSON file
        append_to_json(device, number_of_device, power_rating_watts, cost, currency)

    elif choice == '2':
        if cost:
            consumption_per_hour = cost * 3600
            print(f"Total consumption per hour: {consumption_per_hour}")
        else:
            print("You need to calculate the consumption per second first.")

    elif choice == '3':
        if consumption_per_hour:
            consumption_hours_per_day = get_float_input("Enter how many hours device is used in a day: ")
            consumption_per_month = consumption_per_hour * consumption_hours_per_day * 30
            print(f"Total consumption per month: {consumption_per_month}")
        else:
            print("You need to calculate the consumption per hour first.")

    elif choice == '4':
        total_cost = calculate_total_cost_from_json()
        print(f"Total consumption of all saved devices: {total_cost}")
    else:
        print("Invalid choice. Please select a valid option.")

