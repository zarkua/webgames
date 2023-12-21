@echo off
setlocal enabledelayedexpansion

set SOURCE_FOLDER=Music_test
set OUTPUT_FOLDER=Final
set ERROR_LOG=error_log.txt

REM Создание папки для конвертированных файлов, если она не существует
if not exist "%OUTPUT_FOLDER%" mkdir "%OUTPUT_FOLDER%"

REM Массивы битрейтов, частот дискретизации и каналов
set QUALITIES=1 2 3 4 5 6 7 8 9 10
set SAMPLE_RATES=8000 11025 16000 22050 32000 44100 48000 88200 96000
set CHANNELS=1 2

REM Перебор всех файлов в исходной папке
for %%f in ("%SOURCE_FOLDER%\*.*") do (
    REM Перебор всех комбинаций битрейтов, частот дискретизации и каналов
    for %%q in (%QUALITIES%) do (
        for %%s in (%SAMPLE_RATES%) do (
            for %%c in (%CHANNELS%) do (
                echo converting %%~nxf with bitrate %%q, sample rate %%s and %%c channels
                ffmpeg -i "%%f" -ac %%c -c:a libvorbis -q:a %%q -ar %%s "%OUTPUT_FOLDER%\%%~nf_q%%q_s%%s_c%%cch.ogg" 
            )
        )
    )
)

echo Конвертация завершена.
pause
