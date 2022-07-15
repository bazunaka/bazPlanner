@echo off

rem Пакетный файл для приложения.

dotnet run
@if "%ERRORLEVEL%" == "0" goto success

:fail
    rem Ошибка!
    echo This application has failed!
    echo return value = %ERRORLEVEL%
    goto end
:success
    rem Успешно!
    echo This application has successed!
    echo return value = %ERRORLEVEL%
    goto end
:end
rem Все готово!
echo All Done!