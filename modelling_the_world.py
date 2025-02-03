# Define a simple frame-based representation of a smart home

smart_home = {
    "living_room": {
        "lights": {
            "state": "off",
            "actions": ["turn_on", "turn_off"]
        },
        "thermostat": {
            "temperature": 22,  # in Celsius
            "actions": ["set_temperature"]
        },
        "smart_tv": {
            "state": "off",
            "actions": ["turn_on", "turn_off", "change_channel"]
        }
    },
    "kitchen": {
        "coffee_maker": {
            "state": "idle",
            "actions": ["brew_coffee", "stop"]
        },
        "fridge": {
            "temperature": 4,  # in Celsius
            "actions": ["set_temperature"]
        }
    }
}

def perform_action(room, device, action, **kwargs):
    if room in smart_home and device in smart_home[room]:
        if action in smart_home[room][device]["actions"]:
            # Example: handle turning lights on/off
            if action == "turn_on":
                smart_home[room][device]["state"] = "on"
                print(f"{device} in {room} is now on.")
            elif action == "turn_off":
                smart_home[room][device]["state"] = "off"
                print(f"{device} in {room} is now off.")
            elif action == "set_temperature":
                if "temperature" in kwargs:
                    smart_home[room][device]["temperature"] = kwargs["temperature"]
                    print(f"{device} in {room} set to {kwargs['temperature']}°C.")
            elif action == "change_channel":
                if "channel" in kwargs:
                    smart_home[room][device]["channel"] = kwargs["channel"]
                    print(f"{device} in {room} changed to channel {kwargs['channel']}.")
            elif action == "brew_coffee":
                smart_home[room][device]["state"] = "brewing"
                print("Coffee is brewing.")
            elif action == "stop":
                smart_home[room][device]["state"] = "idle"
                print("Coffee maker stopped.")
        else:
            print("Action not available for this device.")
    else:
        print("Device or room not found.")

# Example usage:
perform_action("living_room", "lights", "turn_on")
perform_action("living_room", "thermostat", "set_temperature", temperature=20)
