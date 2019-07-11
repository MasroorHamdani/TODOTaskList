# TODOTaskList

#Install python
brew install python3

# Test if python is installed
python3

# Install pip
easy_install pip

# Install Virtual Environment
python3 -m pip install --user virtualenv

# Create Virtual Environment
python3 -m virtualenv env

# Activate virtual Environment
source env/bin/activate

# Install requirements
pip install -r requirement.txt

# Run application using
python main.py <path of folder> <String to be searched> <file extension> <exclude list>

# Changes to be made in order to use any extention
findFileContent(folder_path, '*.js', search_string) // change '*.js' to any file extention format you have to validate

# Exclude folders
Depending on type of folder, if its JS nodel_module will be geenrated folder on local similary if its python app, environment folder will eb generated. in order to exclude those folders, define the folder names in below folder
exclude = ['node_modules']

Leave as empty if no folder is to be left