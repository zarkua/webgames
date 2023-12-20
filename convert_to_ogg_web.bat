@echo off

setlocal enabledelayedexpansion

REM Пути к папкам
set TIER_1=Tier_1
set TIER_2=Tier_2
set TIER_3=Tier_3
set TIER_4=Tier_4
set TIER_5=Tier_5
set FINAL=Final


for %%f in (%TIER_1%\*.*) do (
    ffmpeg -i "%%f" -c:a libvorbis -ab 128k -ar 44100 "%FINAL%\%%~nf.ogg"
)

for %%f in (%TIER_2%\*.*) do (
    ffmpeg -i "%%f" -c:a libvorbis -ab 128k -ar 32100 "%FINAL%\%%~nf.ogg"
)


for %%f in (%TIER_3%\*.*) do (
    ffmpeg -i "%%f" -c:a libvorbis -ab 112k -ar 32100 "%FINAL%\%%~nf.ogg"
)


for %%f in (%TIER_4%\*.*) do (
    ffmpeg -i "%%f" -c:a libvorbis -ab 96k -ar 22050 "%FINAL%\%%~nf.ogg"

)


for %%f in (%TIER_5%\*.*) do (
    ffmpeg -i "%%f" -ac 1 -c:a libvorbis -ab 64k -ar 16000 "%FINAL%\%%~nf.ogg" 
)

echo done.
pause
