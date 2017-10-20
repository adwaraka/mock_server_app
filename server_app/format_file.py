MAX_SIZE = 40

class FileFormat:
    def __init__(self):
        pass

    def format_file(self):
        global MAX_SIZE
        array_line = []
        line_printed = ""

        with open("file.txt", "rb") as f:
            for line in f:
                array_line.append(line)
        entire_text = " ".join(array_line)
        list_of_words = entire_text.split(" ")

        paragraph = []
        for i in list_of_words:
            if len(list(line_printed)) + len(list(i)) + 1 <= MAX_SIZE:
                i = i.strip()
                i+=" "
                line_printed+=i
            else:
                paragraph.append(line_printed)
                line_printed = i.strip() + " "
        return paragraph

if __name__ == "__main__":
    f = FileFormat()
    print f.format_file()
