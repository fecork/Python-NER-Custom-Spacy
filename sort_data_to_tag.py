from dataclasses import replace
import os
import re

path = "/Proyectos/Spacy-NER/Python-NER-Custom-Spacy/data/"

os.chdir(path)


def read_text_file(file_path):
    list_text = []
    with open(file_path, "r") as f:
        list_text.append(f.read())

    with open("/Proyectos/Spacy-NER/train.txt", "a") as f:
        texto = str(list_text[0])
        texto = format_text(texto)
        f.write(texto)
        f.write("\n")
        f.write("---")
        f.write("\n")


def format_text(text: str) -> str:
    """Preprocesses the data text, clean it.

    Args:
        text: String Raw data.
    Returns:
        Preprocessed data text, without stranger character.
    """

    text = text.replace(str("\\n"), "\n")
    text = text.replace(str("/"), " ")
    text = re.sub(r"[^a-zA-Z0-9\s\n.,;]", "", text)
    return text


for file in os.listdir():

    if file.endswith(".txt"):
        file_path = path + "/" + file
        read_text_file(file_path)
