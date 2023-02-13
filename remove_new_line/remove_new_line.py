FILE_PATH = "remove_new_line/text_in.txt"

def main():
    print("Runing... ", end="")
    
    try:
        with open(FILE_PATH, "r") as f:
            txt = f.read()
    except FileNotFoundError:
        print("Created text file.")
        f = open(FILE_PATH, "w")
        f.close()
        return
    txt = txt.replace("\n", " ").replace("", "")
    with open(FILE_PATH, "w") as f:
        f.write(txt)
    print("Done.")
    
if "__main__" == __name__:
    main()