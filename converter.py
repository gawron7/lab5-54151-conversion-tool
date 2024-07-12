import argparse
import json
import yaml
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description='Converter for XML, JSON, and YAML formats')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    return parser.parse_args()

def read_json(file):
    with open(file, 'r') as f:
        return json.load(f)

def write_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def read_yaml(file):
    with open(file, 'r') as f:
        return yaml.safe_load(f)

def write_yaml(data, file):
    with open(file, 'w') as f:
        yaml.dump(data, f)

def read_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    return root

def write_xml(root, file):
    tree = ET.ElementTree(root)
    tree.write(file)

def convert(input_file, output_file):
    if input_file.endswith('.json'):
        data = read_json(input_file)
        if output_file.endswith('.yaml'):
            write_yaml(data, output_file)
        elif output_file.endswith('.xml'):
            write_xml(data, output_file)
    elif input_file.endswith('.yaml'):
        data = read_yaml(input_file)
        if output_file.endswith('.json'):
            write_json(data, output_file)
        elif output_file.endswith('.xml'):
            write_xml(data, output_file)
    elif input_file.endswith('.xml'):
        root = read_xml(input_file)
        if output_file.endswith('.json'):
            data = {child.tag: child.text for child in root}
            write_json(data, output_file)
        elif output_file.endswith('.yaml'):
            data = {child.tag: child.text for child in root}
            write_yaml(data, output_file)

if __name__ == '__main__':
    args = parse_arguments()
    convert(args.input_file, args.output_file)
