import json


def load_data(filepath):
    with open(filepath) as json_file:
        json_data = json.load(json_file)
    return json_data


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    path_to_json = input("Enter the path to your json file: \n")
    json_file = load_data(path_to_json)
    pretty_print_json(json_file)
