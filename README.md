df-finder
=========

Usage: df-finder [OPTION]... [PATH]...
Dublicate file finder, find dublicated files (same content) in specific PATH.

Mandatory arguments to long options are mandatory for short options too.
  -e, --exclude=PATTERN     directories and files to be excluded from search
  -i, --include=PATTERN     directories and files to be examined
      --excludef=PATTERN    same as -e but for files ONLY
      --includef=PATTERN    same as -i but for files ONLY
      --excluded=PATTERN    same as -e but for directories ONLY
      --included=PATTERN    same as -i but for directories ONLY
  -h, --help                print this message
  -v                        be verbose
  -vv                       be more verbose
  -0                        include empty files (why anyone want to do that?)
  -P                        never  follow  symbolic  links,   this  is the
                            default behaviour.
  -L                        follow symbolic links

PATTERN is a python regular expresion pattern
