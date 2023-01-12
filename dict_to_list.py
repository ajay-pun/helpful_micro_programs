def dict_to_list(dictionary):
    get_data=lambda key:dictionary[key]
    return list(map(get_data,dictionary))
