call conda activate colorbot
call pyinstaller --noconsole --onefile -w --add-data "data/*;." --icon "data/icon.ico" my3isthebest.py
call pyarmor gen --enable-bcc --enable-jit --mix-str --pack dist/my3isthebest.exe my3isthebest.py

call move /Y ".\dist\my3isthebest.exe" ".\my3isthebest.exe"
call rd /s /q ".pyarmor"
call rd /s /q "__pycache__"
call rd /s /q "build"
call rd /s /q "dist"
call del *.spec

call cls

echo Process completed.
pause