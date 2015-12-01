::ref:http://stackoverflow.com/questions/8487489/batch-programming-get-relative-path-of-file

@echo off & setlocal enabledelayedexpansion

set rootdir=%~dp0
set foo=%rootdir%
set cut=
:loop
if not "!foo!"=="" (
    set /a cut += 1
    set foo=!foo:~1!
    goto :loop
)
echo Root dir: %rootdir%
echo strlen  : %cut%
echo ------------------------
:: also remove leading /
set /a cut += 1

for /R %rootdir% %%F in (.,*) do (
    set B=%%~fF
    ::take substring of the path
    set B=!B:~%cut%!
    ::echo Full    : %%F 
    echo \!B!
 
	echo \!B!>>%~n0.txt
)
echo ------------------------
echo result saved in %~n0.txt .
 

 
pause