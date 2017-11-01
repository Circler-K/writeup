# 서울아이티고등학교 해킹방어대회 Writeup
## Introduce
* Author : 김한솔 (Circler)
* E-Mail : dkdlelgksthf@gmail.com
* Blog   : [naver blog](http://blog.naver.com/dkdlelgksthf)
* Date   : 2017-09-24

## Review
 * 생각했던 난이도보다 쉬웠다.
 * 초반에 4등까지 올라갔지만 후반에 리버싱을 풀지 못해서 엄청 내려갔다.  
 ~~리버싱을 공부하자~~

## Solve
- 문제의 번호순서대로 작성하고 번호는 문제의 번호이다.   

### 1. warm up
- 플래그를 찾아야한다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/1.png)
-

- 페이지소스코드를 보자.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/1-2.png)

- welcome.js 파일이 있다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/1-3.png)
- 플래그가 있다.


### 2. warm up
- 시작
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/2.png)

- 로마의 군인이 쓰는암호 = 99% 카이사르암호
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/2-2.png)

- 복호화를 하고 전송을 하면 플래그가 나온다.  
-플래그인증을 하고나서 생각해봤는데 플래그도 암호화 되있는 것 같지만 결국 복호화를 못했다.

### 5. encrypt code
- 문제를 열면 자바코드를 준다.

> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/5.png)

>배열에다가 숫자를 집어넣고 배열을 또 입력받아서 XOR연산 후 Ruby_is_light와 동일한지 묻는다.

- XOR연산의 특성상 3개의 개체가 있으면 하나는 다른 두 개체의 XOR연산 값이다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/5-1.png)
* 코드를 짜서 돌리면 플래그가 나온다.

### 6. permission
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/6-first.PNG)

> First Solve!

- 문제를 보면 아무것도 없이 참거짓의 여부를 묻고있다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/6.png)
> 뭔가 쿠키에 있을 것 같은 느낌이여서 봤더니 뭔가 있다!

- 자바스크립트로 쿠키를 변경한 다음에 새로고침하면 플래그가 나온다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/6-1.png)

### 7. spongebob
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-first.PNG)

> First Solve!

- 스폰지밥이 무지개빛 무지개와 함께 있다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7.png)

- '어딘가에' 라는 문구가 힌트인 것 같아서 소스코드를 봤더니 어느 페이지가 나온다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-1.png)

- 들어가면 편지를 보내야한다고 나온다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-2.png)

- view-source 있길래 들어가 봤다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-3.png)
>
> ~~처음 문제를 봤을 때는 이런 텍스트 없었는데 풀고나서 10분 쯤 있다가 나온 것 같다.~~  
> 정규식인 [a-zA-Z-0-9]을 이용해서 영문자, 숫자가 GET방식으로 넘어올 경우 필터링한다.  
> 위 정규식에 걸리지 않는 문자는 " ~!@#$%^&\*()\_\= 한글"  
>  
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/7-4.png)
> NULL  byte를 전달해도 플래그가 나온다.

### 8. wizard
- 문제를 보면 웬 마법사로 추정되는 2D 할아버지 사진이 나온다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/8.png)
- change wizard 나 change weapon 버튼을 눌러도 아무런 반응이 없지만 shop 버튼을 누르면 뭔가 뜬다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/8-1.png)
- 코드를 봤더니 unknown에 value만 가진 input태그가 있었다. (name속성이 없으면 GET으로 값을 받지 못함)
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/8-2.png)

- 일단 value속성이 가진 값을 GET파라미터의 character로 넘겨주면 심슨캐릭터가 뜬다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/8-3.png)

- 이미지에있는 [A-B-C-D-E-F-G-H-I-J-K-...Z] 이것이 왜 있는지 한참을 생각한 결과 정규표현식이라고 결론을 내었고 실제로 저 패턴을 ([regexr.com](http://regexr.com)) 사이트에서 테스트를 해보니 실제로 알파벳 대문자만 검색되는 것이였다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/8-4.png)
- URL에 있는 Fitgerald를 fitgerald로 바꿔주면 플래그 획득

### 9. login
- 우선 문제를 열면 검은 화면이 나온다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/9.png)

- 일단 웹문제는 웹페이지의 소스코드부터 보는 것이 정석인듯 하다. 우선 보면 robots.txt라고 써져있다. 들어가보자
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/9-1.png)

- admin 폴더의 크롤링을 막는다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/9-2.png)

- admin 폴더에 들어가서 쿠키를 확인해 보면 내 아이디인 123456789 를 md5로 해싱한 값을 쿠키로 저장했다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/9-3.png)

- 그러면 admin 문자열을 md5로 해싱한 값을 쿠키에다가 넣어주면 풀린다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/9-5.png)

### 10. find.
- 로그인창이 있고 힌트로 id=admin, password=0~9999 라는 힌트가 주어졌다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/10.png)

- 뭔가 브루트포싱을 해야 할 것 같다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/10-1.png)

- 돌리면 나온다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/10-2.png)

### 15. server
- 패킷파일을 하나 주는데 처음에 HEX 에디터로 열어보았다. 그러나 찾기 힘들어서 wireshark로 다시 열었다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/15.png)
- 보다보면 "..etwork_Is_Easy"라는 문자열이 있는데 약간의 게싱으로 network_Is_Easy로 인증했더니 풀렸다.

### 16 . capture
- 또 다시 패킷파일을 하나 준다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/16.png)
- 열어서 string 검색으로 flag 를 검색했더니 플래그가 나온다.

### 17. unknown
- 페이지에 들어가서 소스코드를 보면 뭔가 이상한 페이지로 리다이렉트시키는데 정상적인 이름이 아니다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/17.png)

- hint.txt가 있다고 해서 들어갔더니 이상한 문자열이 있다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/17-1.png)

- base64로 디코딩하면 처음페이지에서 리다이렉트할 페이지의 이름을 어떻게 치환했는지 나온다.
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/17-2.png)

- 그것에 맞게 thisisadminpage.php 로 들어가면 웬 로그인폼이 있는데
> ![Circler](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/ITgo_CTF/1st/17-3.png)
> 입력창에다가 admin 과 아무문자열이나 입력하면 플래그가 나온다.
