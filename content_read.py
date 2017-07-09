import os
import re

# the return value should look like this:
# content(list):
#     0(dict):
#         package_name
#         cover_file_name
#         author and created year
#         tags


def dir_read(target):
    last_path = os.getcwd()
    content = []
    path = './static/'+target
    os.chdir(path)
    packages = os.listdir()
    for package in packages:
        sub_path = './' + package
        os.chdir(sub_path)
        package_content = os.listdir()
        description = dict()
        description['package_name'] = package
        for file in package_content:
            if re.match(re.compile('^(cover).*(.jpg|.jpeg|.png)$'), file):
                description['cover_file_name'] = file
            if re.match(re.compile('.*(.txt)$'), file):
                f = open(file, encoding='UTF-8')
                description_content = f.readline()
                description['author'] = description_content
                description_content = f.readline()
                description['tags'] = description_content
                f.close()
        os.chdir('..')
        content.append(description)
    os.chdir(last_path)
    return content



