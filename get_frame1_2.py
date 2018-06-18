import os  
import argparse
# import natsort
'''
author: chuchienshu
date:	2018/6/18
copyright reserved.
usage:	this script is used to create .txt file that including two sequence frame each line.
'''
def frame(path, list_name, is_dir=True, del_f=0):  
    '''
    this function is used to get the list of the frame 2 in a two order dir.
    '''
    fil_lis = sorted(os.listdir(path))
    if not is_dir:
        del fil_lis[del_f]
    for file in fil_lis:  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
                
            frame(file_path, list_name, is_dir=False, del_f=del_f)  
        else:  
            list_name.append(file_path)  
    list_name = sorted(list_name)
    return list_name

def main(args):

    curr_dir =  os.path.split(os.path.abspath(__file__) )[0]
    # curr_dir = os.path.split(__file__)[0]

    # print(curr_dir)

    parser = argparse.ArgumentParser()
    # Required arguments: input and output.
    parser.add_argument(
        "--root_dir",
        '-rd',
        help="the root directory of your file including all subfolders."
    )
    parser.add_argument(
        "--output_file",
        '-o',
        help="name the output file.eg. ***.txt"
    )
    args = parser.parse_args()

    root_dir = args.root_dir
    output_file = args.output_file

    f1 = frame(root_dir, [], del_f=-1)
    f2 = frame(root_dir, [])

    with open('%s/%s' % (curr_dir, output_file), 'a') as f:
        for f1_, f2_ in zip(f1,f2):
            f.write('%s %s\n' % (f1_, f2_))

    print('saved %s/%s!' % (curr_dir, output_file))


if __name__ == "__main__":
    import sys
    main(sys.argv)
