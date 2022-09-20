import os

path = "/Proyectos/Spacy-NER/data"

os.chdir(path)


def read_text_file(file_path):
    list_text = []
    with open(file_path, "r") as f:
        list_text.append(f.read())

    with open("/Proyectos/Spacy-NER/train.txt", "a") as f:
        f.write(str(list_text[0]))
        f.write("\n")
        f.write("---")
        f.write("\n")


for file in os.listdir():

    if file.endswith(".txt"):
        file_path = path + "/" + file
        read_text_file(file_path)
