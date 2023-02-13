FILE_PATH = "tools/remove_new_line/text_in.txt"

def main():
    print("Runing... ", end="")
    with open(FILE_PATH, "r") as f:
        txt = f.read()
    txt = txt.replace("\n", " ").replace("", "")
    with open(FILE_PATH, "w") as f:
        f.write(txt)
    print("Done.")
    
if "__main__" == __name__:
    main()