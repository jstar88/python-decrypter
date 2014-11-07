python-decrypter
================

python command line tool to decrypt and decompile bytecode, compatible with python 2.7


### Usage
Download *decrypter.py* and *fupy.py* in the same directory then run:
```
   > python decrypter.py path/yourfile.pyc
```
In *path* directory will be generated the decrypted file *_.pyc* and the decompiled file *_.py* 

### Features
* work also with file with old python version(magic number)
* bypass stupid algorithms that obfuscate marshal dumps, doesn't matter how it's done..the code is retrived from memory   

### Thanks
Fupy small and dirty decompiler: https://github.com/gdelugre/fupy
