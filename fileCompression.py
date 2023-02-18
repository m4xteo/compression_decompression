import zstd
import os
import sys


#TODO: Decompress and add other functions such as dynamic compress

# Compressing Folder Function
def compress_folder(folder):
    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_list.append(file_path)

    total_files = len(file_list)
    count = 1
    compressed_data = b''
    for file in file_list:
        with open(file, 'rb') as f_in:
            data = f_in.read()
            compressed = zstd.compress(data, 12)
            compressed_data += compressed
    with open(os.path.join(folder, 'compressed_files.zst'), 'wb') as f_out:
        f_out.write(compressed_data)
    print(f'Compressed {total_files} files into a single file.')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide the directory to be compressed')
        sys.exit(1)

    folder = sys.argv[1]
    folder = ' '.join(sys.argv[1:])
    compress_folder(folder)
