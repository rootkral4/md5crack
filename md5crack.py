import sys
import hashlib 
import time
import codecs
from termcolor import colored

linecounter = 1

try:
    filedest = sys.argv[1]
    md5hash = sys.argv[2]
except IndexError:
    print(colored("Usage :md5crack.py PATH HASH -v\n-v : verbose mode\nUsing -v slow downs script e.g. (without -v:0.0052449703216552734,with -v:1.5361571311950684)","magenta"))
    sys.exit(1)
try:
    if sys.argv[3] == "-v":
        verbose = "verbose"
    else:
        print(colored("Usage :md5crack.py PATH HASH -v\n-v : verbose mode\nUsing -v slow downs script tested on rockyou.txt\n* without -v *:Line :5189105 Text :natalia012 | 531f950d9690f4383579facd19cd5f45Took 4.539779186248779 Seconds To Crack\n* with -v *:Line :5189105 Text :natalia012 | 531f950d9690f4383579facd19cd5f45Took 94.51337599754333 Seconds To Crack","magenta"))
        sys.exit(1)
except IndexError:
    verbose = "noverbose"
    pass
    
print(colored("Reading File {}","blue").format(filedest))

with codecs.open(filedest, 'r', encoding='cp1258', errors="ignore") as f:
    getlines = f.readlines()

print(colored("File {} Read Ok, Starting Timer","cyan").format(filedest))
startcrack = time.time()
print(colored("Timer Started,Starting Crack","blue"))
if verbose == "verbose":
    for line in getlines:
        line = line.strip()
        md5line = hashlib.md5(line.encode())
        if md5hash == md5line.hexdigest():
            print(colored("Line :{} Text :{} | {}","green").format(linecounter, line, md5line.hexdigest()))
            print(colored("Took {} Seconds To Crack","yellow").format(time.time() - startcrack))
            sys.exit(0)
        else:
            print(colored("Line :{} Text :{} | {}","red").format(linecounter, line, md5line.hexdigest()))
        linecounter += 1
else:
    for line in getlines:
        line = line.strip()
        md5line = hashlib.md5(line.encode())
        if md5hash == md5line.hexdigest():
            print(colored("Line :{} Text :{} | {}","green").format(linecounter, line, md5line.hexdigest()))
            print(colored("Took {} Seconds To Crack","yellow").format(time.time() - startcrack))
            sys.exit(0)
        linecounter += 1
