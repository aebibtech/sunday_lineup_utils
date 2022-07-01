echo Creating a new virtual environment for Sunday Line-up Utils...
python -m venv .\venv

echo Activating the virtual environment
call .\venv\Scripts\activate.bat

echo Installing requirements . . .
pip install -r requirements.txt

echo Good to go!
pause