import hashlib
import os

current_directory = os.getcwd()
path = os.path.join(current_directory, 'Tasks\\t2\\task2')

list_of_heshes = []

for root, dirs, files in os.walk(path):
    for fn in files:
        file_path = os.path.join(path, fn)
        with open(file_path, 'rb') as f:
            data = f.read()
        hasher = hashlib.sha3_256(data)
        list_of_heshes.append(hasher.hexdigest())

list_of_heshes.sort()
hesh_text = ''.join(list_of_heshes)
# print(hesh_text)

hasher = hashlib.sha3_256(hesh_text.encode('utf-8'))
print(hasher.hexdigest())

list_of_heshes.append('vip0amirkulov@gmail.com')

hesh_text = ''.join(list_of_heshes)
hasher = hashlib.sha3_256(hesh_text.encode('utf-8'))
print(hasher.hexdigest())
# print(list_of_heshes)
