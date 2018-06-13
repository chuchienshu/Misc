import os  
import argparse

'''
def listdir(path, list_name):  
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        else:  
            list_name.append(file_path)  
    return sorted(list_name)
'''
def listdir(path, out_file):  
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, out_file)  
        else:  
            out_file.write('%s\n' % file_path)  

def main(args):

    # curr_dir, filename = os.path.abspath(__file__)
    curr_dir = os.path.split(__file__)[0]

    parser = argparse.ArgumentParser()
    # Required arguments: input and output.
    parser.add_argument(
        "--root_dir",
        '-rd',
        help="the root directory of your file including all subfolds."
    )
    parser.add_argument(
        "--output_file",
        '-o',
        help="name the output file.eg. ***.txt"
    )
    args = parser.parse_args()

    root_dir = args.root_dir
    output_file = args.output_file

    out_file = open('%s/%s' % (curr_dir, output_file), 'a')
    listdir(root_dir, out_file)
    print('done!')


if __name__ == "__main__":
    import sys
    main(sys.argv)
