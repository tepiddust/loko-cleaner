import json
import dpath.util


def reshape_nested_key(key: str, shape_back=False):
    if not shape_back:
        if "." in key:
            key = "/".join(key.split("."))

    else:
        if "/" in key:
            key = ".".join(key.split("/"))
    return str(key)


def validate_json(json_data):
    try:
        json.loads(json_data)
    except Exception as e:
        return False
    return True


def clean_json_duplicates(search_key, data, ignore_err=False):
    unique = []
    if search_key:
        search_key = reshape_nested_key(search_key)
        if isinstance(data, list):
            for sub_data in data:
                try:
                    if all(dpath.util.get(obj=unique_entries, separator="/", glob=search_key) !=
                           dpath.util.get(obj=sub_data, separator="/", glob=search_key) for unique_entries in unique):
                        unique.append(sub_data)
                except Exception as e:
                    if not ignore_err:
                        raise e
                    else:
                        unique.append(sub_data)
            return unique
        else:
            raise Exception("The input must be a list of JSON objects")
    else:
        return data


def clean_primitive_duplicates(data):
    unique = []
    [unique.append(x) for x in data if x not in unique]
    return [unique]


def replace_empty_values(data, replacing_text):
    if replacing_text:
        if isinstance(data, list):
            for index in range(len(data)):
                if not isinstance(data[index], dict) and (data[index] is None or not data[index]):
                    data[index] = replacing_text
                elif isinstance(data[index], dict) or isinstance(data[index], list):
                    replace_empty_values(data[index], replacing_text)
        else:
            for key, value in data.items():
                if isinstance(value, str):
                    if value is None or not value:
                        data[key] = replacing_text
                    elif isinstance(value, list):
                        data[key] = [replacing_text if v is None or not v else v for v in value]
                if isinstance(value, dict):
                    replace_empty_values(value, replacing_text)
                elif isinstance(value, list):
                    for val in value:
                        if not isinstance(val, str) and not isinstance(val, list):
                            replace_empty_values(val, replacing_text)
        return data
