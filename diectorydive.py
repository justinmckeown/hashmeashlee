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



def itterate():
    start_time = datetime.now()
    file_count = 0
    error_count = 0
    count = 1
    for currentDir, subs, files in os.walk(r'C:\Users\j.mckeown\Documents\jobApplications\QOMPLX\OSINT Technical\OSINT Technical Assesment\Supportingmaterial\Evidence'):
        if len(files) >0:
            hash_and_stash(files, currentDir)
        else:
            print(f'{currentDir} has no files')
        count +=1



def hash_and_stash(files, directory):
    with open(directory+os_details.get('slash')+'hashes.csv', 'w', newline='') as hashfile:
        writer = csv.writer(hashfile)
        writer.writerow(['File Name', 'Sha256 Hash', 'DateTime'])
        for f in files:
            dt = datetime.strftime(datetime.now(), '%Y-%m-%d-%H:%M:%S')
            s = sha256sum(directory+os_details.get('slash')+f)
            writer.writerow([f,s,dt])




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
    itterate()