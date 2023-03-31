import winreg,os,sys

cwd = os.getcwd()

python_exe = sys.executable

# Create a new registry key under HKEY_CLASSES_ROOT\.myext
# key_path = r"Directory\\Background\\shell\\Segregate"
key_path = '*\\shell\\Segregate'

# key = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, key_path)

# winreg.SetValue(key,None, winreg.REG_SZ, 'Segregate')

# subkey = winreg.CreateKeyEx(key, r"command")
# winreg.SetValue(subkey, None,winreg.REG_SZ, python_exe + f' "{cwd}\\file_organizer.py" "%1"')

# # Close the registry keys
# winreg.CloseKey(subkey)
# winreg.CloseKey(key)



key_path_background = 'Directory\\Background\\shell\\Segregate'

key_background = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, key_path_background)

winreg.SetValue(key_background,None, winreg.REG_SZ, 'Segregate')

subkey_background = winreg.CreateKeyEx(key_background, r"command")
winreg.SetValue(subkey_background, None,winreg.REG_SZ, python_exe + f' "{cwd}\\file_organizer.py" "%V"')

# Close the registry keys
winreg.CloseKey(subkey_background)
winreg.CloseKey(key_background)