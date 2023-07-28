import os
import json

def set_user_config(user_config_path: str, **kwargs):
    # Check if the file exists and is a file
    if not os.path.isfile(user_config_path):
        print(f"Invalid file path: {user_config_path}")
        return

    try:
        # Load the existing config
        with open(user_config_path, "r") as f:
            user_config = json.load(f)

        # Update the config with the provided kwargs
        user_config.update(kwargs)

        # Save the updated config
        with open(user_config_path, "w") as f:
            json.dump(user_config, f, indent=4)

        print(f"User config updated successfully")

    except Exception as e:
        print(f"Failed to update user config. Error: {str(e)}")
