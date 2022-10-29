import os
import time

# The function returns a list of [file name, date of creation, the full path]


def file_dits():
    dir_name = 'C:\\Users\\zeldi\\Downloads'
    list_of_files = filter(lambda x: os.path.isfile(os.path.join(dir_name, x)),
                            os.listdir(dir_name) )

    list_of_files = sorted( list_of_files,
                            key=lambda x: os.path.getmtime(os.path.join(dir_name, x)), reverse=True
                            )

    file_path = os.path.join(dir_name, list_of_files[0])
    timestamp_str = time.strftime('%m/%d/%Y :: %H:%M:%S', time.gmtime(os.path.getmtime(file_path)))
    return [list_of_files[0], timestamp_str, file_path]

