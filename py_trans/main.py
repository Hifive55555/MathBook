import os
# import shutil
from trans import Trans

path_root = './py_trans/src'
to_path_root = './src'

md_file_paths = []
print(os.path.abspath(path_root))
for root, dirs, files in os.walk(path_root):
    for file in files:
        if file.split('.')[-1] == 'md':
            md_file_paths.append(
                [os.path.abspath(os.path.join(root, file)),
                 os.path.abspath(to_path_root + (root.split(path_root))[1] + '\\' + file)])        

for md_file_path in md_file_paths:
    root = '\\'.join(md_file_path[1].split('\\')[:-1])
    if not os.path.exists(root):
        os.makedirs(root)
    else:
        for file_name in os.listdir(root):
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)

for md_file_path in md_file_paths:
    t = Trans(md_file_path[0], md_file_path[1])
    t.transmit()
    t.write()
