from pathlib import Path
import unicodedata
import string
from collections import namedtuple

class NameDataset():
    all_letters = string.ascii_letters + " .,;'"
    n_letters = len(all_letters)

    def __init__(self, root):
        self.annotations = []
        Annotation = namedtuple('Annotation', ['language', 'name'])
        for txt_file in Path(root).rglob('*.txt'):
            names = readlines(str(txt_file))
            for name in names:
                annotation = Annotation(txt_file.stem, name)
                self.annotations.append(annotation)
            
    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        language, name = self.annotations[index]
        self.all_letters.find 
        return language, name
        
def readlines(filename):
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    return [unicode_to_ascii(line) for line in lines]


def unicode_to_ascii(unicode_string):
    return ''.join(
    c for c in unicodedata.normalize('NFD', unicode_string)
    if unicodedata.category(c) != 'Mn'
    and c in all_letters
)