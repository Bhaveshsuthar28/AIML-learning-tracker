Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get the script directory
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
repoRoot = fso.GetParentFolderName(scriptDir)

' Path to Python executable
pythonExe = "pythonw.exe"  ' pythonw.exe runs without showing console window

' Path to the schedule script
scheduleScript = scriptDir & "\schedule_streak.py"

' Run the script silently
WshShell.Run """" & pythonExe & """ """ & scheduleScript & """", 0, False

Set WshShell = Nothing
Set fso = Nothing

