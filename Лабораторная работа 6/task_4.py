import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line='\n') -> list[dict]:
    with open(filename) as f:
        data = []
        for index, line in enumerate(f):
            value = line.strip(new_line).split(delimiter)
            if index == 0:
                column = value
                continue

            data.append({})
            for i, _ in enumerate(column):
                data[-1][column[i]] = value[i]
    return data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
