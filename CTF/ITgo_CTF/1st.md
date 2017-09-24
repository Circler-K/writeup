# 서울아이티고등학교 해킹방어대회 Writeup
## Introduce
* Author : 김한솔 (Circler)
* E-Mail : dkdlelgksthf@gmail.com
* Blog   : [naver blog](http://blog.naver.com/dkdlelgksthf)
* Date   : 2017-09-24

## Review
 * 생각했던 난이도보다 쉬웠다.
 * 초반에 4등까지 올라갔지만 후반에 리버싱을 풀지 못해서 엄청 내려갔다.\
 ~~리버싱을 공부하자~~

## Solve
- 문제의 번호순서대로 작성하고 번호는 문제의 번호이다.   

### 1. warm up
- 플래그를 찾아야한다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/1.png)
-

- 페이지소스코드를 보자.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/1-2.png)

- welcome.js 파일이 있다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/1-3.png)
- 플래그가 있다.


### 2. warm up
- 시작
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/2.png)

- 로마의 군인이 쓰는암호 = 99% 카이사르암호
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/2-2.png)

- 복호화를 하고 전송을 하면 플래그가 나온다.  
-플래그인증을 하고나서 생각해봤는데 플래그도 암호화 되있는 것 같지만 결국 복호화를 못했다.

### 5. encrypt code
- 문제를 열면 자바코드를 준다.

>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/5.png)

>배열에다가 숫자를 집어넣고 배열을 또 입력받아서 XOR연산 후 Ruby_is_light와 동일한지 묻는다.

- XOR연산의 특성상 3개의 개체가 있으면 하나는 다른 두 개체의 XOR연산 값이다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/5-1.png)
* 코드를 짜서 돌리면 플래그가 나온다.

### 6. permission
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/6-first.PNG)

> First Solve!

- 문제를 보면 아무것도 없이 참거짓의 여부를 묻고있다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/6.png)
> 뭔가 쿠키에 있을 것 같은 느낌이여서 봤더니 뭔가 있다!

- 자바스크립트로 쿠키를 변경한 다음에 새로고침하면 플래그가 나온다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/6-1.png)

### 7. spongebob
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-first.PNG)

> First Solve!

- 스폰지밥이 무지개빛 무지개와 함께 있다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7.png)

- '어딘가에' 라는 문구가 힌트인 것 같아서 소스코드를 봤더니 어느 페이지가 나온다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-1.png)

- 들어가면 편지를 보내야한다고 나온다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-2.png)

- view-source 있길래 들어가 봤다.
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-3.png)
>
> ~~처음 문제를 봤을 때는 이런 텍스트 없었는데 풀고나서 10분 쯤 있다가 나온 것 같다.~~  
> 정규식인 [a-zA-Z-0-9]을 이용해서 영문자, 숫자가 GET방식으로 넘어올 경우 필터링한다.  
> 위 정규식에 걸리지 않는 문자는 " ~!@#$%^&*()_+= 한글 "  
>  
>![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-4.png)
> NULL  byte를 전달해도 플래그가 나온다.

### 8. wizard
