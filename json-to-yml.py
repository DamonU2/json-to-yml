import json
import sys
import yaml


# Function to convert .json file to .yml file
def convert_to_yaml(filename: str):
    if filename[-5:] != '.json':
        print('Not a valid .json file')
    else:
        yaml_filename = filename[:-4] + 'yml'
        with open(filename, 'r') as f:
            yaml_data = yaml.dump(json.load(f))
            with open(yaml_filename, 'w') as g:
                g.write(yaml_data)


# To run directly - python json-to-yml.py /path/to/filename.json
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Provide path to .json file as only argument')
    else:
        convert_to_yaml(sys.argv[1])