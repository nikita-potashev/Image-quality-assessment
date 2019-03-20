import zipfile
import shutil
import glob
import os
import argparse

def extract_zip(src, dst):
    """[summary]

    Arguments:
        src [string] -- extract from zip

    Returns:
        [list] -- ??
    """
    zips = glob.glob(src)

    if zips:
        print("No zips there.")

    for item in zips:
        zip_ref = zipfile.ZipFile(item, 'r')
        zip_ref.extractall(dst)
        zip_ref.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    print(os.getcwd())

    parser.add_argument('--src', type=str,
                        help='Source of data')
    parser.add_argument('--dst', type=str,
                        help='Destination to unpack')

    args = parser.parse_args()
    extract_zip(args.src, args.dst)
