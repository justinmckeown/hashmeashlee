import os
import platform
import csv
import hashlib
from datetime import datetime

#Set a buffer size to control memory use on the host machine
BUFFER_SIZE = 65536
os_details = {}

def print_hello():
    print('Hello!')

def process_input():
    file_path = str(input('What is the file path to the directory which contains the files and subfolders you wish to hash?\n'))
    print(file_path)

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
    error_count = 0
    report = []
    report.append(f'START TIME: {str(start_time)}\n')
    count = 1
    print(f'About to search on filepath: {filepath}')
    for currentDir, subs, files in os.walk(filepath):
        file_count += len(files)
        if len(files) >0:
            report.extend(hash_and_stash(files, currentDir))
            report.append('\n\n')
            
        else:
            print(f'{currentDir} has no files')
            report.append(currentDir+'\n')
            report.append('Directory has no files\n')
            report.append('\n')
        count +=1
    report.insert(1,f'FINISH TIME: {str(datetime.now())}\n'+'\n')

    return report


def hash_and_stash(files, directory):
    details = []
    details.append(directory+'\n')
    with open(directory+os_details.get('slash')+'hashes.csv', 'w', newline='') as hashfile:
        writer = csv.writer(hashfile)
        writer.writerow(['File Name', 'Sha256 Hash', 'DateTime'])
        for f in files:
            dt = datetime.strftime(datetime.now(), '%Y-%m-%d-%H:%M:%S')
            s = sha256sum(directory+os_details.get('slash')+f)
            writer.writerow([f,s,dt])
            details.append(str(f)+'\t'+str(s)+'\n')
    return details




#NOTE: Got this from here: https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

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


#NOTE: This may only work on Linux Systems, but may be faster
def sha256sum_v2(filename):
    h  = hashlib.sha256()
    with open(filename, 'rb') as f:
        with mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) as mm:
            h.update(mm)
    return h.hexdigest()


if __name__ == '__main__':
    get_os_details()
    process_input()
    t = itterate()