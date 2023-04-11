from docx import Document
import re

def execute():
    pageNumberRegex = "\d{1,2}$"
    curr_paragraph = ""
    with open("/Users/divij/Desktop/ClarityForUPSC/python_files/file.txt", "+r", encoding="utf-8") as f:
        for curr_line in f.readlines():
            if (curr_line.find("DELHI | JAIPUR | PUNE") != -1 or curr_line.lower().find("vision ias") != -1):
                continue
            elif (re.match(pageNumberRegex, curr_line.strip("")) != None):
                curr_paragraph += "\n(PAGE_BREAK)\n"
                continue
            elif (re.match("(\d\.){1,5}\d?", curr_line)):
                curr_paragraph += "\n\n"
            elif (curr_line.startswith("\u2022 ") or curr_line.startswith("•") or curr_line.startswith("o ")):
                curr_paragraph += "(BULLET_START)" + ">>" + curr_line[1:]
                continue

            curr_paragraph += curr_line

    with open("writable_file.txt", "+w", encoding="utf-8") as out_f:
        out_f.write(curr_paragraph)





    
    
    
    
    