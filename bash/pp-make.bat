@echo off

set par0=%1
set par1=%2
set par2=%3
for %%X in (*.%par0%) do pandoc-plus %%X %par1% %par2% 