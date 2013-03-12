#!/usr/bin/env python3

import hashlib
import os
import re
import sys


MAX_BUFFER_SIZE = 8 * 1024

def generate_file_check_sum (filepath):

    file = None
    try:
        file = open (filepath, 'rb')
        hash = hashlib.new ('sha1')
        while True:
            chunk = file.read (MAX_BUFFER_SIZE)
            if not chunk:
                break
            hash.update (chunk)
    except Exception as e:
        print ('ERROR!:', e)
    else:
        return hash.hexdigest ()
    finally:
        if file is not None:
            try:
                file.close ()
            except Exception:
                pass

def main (argv=sys.argv):
    usage = "%s [dir]" % argv [0]

    if not argv[1:]:
        basedir = os.getcwd ()
    else:
        basedir = argv [1]

    # TODO: make this settable program arguments 
    verbose = True
    exclude = [r'\.opera']
    exclude = list (map (re.compile, exclude))

    f_list = {}
    try:
        for (dirpath, dirnames, filenames) in os.walk (basedir):
            # omit directories that match any pattern in exclude variable 
            if any (pattern.search (dirpath) for pattern in exclude):
                if verbose:
                    print ('omitted:', dirpath)
                for d_name in dirnames[:]:
                    dirnames.remove (d_name)
                continue
            if verbose:
                print ('checking:', dirpath)
            for f_name in filenames:
                path = os.path.join (dirpath, f_name)
                if os.path.islink (path):
                    continue
                key = generate_file_check_sum (path)
                if key in f_list:
                    f_list [key].append (path)
                else:
                    f_list [key] = [path]
    except KeyboardInterrupt:
        print ('Canceled!')
    finally:
        for k, v in f_list.items ():
            if len (v) > 1:
                print ('same key:', k)
                for f in v:
                    print (f)
                print ()

if __name__ == "__main__":
    main ()
