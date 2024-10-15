from katas.total_expense import expenses


def file_exceptions(file_path, op='r'):
    """
    Replaces ' ' by '_' in the given file_path.

    You have to except the MOST SPECIFIC exception and print an informative message for ALL potential file-related exceptions.
    The message must contain the exception name, e.g. RuntimeError, ZeroDivisionError, ...
    """
    try:
        with open(file_path, op) as file:
            content = file.read()
            content_modified = content.replace(' ', '_')
            return content_modified
    except FileNotFoundError:
        return print ("FileNotFoundError: the file is not exist")
    except IsADirectoryError:
        return print ("IsADirectoryError: the file trying open is a directory")
    except FileExistsError:
        return print ("FileExistsError: already exists")
    except PermissionError:
        return print ("PermissionError: you dont have permission")

if __name__ == '__main__':
    print(file_exceptions('files/nonexistent_file.txt'))
    print(file_exceptions('files/somefile'))
    print(file_exceptions('files/'))
    print(file_exceptions('files/someotherfile', op='x'))
    print(file_exceptions('files/someotherfile'))

