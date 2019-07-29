@echo off
set /a a=0
:start
title %a%
set /a a+=1
python main.py
goto start
