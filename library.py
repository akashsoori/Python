from pathlib import Path
import os, platform, time, xml.etree.ElementTree as ET

def extract_file(src_loc, dest_loc):
    if platform.system() == "Windows":
        extract_exec_cmd = "C:\\apps\\7-Zip\\7z" + " -y x " + src_loc + " -o" + dest_loc    
    else:
        extract_exec_cmd = "cd " + dest_loc + " && unzip -o " + src_loc

    os.system(extract_exec_cmd)

def extract_and_delete_file(src_loc, dest_loc):
    if platform.system() == "Windows":
        extract_exec_cmd = "C:\\apps\\7-Zip\\7z" + " x " + src_loc + " -o" + dest_loc
        delete_exec_cmd = "del /q /f " + src_loc
    else:
        extract_exec_cmd = "echo && cd " + dest_loc + " && unzip " + src_loc
        delete_exec_cmd = "rm -rf " + src_loc

    os.system(extract_exec_cmd)
    os.system(delete_exec_cmd)

def zip_file(dest_loc, src_loc):
    if platform.system() == "Windows":
        zip_exec_cmd = "C:\\apps\\7-Zip\\7z" + " a " + dest_loc + " " + os.path.join(src_loc, "*")
    else:
        zip_exec_cmd = "cd " + src_loc + " && zip -r " + dest_loc + " * && chmod -Rf 755 " + dest_loc
    
    os.system(zip_exec_cmd)

def make_dir_if_not_exists(folder):
    isExist = os.path.exists(folder)
    
    if not isExist:
        os.makedirs(folder)

def if_dir_exists_rename(src_loc, dest_loc):
    isExist = os.path.exists(src_loc)
    if isExist:
        os.rename(src_loc, dest_loc)

def delete_fldr(folder_name):
    isExist = os.path.exists(folder_name)
    if isExist:
        if platform.system() == "Windows":
            os.system("rmdir /s /q " + folder_name)
        else:
            os.system("rm -rf " + folder_name)

def delete_and_make_fldr(folder_name):
    isExist = os.path.exists(folder_name)
    if isExist:
        if platform.system() == "Windows":
            os.system("rmdir /s /q " + folder_name)
            os.system("mkdir " + folder_name)
        else:
            os.system("rm -rf " + folder_name)
            os.system("mkdir -p " + folder_name)
    else:
        if platform.system() == "Windows":
            os.system("mkdir " + folder_name)
        else:
            os.system("mkdir -p " + folder_name)

def check_file_delete(file_name):
    file_name = Path(file_name)
    if file_name.is_file():
        os.remove(file_name)

def search_replace(search, replace, file_name, file_path_name):
    print("Parsing and updating " + search + " " + replace + " in " + file_name + "...\n")

    with open(file_path_name, "r") as file :
        filedata = file.read()

    filedata = filedata.replace(search, replace)

    with open(file_path_name, "w") as file:
        file.write(filedata)

def parse_remove_line(file_path_name):
    try:
        with open(file_path_name, 'r') as fr:
            lines = fr.readlines()
 
        with open(file_path_name, 'w') as fw:
            for line in lines:   
                if line.find('Custom_BMIDE_Templates') == -1:
                    fw.write(line)
    except:
        print("Could not parse the file...")

def get_line_from_file(search_string, search_in_file):
    with open(search_in_file) as file:
        for line in file:
            if search_string in line:
                return line

def stop_services_win(service_display_name, service_name):
    status = os.system("net start | find \"" + service_display_name + "\" > NUL")
    if status == 0:
        status = os.system("sc query \"" + service_name + "| find \"STATE\" | find \"RUNNING\"")
        if status == 0:
            os.system("net stop \"" + service_name + "\"")

def start_services_win(service_display_name, service_name):
    status = os.system("net start | find \"" + service_display_name + "\" > NUL")
    if status == 0:
        status = os.system("sc query \"" + service_name + "| find \"STATE\" | find \"RUNNING\"")
        if status != 0:
            os.system("net start \"" + service_name + "\"")

def get_folder_name(directory_path, directory_pattern):
    directories = [name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name))]

    for directory in directories:
        if directory.find(directory_pattern) != -1:
            return directory

def check_if_file_exists(my_file):
    my_file = Path(my_file)
    if my_file.is_file():
        print(str(my_file) + " exists...")
    else:
        print(str(my_file) + " does not exists...")
        exit(1)
