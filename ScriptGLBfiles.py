import json
import os


def process_json_file(file_path, excluded_traits):
    # Read the JSON file
    with open(file_path, "r") as file:
        data = json.load(file)

    # Extract values from attributes, excluding specified traits
    values = [
        attr["value"]
        for attr in data["attributes"]
        if attr["trait_type"] not in excluded_traits
    ]

    # Join values with underscore
    name = "_".join(values)

    return name


def process_folder(folder_path, excluded_traits):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            json_file_path = os.path.join(folder_path, filename)

            # Process the JSON file
            new_name = process_json_file(json_file_path, excluded_traits)

            # Construct the new .glb file path
            glb_filename = os.path.splitext(filename)[0] + ".glb"
            glb_file_path = os.path.join(folder_path, glb_filename)

            # Rename the .glb file
            os.rename(glb_file_path, os.path.join(folder_path, f"{new_name}.glb"))

            print(f"Renamed: {glb_filename} -> {new_name}.glb")


# Example usage
folder_path = r"C:\folder_path\folder_with_files"
excluded_traits = [
    "trait_that_you_want_to_exclude"
]  # Add any trait types you want to exclude
process_folder(folder_path, excluded_traits)
