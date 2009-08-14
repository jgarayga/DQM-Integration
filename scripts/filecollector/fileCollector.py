#! /usr/bin/env python

import os,time,sys,glob,zipfile,re,shutil,stat

#set environments
exedir = '/nfshome0/dqmpro/filecollector' # directory to execute the relevant scripts
YourEmail='lilopera@cern.ch'
DIR = '/home/dqmprolocal/output'  #directory to search new files
TMPDIR = '/dqmdata/dqm/.dropbox_tmp' # stealth area on cmsmon
FILEDIR = '/dqmdata/dqm/dropbox' # directory, to which files are stored
TFILEDONEDIR = '/home/dqmprolocal/done' # directory to store *_T files once they have been processed
IGFILEDIR = '/dqmdata/EventDisplay/dropbox' #Directory to store ig Files.
OLDIGFILES = '/dqmdata/EventDisplay'
WAITTIME = 120 # waiting time for new files (sec)
RETRIES = 3

def filecheck(rootfile):
  cmd = exedir + '/filechk.sh ' + rootfile
  a = os.popen(cmd).read().split()
  tag = a.pop()
  if tag == '(int)(-1)':
    #print "File corrupted"
    return 0
  elif tag == '(int)0':
    #print "File is incomplete"
    return 0
  elif tag == '(int)1':
    #print "File is OK"
    return 1
  else:
    return 0
  
def sendmail(EmailAddress,run):
  sever=os.getenv("HOSTNAME")
  s=smtplib.SMTP("localhost")
  tolist=[EmailAddress, "lat@cern.ch"]
  body="File copy to dropbox failed by unknown reason for run:%09d on server: %s" % (run,server)
  msg = MIMEText(body)
  msg['Subject'] = "File merge failed."
  msg['From'] = ServerMail
  msg['To'] = EmailAddress
  s.sendmail(ServerMail,tolist,msg.as_string())
  s.quit()
    
def convert(infile, ofile):
  cmd = exedir + '/convert.sh ' + infile + ' ' +ofile
  os.system(cmd)

####### ENDLESS LOOP WITH SLEEP
while True:
  NRUNS = 0  #Number of runs found
  NFOUND = 0  #Number of files found
  NEW = {}
  TAGS= []
  #Dealing with .ig files
  ignames=sorted(glob.glob("%s/*.ig" % DIR))
  for igfile in ignames:
    if re.search("_R[0-9]{9}",igfile):
      runstr=igfile.split("_R")[-1][:9]
      destdir="%s/%s/%s" % (IGFILEDIR,runstr[:3],runstr[3:6])
      destfile="%s/%s" % (destdir,igfile.rsplit("/",1)[-1])
      if not os.path.exists(destdir):
        os.makedirs(destdir)
      shutil.move(igfile,destfile)
      os.chmod(destfile,stat.S_IREAD|stat.S_IRGRP|stat.S_IROTH| stat.S_IWRITE|stat.S_IWGRP|stat.S_IWOTH)
    else:
      destfile="%s/%s" % (OLDIGFILES,igfile.rsplit("/",1)[-1])
      ref=1
      ndestfile=destfile
      while os.path.exists(ndestfile):
        ndestfile="%s-%03d.ig" %(destfile.split(".ig")[0],ref)
        ref+=1	
      shutil.move(igfile,ndestfile)
      print "file %s is not a standar name file, saved in %s directory for manual handeling" % (igfile,OLDIGFILES)
  for dir, subdirs, files in os.walk(DIR):
    for f in files:
      if re.match('^DQM_.*_R[0-9]*_T[0-9]*\.root$', f) or re.match('^Playback_.*_R[0-9]*_T[0-9]*\.root$', f):
        runnr = long(f[f.rfind("_R")+2:f.rfind("_T")])
        subsystem=f.split("_")[2]
        runstr="%09d" % runnr
        donefile = "%s/%s/%s/%s" % (TFILEDONEDIR, runstr[0:3], runstr[3:6], f)
        f = "%s/%s" % (dir, f)
        if os.path.exists(donefile) and os.stat(donefile).st_size == os.stat(f).st_size:
          print "WARNING: %s was already processed but re-appeared" % f
          os.remove(f)
          continue
        NEW.setdefault(runnr, {}).setdefault(subsystem,[]).append(f)
        NFOUND += 1  
  if len(NEW.keys()) == 0:
    print 'waiting for new files to process...'
    time.sleep(WAITTIME)
    continue
      
  TAGS=sorted(glob.glob('%s/tagfile_runend_*' % DIR ),reverse=True)
  if len(TAGS)==0:
    if len(NEW.keys()) <= 1:
      print 'waiting for new files to process...'
      time.sleep(WAITTIME)
      continue
    print 'No tagfile_runend foud, checking for *_T files that could have been left behind'
    TAGRUNEND=long(sorted(NEW.keys(),reverse=True)[1])
  else:
    TAGRUNEND=long(TAGS[0].split("_")[2])
    
  for tag in TAGS:
    os.remove(tag)

  for run,subsystems in NEW.items():
    if run <= TAGRUNEND:
      for subsystem,files in  subsystems.items():
        done=False
        keeper=0
        Tfiles=sorted(files,reverse=True)
        for Tfile in Tfiles:
          version=len(glob.glob("%s/DQM_V*_%s_R%09d.root" % (FILEDIR,subsystem,run)))+1
          finalTMPfile="%s/DQM_V%04d_%s_R%09d.root" % (TMPDIR,version,subsystem,run)
          finalfile="%s/DQM_V%04d_%s_R%09d.root" %   (FILEDIR,version,subsystem,run) 
          runstr="%09d" % run
          finalTfile="%s/%s/%s/%s" % (TFILEDONEDIR,runstr[0:3],runstr[3:6],Tfile.split("/")[-1])
          finalTsubdir="%s/%s" % (TFILEDONEDIR,runstr[0:3])
          finalTdir="%s/%s/%s" % (TFILEDONEDIR,runstr[0:3],runstr[3:6])
          if not os.path.exists(finalTsubdir):
            os.mkdir(finalTsubdir)
          if not os.path.exists(finalTdir):
            os.mkdir(finalTdir)
          if os.path.exists(finalTMPfile):
            os.remove(finalTMPfile)
          if not done:
            if filecheck(Tfile) == 1:
              if "Playback" in Tfile:
                dqmfile = Tfile.replace('Playback','DQM')
                convert(Tfile,dqmfile)
                os.rename(Tfile,finalTfile.replace('Playback','Playback_full'))
                Tfile=dqmfile  
              for i in range(RETRIES):
                shutil.copy(Tfile,finalTMPfile)
                if os.path.exists(finalTMPfile) and os.stat(finalTMPfile).st_size == os.stat(Tfile).st_size:
                  os.rename(Tfile,finalTfile)
                  os.rename(finalTMPfile,finalfile)
                  os.chmod(finalfile,stat.S_IREAD|stat.S_IRGRP|stat.S_IROTH| stat.S_IWRITE|stat.S_IWGRP|stat.S_IWOTH)  
                  break
                else:
                  print "Problem transfering final file for run %09d\n Retrying in %d" % (run,WAITTIME)
                  if i == RETRIES-1: sendMail(YourEmail,run)
                  time.sleep(WAITTIME)
              done=True
            else:
              print "file %s is incomplete looking for next DQM_V*_%s_R%09d_T*.root valid file" % (Tfile,subsystem,run)
              if keeper == 0:
                keeper+=1
                shutil.move(Tfile,finalTfile+"_d")
              else:
                os.remove(Tfile) #
                
          else:
            if keeper == 0:
              keeper+=1
              shutil.move(Tfile,finalTfile+"_d")
            else:
              os.remove(Tfile) #
  #continue
      
  