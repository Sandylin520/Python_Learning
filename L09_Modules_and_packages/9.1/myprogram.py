from mymodule import my_func
my_func()#Hey I am in mymodule.py

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()#Hey I am in some_main_script in main pacakge
mysubscript.sub_report()#Hey Im a function inside mysubscript
