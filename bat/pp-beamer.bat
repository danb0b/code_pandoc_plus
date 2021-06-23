@echo off


::filename
set par1=%1
::output
set par2=%2

IF ["%par1:~-2%"] == ["md"] ( set fname=%par1:~0,-3%)

IF ["%par2%"] == ["pdf"] ( 
pandoc %~dp0\beamer_default.yaml -s -t beamer --pdf-engine=xelatex --slide-level=2 %par1% -o %fname%.%par2%)

IF ["%par2%"] == ["tex"] ( 
pandoc %~dp0\beamer_default.yaml -s -t beamer --pdf-engine=xelatex --slide-level=2 %par1% -o %fname%.%par2%)

IF ["%par2%"] == ["slidy"] ( 
pandoc -t slidy -s --slide-level=2 %par1% -o %fname%.html)

IF ["%par2%"] == ["slideous"] ( 
pandoc -t slideous -s --slide-level=2 -V slideous-url="file:///c:/web/slideous"  %par1% -o %fname%.html)

IF ["%par2%"] == ["s5"] ( 
pandoc -t s5 -s --slide-level=2 -V s5-url="c:/web/s5" %par1% -o %fname%.html)

IF ["%par2%"] == ["revealjs"] ( 
pandoc -t revealjs -s --slide-level=2 -V revealjs-url="file:///c:/web/reveal.js" %par1% -o %fname%.html)

IF ["%par2%"] == ["dzslides"] ( 
pandoc -t dzslides -s %par1% -o %fname%.html)

IF ["%par2%"] == ["pptx"] ( 
pandoc -s --slide-level=2 %par1% -o %fname%.%par2%)