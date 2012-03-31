OpenERP 6.1 POS - LED Display Daemon
===========================

![Selling machine ledDisplay](http://cloud.github.com/downloads/guerrerocarlos/OpenERP-ledDisplay/OpenERP-POS-ledDisplay.png)

**Summary:** this is a WSGI web socket that allows OpenERP 6.1 web-POS to communicate with
the selling machine ledDisplay (connected to a COM serial port), from javascript.

It allows the OpenERP web-POS to run within the browser but still be able to communicate with the COM port and and
local peripheral connected to the machine.

Any request, improvement or bug can be reported at:
https://github.com/guerrerocarlos/OpenERP-ledDisplay/issues

*OpenERP-ledDisplay* is released under the *GPL v3* licence see file ``COPYING`` or visit
http://www.gnu.org/licenses/gpl-3.0.html

Install as a Windows Service:
----------------------------

Download the latest .zip from 
https://github.com/guerrerocarlos/OpenERP-ledDisplay/downloads

Unzip the file

Execute:

    ServiceLauncher.exe -install

Start it or/and configure to start automatically at Windows startup in the Windows Services Manager


Compiling Requirements:
-----------------------

 * ``eventlet``
 * ``greenlet``
 * ``py2exe`` 

Build:
------

The easiest way to install the dependences is grabbing the compiled installer at:
http://www.lfd.uci.edu/~gohlke/pythonlibs/

Then execute  
    
    $ python setup.py py2exe

The Windows executable (Daemon) will be in the *dist* folder.

How to use:
-----------

Add this function to your web-POS javascript file located in:
addons_folder/point_of_sale/static/src/js/pos.js

    function ledDisplay(line1,line2){
            try{
                if (window.XMLHttpRequest)
                  {// code for IE7+, Firefox, Chrome, Opera, Safari
                  xmlhttp=new XMLHttpRequest();
                  }
                else
                  {// code for IE6, IE5
                  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
                  }
                  xmlhttp.open("GET","http://localhost:8100/"+String(line1)+"___"+String(line2),false);
                  xmlhttp.send();
                }catch(err){
            }
    }

and use it however you want to show the progress in every sale
for example this would generate something like in this README first image:

    ledDisplay("OpenERP 6.1 POS","LED DISPLAY DAEMON");
