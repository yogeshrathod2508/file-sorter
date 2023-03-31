import winreg

# Create a new registry key under HKEY_CLASSES_ROOT\.myext
key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, '*\\shell\\Myapp')

# Create a new subkey under the .myext key
subkey = winreg.CreateKey(key, 'command')

# Set the default value of the new subkey to "MyApp File"
command = r' "C:\\Program Files\\Sublime Text\\sublime_text.exe %1"'
winreg.SetValueEx(subkey, '', 0, winreg.REG_SZ, command)

# Close the registry keys
winreg.CloseKey(subkey)
winreg.CloseKey(key)
