import time
import sys
buildservice = True
if '--no-service' in sys.argv[1:]:
        buildservice = False
        sys.argv = [k for k in sys.argv if k != '--no-service']
        print sys.argv
       
from distutils.core import setup
import os
import py2exe
import glob
import shutil
 
sys.path.insert(0,os.getcwd())
 
def getFiles(dir):
        """
        Retorna una tupla de tuplas del directorio
        """
        # dig looking for files
        a= os.walk(dir)
        b = True
        filenames = []
 
        while (b):
                try:
                        (dirpath, dirnames, files) = a.next()
                        filenames.append([dirpath, tuple(files)])
                except:
                        b = False
        return filenames
 
DESCRIPTION = 'TCP/IP to COM daemon'
NAME = 'OpenERP Display Connector'
 
 
class Target:
        def __init__(self,**kw):
                        self.__dict__.update(kw)
                        self.version        = "1.00.00"
                        self.compay_name    = "carlosguerrero.org"
                        self.copyright      = "(c) 2011, Carlos Guerrero"
                        self.name           = NAME
                        self.description    = DESCRIPTION
 
my_com_server_target = Target(
                description    = DESCRIPTION,
                service = ["service_module"],
                modules = ["service_module"],
                create_exe = True,
                create_dll = True)
 
if not buildservice:
        print 'Compilando como ejecutable de windows...'
        time.sleep(2)
        setup(
            name = NAME ,
            description = DESCRIPTION,
            version = '1.00.00',
            console = ['pos.py'],
                zipfile=None,
                options = {
                                "py2exe":{"packages":"encodings",
                                        "includes":"win32com,win32service,win32serviceutil,win32event",
                                        "optimize": '2'
                                        },
                                },
        )
else:
        print 'Compilando como servicio de windows...'
        time.sleep(2)
        setup(
            name = NAME,
            description = DESCRIPTION,
            version = '1.00.00',
                service = [{'modules':["ServiceLauncher"], 'cmdline':'pywin32'}],
                zipfile=None,
                options = {
                                "py2exe":{"packages":"encodings",
                                        "includes":"win32com,win32service,win32serviceutil,win32event",
                                        "optimize": '2'
                                        },
                                },
        )
