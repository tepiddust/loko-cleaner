import json

from flask import Flask, request

from utils.clean_utils import clean_json_duplicates, clean_primitive_duplicates

app = Flask("")


@app.route("/clean_input", methods=["POST"])
def clean_input():
    input_value = request.json.get("value")
    args = request.json.get('args')
    data_type = ""

    if args == {}:
        raise Exception("Can't start flow - ERROR: Cleaner, missing required argumens'")

    remove_duplicates = args.get('remove_duplicates')
    replace_null = args.get('replace_null')

    if isinstance(input_value, list):
        data_type = 'JSON'
        for item in input_value:
            if not isinstance(item, dict):
                data_type = 'Primitive'
    else:
        raise ValueError('Unsupported input data')

    print("DATATYPE", data_type)

    match data_type:
        case 'JSON':
            if remove_duplicates:
                key = args.get('key', None)
                ignore_err = args.get('ignore_err', False)
                result = clean_json_duplicates(key, input_value, ignore_err)
            if replace_null:
                replacing_text = args.get('replacing_text')
                #TODO funzione replace
        case 'Primitive':
            if remove_duplicates:
                result = clean_primitive_duplicates(input_value)
            if replace_null:
                replacing_text = args.get('replacing_text')
                #TODO funzione replace
    return result


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
