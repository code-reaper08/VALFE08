import os
import pathlib
from zipfile import ZipFile
import tarfile

def zipdir():
    directory = grabdir()
    with ZipFile("specimen.zip", mode="w") as archive:
        for file_path in directory.iterdir():
            archive.write(file_path, arcname=file_path.name)
    print("archived specimen successfully!")
    directory = grabdir()
    for file_path in directory.iterdir():
        os.remove(file_path)
    os.rmdir('specimen/')

def tardir():
    # with tarfile.open("specimen.tar.gz", "w:gz") as th:
    #     for root,dirs,files in os.walk("specimen/"):
    #         for f in files:
    #             th.add(os.path.join(root,f))
    #     th.close()
    archive = tarfile.open("specimen.tar.gz", "w:gz")
    archive.add("specimen/", arcname="")
    print("archived specimen successfully!")
    directory = grabdir()
    for file_path in directory.iterdir():
        os.remove(file_path)
    os.rmdir('specimen/')

def untardir():
    tarObj = tarfile.open('specimen.tar.gz')
    # tarObj.extract("specimen/","specimen")
    tarObj.extractall("specimen")
    tarObj.close()

def checkoktozip():
    count_valid = 0
    with os.scandir("specimen") as entries:
        for entry in entries:
            if entry.is_file():
                count_valid += 1
    if count_valid == 7:
        if not os.path.isdir(os.getcwd()+"specimen.tar.gz"):
            # zipdir()
            tardir()
        else:
            print("Archive already created!")
    else:
        print("Something's corrupted try again by deleting the existing archive!")

def grabdir():
    directory = pathlib.Path("specimen/")
    return directory

def unziparchive(path_to_zip_archive, path_to_unzipped_archive):
    # with ZipFile(path_to_zip_archive, 'r') as zo:
    #     zo.extractall(path=path_to_unzipped_archive)
    ZipFile(path_to_zip_archive).extractall(path_to_unzipped_archive)
