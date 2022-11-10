import os
import mod
import urllib.request

ver = '1.0.0beta'
t = urllib.request.urlopen('http://101.43.48.113:1025/')
onlineVers = t.read();del(t)
onlineVer = onlineVers.split('|')
if not ver == onlineVer[2]:
    os.system('powershell rm setup.exe')
    f = open('setup.exe','wb')
    fb = urllib.request.urlopen('http://101.43.48.113/pcsetup.exe')
    f.write(fb.data)
    f.close()
    os.system('start setup.exe')
    mod.logout('Update is over',0)
mod.logout('mcbox is setup.',0)
mod.logout('Starting...',0)
os.system('nwjs.exe')
mod.logout()