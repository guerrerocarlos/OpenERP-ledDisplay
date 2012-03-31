import win32serviceutil
import win32service
import win32event
import os
import sys
import time
 
sys.stopdriver = "false"
 
def main():
        '''
        Modulo principal para windows
        '''
        sys.path.insert(0,os.getcwd())
        import pos
        a = pos.PosDisplay()
        a.run()
 
class ServiceLauncher(win32serviceutil.ServiceFramework):
        _svc_name_ = 'OpenERP LED-Display Daemon'
        _scv_display_name_ ='TCP to COM - WSGI Server'
        def __init__(self, args):
                win32serviceutil.ServiceFramework.__init__(self, args)
                self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
       
        def SvcStop(self):
                self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
                sys.stopservice = "true"
                win32event.SetEvent(self.hWaitStop)
 
        def SvcDoRun(self):
                main()
