import zipfile
import shutil
import glob
import os


def extract_zip(path, new_path):
    """[summary]

    Arguments:
        path [string] -- extract from zip

    Returns:
        [list] -- ??
    """
    zips = glob.glob(path)

    if len(zips) == 0:
        print("No zips there.")

    for item in zips:
        zip_ref = zipfile.ZipFile(item, 'r')
        zip_ref.extractall(new_path)
        zip_ref.close()


if __name__ == "__main__":
    print(os.getcwd())
    extract_zip('data/blur/*.zip', 'data/blur/train/')

