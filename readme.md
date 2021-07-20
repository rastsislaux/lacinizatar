Easy way to use the program:
just run .\compiled\lacinizatar_v1.1.exe

If you don't believe in my executable or want to change something or want to use it not on windows:
1) run command "pyinstaller --windowed --onefile .\script\taraskevizatar.py"
2) replace the file in .\gui\fil\ with the one you got
3) run command "pyinstaller --windowed --onefile -add-data="fil/taraskevizatar.exe;fil" .\exe.py

If you want to run in a console:
py .\script\taraskevizatar.py
