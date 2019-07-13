# TODOTaskList

#Install python
brew install python3

# Test if python is installed
python3

# Install pip
easy_install pip

# Install Virtual Environment - Optional
python3 -m pip install --user virtualenv

# Create Virtual Environment - Optional
python3 -m virtualenv env

# Activate virtual Environment - Optional
source env/bin/activate

# Install requirements - Optional
pip install -r requirement.txt

# Run application using
python main.py <path of folder> <String to be searched> <file extension to be checked for> <exclude dir list>

# File extention
file extension to be checked for can be any, likle '*.js' or *.py etc depending on type of folder syetem we are testing
Leave empty if you don't want to exclude any filr type.
Make sure if any wildcard is being used put that as as string, else command prompt will try to resolve the wildcard.

# Exclude folders
Depending on type of folder, if its JS 'nodel_module' will be geenrated folder on local similary if its python app, environment folder will be generated. in order to exclude those folders, define the folder names as last argument
Leave as empty if no folder is to be left.
In order to add more then one folder put as a comma seperated string e.g,
'test_folder, main_folder'

# Running examples
python main.py ./ TODO '*.py' 'test_folder, main_folder'
python main.py ./ TODO
python main.py ./ TODO '*.py'
python main.py ./ TODO '*.py' 'test_folder'