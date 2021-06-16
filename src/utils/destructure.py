def destructure(dict, *keys):
    return [dict[key] if key in dict else None for key in keys]
