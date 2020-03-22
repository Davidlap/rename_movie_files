import os
import shutil
import argparse


def _parse_arguments():
    parser = argparse.ArgumentParser(description='Process configuration needed')

    parser.add_argument('path',  help='Path to the folder', type=str, metavar='path')
    parser.add_argument('-r',  help='Regular expresion to split the directory name', default=' [', type=str, metavar='')
    parser.add_argument('-e', help='Movie file extensions', default=['.avi', '.mkv', '.mp4'], action='append', metavar='')
    args = parser.parse_args()

    return args


def main():

    args = vars(_parse_arguments())

    directory_path = args['path']
    file_extensions = args['e']
    split_part = args['r']
    
    if(os.path.isdir(directory_path)):
        for directory, subdirectory, files in os.walk(directory_path): 
            title_from_folder = obtain_movie_title(directory, split_part)
            if title_from_folder != '':
                rename_movie_file(file_extensions, directory, title_from_folder, files)
            else:
                print('Not able to sanitize ' + directory)
    else:
        print("Path is not correctly defined")
   
    
 

def obtain_movie_title(directory, split_part):
    
    # Split the full directory and get the last part
    try:
        movie_name = directory.split(os.path.sep)[-1].replace(".", " ")
        # Split the name by the expression given by user
        movie_name = movie_name.split(split_part)
        return movie_name[0]
    except Exception:
        return ''
        
def rename_movie_file(valid_file_extensions, directory, title_from_folder, files):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension in valid_file_extensions:
            try:
                print('Renaming ' +  file + ' --> With this name ' +  title_from_folder + file_extension)
                shutil.move(os.path.join(directory, file),os.path.join(directory, title_from_folder + file_extension))
            except Exception:
                print('Error renaming this file ' + file + ' --> With this name ' +  title_from_folder + file_extension)
        else:
            remove_extra_files(directory, file)



def remove_extra_files(directory, file):
    try:
        print('Removing this file ' +  os.path.join(directory, file))
        os.remove(os.path.join(directory, file))
    except Exception as ex:
        print("Error while removing file " + file + "\s" + ex)


if __name__ == "__main__":
    main()
