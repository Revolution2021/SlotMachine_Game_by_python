#!/usr/bin/bash

cd /Users/yonishik_jp/code

source ~/.bashrc

graalpython --polyglot --jvm game7x.py &  #1 Machine
graalpython --polyglot --jvm game7x.py &  #2 Machine
graalpython --polyglot --jvm game7x.py &  #3 Machine
graalpython --polyglot --jvm game7x.py &  #4 Machine
graalpython --polyglot --jvm game7x.py &  #5 Machine
graalpython --polyglot --jvm game7x.py &  #6 Machine
graalpython --polyglot --jvm game7x.py &  #7 Machine
graalpython --polyglot --jvm game7x.py &  #8 Machine
graalpython --polyglot --jvm game7x.py &  #9  Machine
graalpython --polyglot --jvm game7x.py &  #10 Machine

exit 0
