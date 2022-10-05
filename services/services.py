from flask import Flask, request

from utils.clean_utils import clean_json_duplicates, clean_list_duplicates

app = Flask("")


@app.route("/clean_input", methods=["POST"])
def clean_input():
    input_value = request.json.get("value")
    args = request.json.get('args')
    data_type = args.get('data_type')

    if args == {} or data_type==None:
        raise Exception("Can't start flow - ERROR: Cleaner, missing required argumens'")

    match data_type:
        case 'JSON':
            key = args.get('key', None)
            ignore_err = args.get('ignore_err', False)
            result = clean_json_duplicates(key, input_value, ignore_err)
        case 'List':
            result = clean_list_duplicates(input_value)

    return result


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
