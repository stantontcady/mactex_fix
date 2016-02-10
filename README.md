#Overview

MacTeX Fix is a simple script that fixes the problems that arise when trying to typeset (using the command line or with TeXShop) a document on newer versions of OS X. Specifically, in El Capitan, i.e., OS X 10.11.x, (possibly before), the OS has a new rootless features that prevents important files from being modified.

The script simply adds a new path to the .bash_profile file and changes the (pdf)tex binary in TeXShop to an alternative that gets around the rootless feature.

##Dependencies
Given that the TeXShop preferences plist is a binary, it requires the binary plist library, [biplist](https://github.com/wooster/biplist).

##Credit
The approach for this script is based off of [this](http://tex.stackexchange.com/questions/249966/install-latex-on-mac-os-x-el-capitan-10-11) discussion on Stack Exchange.