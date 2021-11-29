def to_bool(val):

    valid = {
        "True": True,
        "true": True,
        "1": True,
        "False": False,
        "false": False,
        "0": False
    }

    if val in valid:
        return valid[val]
    else:
        return None