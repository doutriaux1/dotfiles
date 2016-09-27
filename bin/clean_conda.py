#!/usr/bin/env python
import subprocess
import shlex

def call(cmd):
    cmd = shlex.split(cmd)
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    return p.stdout.read()
envs = call("conda env list")
for e in envs.split("\n"):
    if e!="" and e[0]=="v" and e.find("-g")>-1:
        print "cleaning:",e
        call("conda remove -y --all -n %s" % e.split()[0])

