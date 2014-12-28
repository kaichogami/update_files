##INTRODUCTION

This is a simple python script which will copy all the unmatched directories and
files from a source folder to a destination folder.
Make sure all copy permission is enabled.

###USE
This is useful if you have an external disk and regularly want to update songs, movies etc.

###NOTE 
This will not check files or directories of a directory in the destination folder.


###EXAMPLE:

```
from copy import update
x = update(source = "G:\\songs", destination = "K:\\songs")
x.update()
```
