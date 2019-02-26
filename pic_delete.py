import sys
import os

def main():
    if len(sys.argv) != 2:
        print("You gave " + str(len(sys.argv)-1) + " arguments instead of only one")
    else:
        print("ok.")
    if not os.path.exists(sys.argv[1]):
        print("Path does not exist. :(")
        return False
    dir_path = os.path.realpath(sys.argv[1])
    print(dir_path)
    files = [file for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file))]
    print(str(len(files)) + " files detected.")
    files.sort()
    print(files)

    



if __name__ == "__main__":
    main()
