import os

def main():
    for root, directories, files in os.walk("C:/Users/mateo/OneDrive/Documentos/IMT NORD EUROPE/AÑO 2/Scripping course/project_1"):
        print(f"Root:{root}")
        print(f"directory: {directories}")
        print(f"File: {files}")


if __name__ == '__main__':
    main()