filename = r'C:\Users\forte\Desktop\Beetroot_course\Tasks\Files_I-O_ContextManagers_JSON\myfile.txt'
def funct():
    with open(filename, 'r') as file:
        content = file.read()
    print(content)

funct()