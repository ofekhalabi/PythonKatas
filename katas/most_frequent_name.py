def most_frequent_name(file_path):
    """
    Receives a path to a file containing names (name in each line)
    The function should return the most frequent name in the file.

    You can assume file_path exists in the file system.
    """
    with open(file_path,mode= 'r') as file:
        name_list = file.read().splitlines()
        name_count = {}
        for name in name_list:
            if name in name_count:
                name_count[name] += 1
            else:
                name_count[name] = 1
        max_high = max(name_count,key=name_count.get)
        return max_high



if __name__ == '__main__':
    print(most_frequent_name('files/names.txt'))
