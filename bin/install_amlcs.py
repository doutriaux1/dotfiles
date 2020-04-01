# install kosh and aml_dmt into current Python
# Sets permission correctly
#!/usr/bin/env python
import os
import shlex
import sys
from subprocess import Popen, PIPE
import argparse

p = argparse.ArgumentParser()

p.add_argument("--no_chmod", action="store_true")
p.add_argument("-v", "--verbose", action="store_true")

args = p .parse_args()

os.chdir(os.path.expanduser("~/git/kosh"))

def run_cmd(cmd, verbose=False):
  p = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
  o,e = p.communicate()
  if verbose:
    print(o.decode("utf-8"))

cmd = "python setup.py install"
run_cmd(cmd, args.verbose)

os.chdir(os.path.expanduser("~/git/data_management_tools"))
run_cmd(cmd, args.verbose)

if args.no_chmod:
  print("will not rechmod")
else:
  print("Chmoding")
  cmd = f"find {sys.prefix}/bin   -type f -exec chmod g+rx  {{}} +"
  run_cmd(cmd, args.verbose)
  cmd = f"find {sys.prefix}  -type f -exec chmod g+r  {{}} +"
  run_cmd(cmd, args.verbose)
  cmd = f"find {sys.prefix}  -type d -exec chmod g+rx  {{}} +"
  run_cmd(cmd, args.verbose)
