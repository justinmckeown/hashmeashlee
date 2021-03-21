import os
import platform
import csv
import hashlib
from datetime import datetime

#Set a buffer size to control memory use on the host machine
BUFFER_SIZE = 65536
os_details = {}
hash_type = None

def get_hashing_algs():
    available_hashes = []
    try:
        available_hashes.extend(list(hashlib.algorithms_available))
        available_hashes.sort()
    except Exception as e:
        print(f'Error getting hashing algorithims: {e}')
    finally:
        return available_hashes
    

def print_hello():
    print('Hello!')

def process_input():
    file_path = str(input('What is the file path to the directory which contains the files and subfolders you wish to hash?\n'))
    print(file_path)
    return file_path

def get_os_details():
    try:
        os_details['os'] = platform.system()
        if platform.system() == 'Linux':
            os_details['slash'] = '//'
        else:
            os_details['slash'] = '\\'
    except Exception as e:
        print(f'Eception thrown in get_os_details: {e}')



def itterate(filepath):
    start_time = datetime.now()
    file_count = 0
    dir_count = 0
    report = []
    report.append(f'START TIME: {str(start_time)}\n')
    count = 1
    print(f'About to search on filepath: {filepath}')
    for currentDir, subs, files in os.walk(filepath):
        file_count += len(files)
        dir_count += 1
        if len(files) >0:
            report.extend(hash_and_stash(files, currentDir))
            report.append('\n\n')
            
        else:
            report.append(currentDir+'\n')
            report.append('Directory has no files\n')
            report.append('\n')
        count +=1
    report.insert(1,f'FINISH TIME: {str(datetime.now())}\n')
    report.insert(2, f'TOTAL DIRECTORIES (including base directory): {dir_count}\n')
    report.insert(3, f'TOTAL FILES HASHED: {file_count}\n'+'\n')
    report.insert(4, '\n')
    report_to_dir(filepath, report)

    return report


def hash_and_stash(files, directory):
    details = []
    details.append(directory+'\n')
    with open(directory+os_details.get('slash')+'hashes.csv', 'w', newline='') as hashfile:
        writer = csv.writer(hashfile)
        writer.writerow(['File Name', hash_type+' Hash', 'DateTime'])
        for f in files:
            dt = datetime.strftime(datetime.now(), '%Y-%m-%d-%H:%M:%S')
            s = perform_hash(directory+os_details.get('slash')+f)
            writer.writerow([f,s,dt])
            details.append(str(f)+'\t'+str(s)+'\n')
    return details


def report_to_dir(dir, report):
    try:
        with open(dir+os_details.get('slash')+'report.txt', 'w', encoding='utf-8') as f:
            for i in report:
                f.write(i)
    except Exception as e:
        print(f'Error: {e}')


def perform_hash(filename):
    h  = hashlib.new(hash_type)
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def hash_file(filename, hashtype):
    h = None
    if hashlib.algorithms_available.__contains__(hashtype):
        print(f'Contains: {hashtype}')
        h = hashlib.new(hashtype)
        print(f'H is {h} of type: {type(h)}')
        h.update(b'Hash Me Ashleee')
        print(h.hexdigest())
    

def get_digest(file_path):
    h = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def present_hashing_options(ls: list) -> str:
    print('Available Hashing Algorithims:')
    for index, item in enumerate(ls):
        print(f'{index}. : {item}')
    ans = int(input('From the list above, please enter the number of the Hasing Algorithim you\'d like to use\n'))
    return ans    

if __name__ == '__main__':
    ls = get_hashing_algs()
    #TODO: Make user select a hasing algirithim from a list
    print(ls)
    get_os_details()
    hashing_alg = present_hashing_options(ls)
    hash_type = ls[hashing_alg]
    target_dir = process_input()
    t = itterate(target_dir)
    if t:
        print(f'Hashing Process completed')