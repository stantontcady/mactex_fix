#!/usr/bin/env python
from logging import error, info
from os.path import expanduser
from sys import exit

from biplist import readPlist, writePlist


home_dir = expanduser("~")

bash_profile_fn = "{0}/.bash_profile".format(home_dir)
texbin_path = "/Library/TeX/Distributions/.DefaultTeX/Contents/Programs/texbin"

with open(bash_profile_fn, "a") as bash_profile_f:
    bash_profile_f.write("export PATH=$PATH:{0}".format(texbin_path))
    info("texbin path added to bash_profile successfully")

texshop_plist_fn = "{0}/Library/Preferences/TeXShop.plist".format(home_dir)

try:
    texshop_plist = readPlist(texshop_plist_fn)
except (InvalidPlistException, NotBinaryPlistException), e:
    exit("could not read existing texshop plist: {0}".format(e))
    
texshop_plist['TetexBinPath'] = texbin_path

try:
    writePlist(texshop_plist, texshop_plist_fn)
except (InvalidPlistException, NotBinaryPlistException), e:
    exit("could not write to existing texshop plist: {0}".format(e))
