
#
# 00_shufflemidi.py
# Plays midi files in present working directory of script in
#   random order.  Parameter option to play all, or specify
#   total number of files to play.
#
#
# Example Usage:
# $ python3 00_shufflemidi.py
# will play all valid midi files in directory in random order
#
# $ python3 00_shufflemidi.py 10
# will play 10 valid midi files in directory in random order
#
#
# Learn At Joes - http://www.learnatjoes.com
#
#
#
# See LICENSE at
# https://github.com/joelabs/learnatjoes-demos/blob/master/LICENSE
#
#


import os
import random
import sys
import shlex

midiPlayer = "aplaymidi"   # set midi application to call here
midiPort   = "128:0"       # set the instrument port here (use aplaymidi -l to list devices)


myFiles = os.listdir(".")

random.shuffle(myFiles)


numFiles = len(myFiles)
idx = 1

reqNumPlays = numFiles;

if len(sys.argv) >= 2:
    reqNumPlays = int(sys.argv[1])
    if reqNumPlays > numFiles or reqNumPlays == 0:
        reqNumPlays = numFiles

for f in myFiles:
    if f.endswith(".mid") or f.endswith(".MID"):
        print("Now Playing ("+str(idx)+"/"+str(reqNumPlays)+"): "+ f)
        f = shlex.quote(f)
        cmdStr = midiPlayer + " -p " + midiPort + " %s" % (f)
        #print(cmdStr)
        #retVal = 0
        retVal = os.system(cmdStr)

        if retVal != 0:
            break

        idx += 1
        if idx > reqNumPlays:
            break

