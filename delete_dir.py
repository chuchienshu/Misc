'''
author: chuchienshu
date:   2018/6/29
@Copyright reserved.
this script is used to remove the dir that containing ONLY ONE image.
'''

import os
from os.path import isdir,join
import sys
import argparse
import shutil

def rm_dir(root_dir):
    subfiles = os.listdir(root_dir)
    if len(subfiles) == 1 and not isdir(join(root_dir, *subfiles)):
        print(join(root_dir, *subfiles), ' removed!')
        shutil.rmtree(root_dir)
        # os.remove(root_dir) #remove cannot delete dir.
    else:
        for file in subfiles:
            file_path = join(root_dir, file)  
            if isdir(file_path):
                rm_dir(file_path)

# rm_dir('/home/chuchienshu/pythonCode/tools/jkjk')

# exit()
def main(args):

    curr_dir = os.path.split(__file__)[0]

    parser = argparse.ArgumentParser()
    # Required arguments: input
    parser.add_argument(
        "--root_dir",
        '-rd',
        help="the root directory of your dataset waitting for processing."
    )
    args = parser.parse_args()

    root_dir = args.root_dir
    print('You sure you wanna remove part subdirs inside %s ? Irrevocable!!' % root_dir)
    answer = input('(Y/N):  ')
    if answer.lower() == 'y':
        rm_dir(root_dir)
        print('done!')
    else:
        print('operation canceled!')

if __name__ == "__main__":
    
    main(sys.argv)

