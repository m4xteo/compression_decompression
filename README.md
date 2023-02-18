# Zstd compression algorithm
Utilizes modern zstd compression / decompression algorithm 


## What does it do?

This python script utilizes zstd compression and decompression method (soon to come). zstd is a compression algorithm is a lossless data compression algorithm developed by Yann Collet at Facebook. It is currently one of the BEST compression / decompression methods due to its ratio to speed properties. 

(more information will be added soon).


This script will encrypt contents inside a DIRECTORY / FOLDER into one .zst file (compressed_files.zst). (WARNING: No decompression methods are implemented, use at your own risk.) 


Settings: Compression uses level 12.

### Requirements:
```pip3 install zstd```

### Usage:
```python3 fileCompression.py PATH```

e.g:

```python3 fileCompression.py /Documents/```
