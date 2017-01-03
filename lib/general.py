import os


# create directory if doesnt exist
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# write to file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
