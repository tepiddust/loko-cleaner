from flask import Flask, request

from utils.clean_utils import clean_json_duplicates, clean_primitive_duplicates, replace_empty_values, validate_json

app = Flask("")


@app.route("/clean_input", methods=["POST"])
def clean_input():
    input_value = request.json.get("value")
    args = request.json.get('args')

    if args == {}:
        raise Exception("Can't start flow - ERROR: Cleaner, missing required arguments'")

    remove_duplicates = args.get('remove_duplicates', False)
    replace_null = args.get('replace_null', False)
    output_as_a_list = args.get('output_as_a_list', False)

    if isinstance(input_value, list):
        data_type = 'JSON'
        for item in input_value:
            if not isinstance(item, dict):
                data_type = 'Primitive'
    elif validate_json(input_value) or isinstance(input_value, dict):
        data_type = 'JSON'
    else:
        raise ValueError('Unsupported input data')

    print("DATATYPE", data_type)
    result = input_value

    match data_type:
        case 'JSON':
            if remove_duplicates:
                key = args.get('key', None)
                ignore_err = args.get('ignore_err', False)
                result = clean_json_duplicates(key, result, ignore_err)
            if replace_null:
                replacing_text = args.get('replacing_text')
                result = replace_empty_values(result, replacing_text)
        case 'Primitive':
            if remove_duplicates:
                result = clean_primitive_duplicates(result)
            if replace_null:
                replacing_text = args.get('replacing_text', 'placeholder empty value')
                result = replace_empty_values(result, replacing_text)

    if output_as_a_list:
        return [result]
    else:
        return result


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
