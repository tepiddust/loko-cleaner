import dpath.util


def reshape_nested_key(key: str, shape_back=False):
    if not shape_back:
        if "." in key:
            key = "/".join(key.split("."))

    else:
        if "/" in key:
            key = ".".join(key.split("/"))
    return str(key)


def clean_json_duplicates(search_key, data, ignore_err=False):
    unique = []
    if search_key:
        search_key = reshape_nested_key(search_key)
        for sub_data in data:
            try:
                if all(dpath.util.get(obj=unique_entries, separator="/", glob=search_key) != \
                        dpath.util.get(obj=sub_data, separator="/", glob=search_key)for unique_entries in unique):
                    unique.append(sub_data)
            except Exception as e:
                if not ignore_err:
                    raise e
                else:
                    unique.append(sub_data)
        return unique
    else:
        return data


def clean_primitive_duplicates(data):
    unique = []
    [unique.append(x) for x in data if x not in unique]
    return [unique]
