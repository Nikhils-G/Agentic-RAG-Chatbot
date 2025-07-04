# parsers/txt_parser.py

def parse_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
