#!/usr/bin/env python

import subprocess
import shlex
import argparse
import sys

parser = argparse.ArgumentParser(description="Cleans local branches that are no longer on their remote")
parser.add_argument("-V","--verbose",action="store_true",help="Verbose mode")
parser.add_argument("-d","--dry-run",action="store_true",help="Dry run, do not actually delete the branches")
parser.add_argument("-s","--summary",action="store_true",help="Print a summary")

P=parser.parse_args(sys.argv[1:])
## First list remotes
cmd = "git remote show"
p = subprocess.Popen(shlex.split(cmd),stderr=subprocess.PIPE,stdout=subprocess.PIPE)
p.wait()

n = 0
ns=[]
nr=[]
for r in p.stdout.read().split():
    if P.verbose: print "Remote:",r
    nr.append(r)
    ns.append(0)
    cmd = "git remote show %s" % r
    p = subprocess.Popen(shlex.split(cmd),stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    p.wait()
    lines = p.stdout.readlines()
    for i,l in enumerate(lines): 
        if l.find("Remote branches")>-1:
            break
    rb = []
    j=0
    for j,l in enumerate(lines[i+1:]):
        if l.find("Local branches")>-1:
            break
        rb.append(l.split()[0])
    for l in lines[i+j+2:]:
        if l.find("Local ref")>-1:
            break
        lb = l.split()[0]
        Rb = l.split()[4]
        if not Rb in rb:
            cmd = "git branch -D %s" % lb
            if P.dry_run:
                print "# Please remove local branch %s tracking inexisting: %s/%s" % (lb,r,Rb)
                print cmd
                n+=1
                ns[-1]+=1
            else:
                if P.verbose:
                    print "Removing local branch %s tracking inexisting: %s/%s" % (lb,r,Rb)
                subprocess.Popen(shlex.split(cmd))
                n+=1
                ns[-1]+=1

if P.summary:
    print "Summary"
    for i,r in enumerate(nr):
        print "Remote:",r
        print "\tCleaned up %i branches" % ns[i]
    print
    print "Total"
    print "%i local branches cleaned up"%n
