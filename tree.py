# import os
# def tree_printer(root):
#     for root, dirs, files in os.walk(root):
#         for d in dirs:
#             print (os.path.join(root, d))
#         for f in files:
#             print (os.path.join(root, f))
# tree_printer('.')

import os
import sys


def tree_view(path_directory, recurse_depth = 0):
    if recurse_depth< 1:
      print("Parent_directory:",path_directory)
    for files in os.listdir(path_directory):
        path = os.path.join(path_directory,files)
        direcrry_exist = os.path.isdir(path)
        if not direcrry_exist:
            print("\t"* recurse_depth, files)

        else:
            print("\t"*recurse_depth + "directory level {}:".format(recurse_depth), files)
            tree_view(path,recurse_depth = recurse_depth + 1)
#
# recurse_dir (sys.argv[1])

tree_view(path_directory=input("enter the path"))
