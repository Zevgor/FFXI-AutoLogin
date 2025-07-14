Simple Windower -> POL -> FFXI Log In script in Python.

You will need to update the following with your machine's path, but I've used Windower's defauly install location in the code:
windower_launch_param = r'C:\Program Files (x86)\PlayOnline\SquareEnix\Windower\Windower.exe --p Default Profile'
windower_dir = r'C:\Program Files (x86)\PlayOnline\SquareEnix\Windower'

and lastly, update the .env file with your password:
SQX_PASSWORD=password

The .bat file will also need updated with wherever you place this script and it's .venv file.
You can remove the 'pause' line to automatically close command prompt once the script is finished.
