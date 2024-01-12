import os
from trans import Trans

path_root = './py_trans/pure_ideas'
to_path_root = './src/pure_ideas'

md_file_paths = []
print(os.path.abspath(path_root))
for root, dirs, files in os.walk(path_root):
    for file in files:
        if file.split('.')[-1] == 'md':
            md_file_paths.append(
                [os.path.abspath(os.path.join(root, file)),
                 os.path.abspath(to_path_root + (root.split(path_root))[1] + '\\' + file)])

# print(md_file_paths)            

for md_file_path in md_file_paths:
    if not os.path.exists('\\'.join(md_file_path[1].split('\\')[:-1])):
        os.makedirs('\\'.join(md_file_path[1].split('\\')[:-1]))
    t = Trans(md_file_path[0], md_file_path[1])
    t.transmit()
    t.write()
