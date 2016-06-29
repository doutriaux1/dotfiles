#!/usr/bin/env python
import sys,os,stat

pth = sys.argv[1]

files = os.popen("find %s" % pth).readlines()

for f in files:
    fnm=f.strip()
    try:
      s=os.stat(fnm)
    except:
       continue
    md=s.st_mode
    m=oct(stat.S_IMODE(md))
    if len(m)==5 and m[1]=='2':
      m2 = m[0]+m[2]+m[1]+m[1]
    elif len(m)==4:
      m2=m[:2]+m[1]+m[1]
    else:
      print "Skipping:",m,len(m),m[1]
      continue
    #print m,m2
    try:
      os.chmod(fnm,eval(m2))
    except:
      print "\t Failed for: ",fnm    
    if stat.S_ISDIR(md):
        print "Going into:",fnm,"went from",m,"to",m2

