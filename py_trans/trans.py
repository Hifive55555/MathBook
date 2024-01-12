# This is a lib to translate $ to \\(
import os
import re

class Trans:
    def __init__(self, file_path, write_path):
        self.file_path = file_path
        self.write_path = write_path
        if not os.path.exists(file_path):
            raise FileNotFoundError(os.path.abspath(file_path))
        if os.path.isfile(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.origin_content = f.read()
        self.to_content = ""
        
    def transmit(self):
        def replace_inner(match):
            if match.group() == "$$":
                return "$$"
            else:
                return r'\\(' + match.group()[1:-1] + r'\\)'
        def replace_ln(match):
            return match.group()*2
        self.to_content = \
        re.sub(r'\$.*?\$', lambda match: replace_inner(match),
               re.sub(r'\\\\', lambda match: replace_ln(match), self.origin_content),
               flags=re.S)
        
    def write(self):
        with open(self.write_path, 'w', encoding='utf-8') as f:
            f.write(self.to_content)
        print(f'Suceed! {self.write_path}')
