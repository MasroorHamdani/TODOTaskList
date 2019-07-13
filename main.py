import sys, os
from fnmatch import fnmatch

#TODO - For Test cases

def main():
    folder_path = sys.argv[1] if len(sys.argv) >= 2 else ''
    search_string = sys.argv[2] if len(sys.argv) >= 3 else ''
    pattern = sys.argv[3] if len(sys.argv) >= 4 else '*.py'
    exclude = sys.argv[4] if len(sys.argv) == 5 else []
    return findFileContent(folder_path, search_string, pattern, exclude)

def findFileContent(folder_path, search_string, pattern, exclude):
    """
    Function to go through all the files in the directory given
    and look for the word to be searched
    """
    result = []
    for path, subdirs, files in os.walk(folder_path):
        subdirs[:] = [d for d in subdirs if d not in exclude]
        for name in files:
            if fnmatch(name, pattern):
                if os.path.isfile(os.path.join(path, name)):
                    f = open(os.path.join(path, name), 'r')
                    if search_string in f.read():
                        result.append(os.path.join(path, name))
                    f.close()
    return result

if __name__ == "__main__":
    print(main())