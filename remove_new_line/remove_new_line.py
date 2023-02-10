def main():
    with open("tools/text_in.txt", "r") as f:
        txt = f.read()
    txt = txt.replace("\n", " ").replace("", "")
    with open("tools/text_in.txt", "w") as f:
        f.write(txt)
    
if "__main__" == __name__:
    main()