def get_column_list(table,column_index):
    get_column_item=lambda row:row[column_index]
    return list(map(get_column_item,table))
