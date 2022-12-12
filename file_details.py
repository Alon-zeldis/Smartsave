import os

# The function returns a list of [file name, date of creation, the full path]


def file_dits():
    dir_name = 'C:\\Users\\zeldi\\Downloads'
    valid_path = 0
    while not valid_path:
        count = 0
        list_of_invalid_files = filter(lambda x: os.path.join(dir_name, x).endswith(('.crdownload', '.tmp')),
                                          os.listdir(dir_name))
        for file in list_of_invalid_files:
            count += 1
        if count == 0:
            valid_path = 1
    list_of_files = filter(lambda x: os.path.isfile(os.path.join(dir_name, x)),
                            os.listdir(dir_name))
    list_of_files = sorted(list_of_files,
                            key=lambda x: os.path.getmtime(os.path.join(dir_name, x)), reverse=True)

    file_path = os.path.join(dir_name, list_of_files[0])
    file_size = os.stat(file_path).st_size
    return [list_of_files[0], file_size, file_path]
