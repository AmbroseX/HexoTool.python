Set WshShell = WScript.CreateObject("WScript.Shell")
targetfolder = createobject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
targetfile = targetfolder+"\hexoblog.vbs"

strDesktop = WshShell.SpecialFolders("Desktop") :'�����ļ��С����桱
set oShellLink = WshShell.CreateShortcut(strDesktop & "\HexoBlogTools.lnk")
oShellLink.TargetPath = targetfile : 'Ŀ��
oShellLink.WindowStyle = 3 :'����1Ĭ�ϴ��ڼ������3��󻯼������7��С��
oShellLink.Hotkey = "Ctrl+Alt+H" : '��ݼ�
oShellLink.IconLocation = targetfolder+"\img\logo.ico" : 'ͼ��
oShellLink.Description = "HexoBlotTools" : '��ע
oShellLink.WorkingDirectory = targetfolder : '��ʼλ��
oShellLink.Save : '���������ݷ�ʽ

Wscript.echo "HexoBlogTools�����ݷ�ʽ�����ɹ�"