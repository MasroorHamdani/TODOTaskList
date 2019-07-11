import sys, os
from fnmatch import fnmatch

def main():
    folder_path = sys.argv[1]
    search_string = sys.argv[2]
    pattern = sys.argv[3] if len(sys.argv) >= 4 else '*.js'
    exclude = sys.argv[4] if len(sys.argv) == 5 else []

    findFileContent(folder_path, pattern, search_string, exclude)

def findFileContent(folder_path, pattern, search_string, exclude):
    """
    Function to go through all the files in the directory given
    and look for the word to be searched
    """
    for path, subdirs, files in os.walk(folder_path):
        subdirs[:] = [d for d in subdirs if d not in exclude]
        for name in files:
            if fnmatch(name, pattern):
                if os.path.isfile(os.path.join(path, name)):
                    f = open(os.path.join(path, name), 'r')
                    if search_string in f.read():
                        print('found string in file %s' % os.path.join(path, name))
                    f.close()

if __name__ == "__main__":
    main()