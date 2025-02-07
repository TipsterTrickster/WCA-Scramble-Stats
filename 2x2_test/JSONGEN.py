import os
import json

def scan_directory(directory):
    """
    Recursively scans a directory and returns its structure as a dictionary.
    """
    structure = {}
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            # If it's a directory, recursively scan it
            structure[item] = scan_directory(item_path)
        elif os.path.isfile(item_path) and item.endswith('.csv'):
            # If it's a CSV file, add it to the structure
            structure[item] = None
    return structure

def save_structure_to_json(structure, output_file):
    """
    Saves the folder structure dictionary to a JSON file.
    """
    with open(output_file, 'w') as f:
        json.dump(structure, f, indent=4)

def main():
    # Define the root directory to scan
    root_directory = '.'  # Current directory (change this if needed)
    
    # Define the output JSON file
    output_file = 'folder-structure.json'
    
    # Scan the directory and generate the structure
    structure = scan_directory(root_directory)
    
    # Save the structure to a JSON file
    save_structure_to_json(structure, output_file)
    
    print(f"Folder structure saved to {output_file}")

if __name__ == '__main__':
    main()