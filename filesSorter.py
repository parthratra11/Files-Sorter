import os, fnmatch

# SPECIFY THE PATH OF THE DIRECTORY TO BE SORTED
myPath = r"D:\\downloads\\"

# SPECIFY THE DIVISONS AND EXTENSIONS OF THE FILES TO BE SORTED
filters = {
    'Images' : ['png', 'jpg', 'jpeg', 'svg', 'ico'],
    'Videos' : ['mp4'],
    'Applications' : ['exe', 'msi'],
    'PDFs' : ['pdf'],
    'ZIP Files' : ['zip', 'rar'],
    'Word Documents' : ['doc', 'docx'],
    'PPTs' : ['pptx'],
    'Excel Sheets' : ['xlsx', 'csv'],
    'Music' : ['mp3'],
    'Folders + Extras' : [],
}

# CREATING SUB-FOLDERS
for dirName in filters:
    try:
        os.mkdir(os.path.join(myPath, dirName))
    except:
        print('Directory already exists.')

# CREATING THE LIST OF ALL SUB-DIRECTORIES IN THE PATH SPECIFIED
listDir = os.listdir(myPath)

for dirName in filters:
    for flag in range(len(filters[dirName])):
        extension = '*.' + filters[dirName][flag]
        
        listDir = os.listdir(myPath) # REGENERATING AFTER EACH LOOP TO MAKE SURE THE LIST OF REMAINING FILES/FOLDERS IS ACCURATE

        for file in fnmatch.filter(listDir, extension):
            # RENAMING THE FILES IN ORDER TO MOVE THEM TO THEIR RESPECTIVE SUB-FOLDERS
            # os.rename(os.path.join(myPath, file), os.path.join(myPath, dirName + '\\' + file))

            src = os.path.join(myPath, file)
            dst = os.path.join(myPath, dirName, file)

            # CHECKS IF THE FILE ALREADY EXISTS OR NOT
            if os.path.exists(dst):
                print(f'File "{file}" already exists in "{dirName}". Skipping...')
            else:
                os.rename(src, dst)

# MOVING THE REMAINING SUB-DIRECTORIES INTO THE 'Folders + Extras' SUB-FOLDER
for extra in listDir:
    if extra not in filters:
        os.rename(os.path.join(myPath, extra), os.path.join(myPath, 'Folders + Extras\\' + extra))
