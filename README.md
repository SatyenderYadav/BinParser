# BinParser

### What are artifacts in $Recycle.Bin

In Windows Vista, the recycle Bin directory is named $Recycle.Bin and in this inside their SID directory the deleted files and their metadata is stored. There are two files in the windows Recycle Bin $I and $R.

$R file is the original file that is deleted and $I contains the metadata of the file. The filename in the recycle bin is such that $R then some random letters and the metadata of this file will start with $I as discussed and have the same random letters.

The $I file contains the original filename, path, file size, and when the file was deleted.

![image](https://user-images.githubusercontent.com/54953623/212481581-13d3ed61-700e-4dbd-a1d0-209368b286c8.png)

### Structure of the $I

![image](https://user-images.githubusercontent.com/54953623/212481242-193d50a6-6f22-44d5-b9c1-11bf595a818f.png)

Image Credit [DF-Stream](https://df-stream.com/2016/04/fun-with-recycle-bin-i-files-windows-10/)

### Usage

```py 
python3 main.py -f <$I file>
```

![image](https://user-images.githubusercontent.com/54953623/212481745-55d19dd9-5425-4a4c-86a1-2fb6bd10d0e6.png)



