# pip install cowsay

import cowsay
import sys
from saying import goodbye

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])
    goodbye(sys.argv[1])
