
#
# 00_shufflemidi.py
# Plays midi files in present working directory of script in
#   random order.  Parameter option to play all, or specify
#   total number of files to play.
#
# 
# Learn At Joes - http://www.learnatjoes.com
#
#
#
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>
#
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

