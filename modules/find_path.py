import os 

def find_path(filename):
    path_file = __file__
    path_file = path_file.split("\\")
    del path_file[-1]
    del path_file[-1]
    path_file = "\\".join(path_file)
    path_file = os.path.join(path_file, filename)
    return path_file