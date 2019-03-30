def group_by_owners(files):
    output = {}
    for key, value in files.items():
        if (output.get(value) != None): # there is already
            output[value].append(key)
        else:
            output[value] = [key]

    return output

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

files2 = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy',
    'Game.py': 'Stan',
    'Test.py': 'Randy'
}

# Should return:
# {
#     'Randy': ['Input.txt', 'Output.txt'],
#     'Stan': ['Code.py']
# }

print(group_by_owners(files))
print(group_by_owners(files2))