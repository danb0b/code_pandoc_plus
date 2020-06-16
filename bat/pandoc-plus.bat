@echo off

::filename
set par1=%1
::output
set par2=%2
::template
set par3=%3

IF ["%par1:~-4%"] == ["docx"] (
::echo hi
::mkdir %par1:~0,-5%_media
set extractstring=--extract-media=./%par1:~0,-5%_media 
) ELSE (
set extractstring=
)

IF ["%par1:~-4%"] == ["docx"] ( set fname=%par1:~0,-5%)
IF ["%par1:~-3%"] == ["tex"] ( set fname=%par1:~0,-4%)
IF ["%par1:~-2%"] == ["md"] ( set fname=%par1:~0,-3%)
IF ["%par1:~-4%"] == ["html"] ( set fname=%par1:~0,-5%)

IF ["%par2%"] == ["docx"] (
::echo hi
pandoc %par1% -s --reference-doc="%HOMEDRIVE%%HOMEPATH%\code_danb0b\code_pandoc_plus\pandoc\%par3%.docx" -o %fname%.%par2%
)

IF ["%par2%"] == ["pdf"] (
::echo hi
pandoc %par1% -s -t latex+smart --filter pandoc-citeproc --data-dir="%HOMEDRIVE%%HOMEPATH%\code_danb0b\code_pandoc_plus\pandoc" --template=%par3%.tex --pdf-engine=xelatex %extractstring%--wrap=none --reference-links --no-highlight -o %fname%.%par2% 
)

IF ["%par2%"] == ["tex"] (
::echo hi
pandoc %par1% -s -t latex+smart --natbib --data-dir="%HOMEDRIVE%%HOMEPATH%\code_danb0b\code_pandoc_plus\pandoc" --template=%par3%.tex --pdf-engine=xelatex %extractstring%--wrap=none --reference-links  --no-highlight -o %fname%.%par2% 
)

IF ["%par2%"] == ["md"] (
::echo hi
pandoc %par1% -s --wrap=none --reference-links %extractstring% --atx-headers -t markdown-raw_html-bracketed_spans-native_spans-native_divs-fenced_divs -o %fname%.%par2%)
::-t markdown-grid_tables-multiline_tables-simple_tables+pipe_tables
