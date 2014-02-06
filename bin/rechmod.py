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
    if len(m)>4:
      print "Skipping:",m
      continue
    m2=m[:2]+m[1]+m[1]
    print m,m2
    continue
    try:
      os.chmod(fnm,eval(m2))
    except:
      print "\t Failed for: ",fnm    
    if stat.S_ISDIR(md):
        print "Going into:",fnm

