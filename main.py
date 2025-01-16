import os

def main():
    for root, directories, files in os.walk("C:/Users/mateo/OneDrive/Documentos/IMT NORD EUROPE/AÑO 2/Scripping course/project_1"):
       # print(f"Root:{root}")
       # print(f"directory: {directories}")
       # print(f"File: {files}")
        for _file in files:
            absolute_path = os.path.join(root, _file)
            print(f"File path: {absolute_path}")


if __name__ == '__main__':
    main()