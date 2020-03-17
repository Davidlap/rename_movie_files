Quick script to modify directories with movie files so plex server can read it appropriately and download the necessary metadata


### Arguments

positional arguments:
  path        Path to the folder

optional arguments:
  -h, --help  show this help message and exit
  -r          Expresion to split the directory name
  -e          Movie file extensions
  
 ### Examples
 
 plex_title_cleaner.py C:\Movies 
 plex_title_cleaner.py C:\Movies -r '(2018)' -e .avi -e .mp4 -e .mpg
 
 ### Use case
 

 C:.
├───A Clockwork Orange (1971) [1080p]
│       a.clockwork.oraangeeee.mp4
│
├───A Dog's Purpose (2017) [1080p] [YTS.AG]
│       dogspurpose.A [1080p].mp4
│
└───A Plastic Ocean (2016) [1080p] [YTS.AG]
        A Plastic Ocean (2016) [1080p] [YTS.AG].mp4

  
 You run  plex_title_cleaner.py C:\Movies and you obtain, a clean movie file title
 
 C:.
├───A Clockwork Orange (1971) [1080p]
│       A Clockwork Orange (1971).mp4
│
├───A Dog's Purpose (2017) [1080p] [YTS.AG]
│       A Dog's Purpose (2017).mp4
│
└───A Plastic Ocean (2016) [1080p] [YTS.AG]
        A Plastic Ocean (2016).mp4
        
 
 
