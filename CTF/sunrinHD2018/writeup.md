# 선린 교내 해킹방어대회

### 최종 5등함
### Team 잘생긴사람들
###### 팀명은 다들 잘생긴 사람들이라서 이렇게 지었습니다.
### 저는 웹만 풀어서 웹만 씁니다.
### 발표용 ppt파일도 있습니다.

## Click the button! (점수 기억안남)

- button 1부터 10, 총 10개가 있고 꼭 1부터 10까지 차례대로 눌러야 플래그가 나온다.

### payload
- #### payload 1
```javascript
$("[onclick='click_button(1, this)']").click();
$("[onclick='click_button(2, this)']").click();
$("[onclick='click_button(3, this)']").click();
$("[onclick='click_button(4, this)']").click();
$("[onclick='click_button(5, this)']").click();
$("[onclick='click_button(6, this)']").click();
$("[onclick='click_button(7, this)']").click();
$("[onclick='click_button(8, this)']").click();
$("[onclick='click_button(9, this)']").click();
$("[onclick='click_button(10, this)']").click();
```
- 한 몇십번 시도하니 플래그가 나왔다.

- #### payload 2
```javascript
for (var i = 0; i < 11; i++) {
	$("[onclick='click_button("+i+", this)']").click();
}
```
- 세번 시도하니 플래그가 나왔다.

- #### payload 3
```javascript
setTimeout(function() {
    $("[onclick='click_button(1, this)']").click();
    setTimeout(function() {
        $("[onclick='click_button(2, this)']").click();
        setTimeout(function() {
            $("[onclick='click_button(3, this)']").click();
            setTimeout(function() {
                $("[onclick='click_button(4, this)']").click();
                setTimeout(function() {
                    $("[onclick='click_button(5, this)']").click();
                    setTimeout(function() {
                        $("[onclick='click_button(6, this)']").click();
                        setTimeout(function() {
                            $("[onclick='click_button(7, this)']").click();
                            setTimeout(function() {
                                $("[onclick='click_button(8, this)']").click();
                                setTimeout(function() {
                                    $("[onclick='click_button(9, this)']").click();
                                    setTimeout(function() {
                                        $("[onclick='click_button(10, this)']").click();
                                    }, 15);
                                }, 15);
                            }, 15);
                        }, 15);
                    }, 15);
                }, 15);
            }, 15);
        }, 15);
    }, 15);
}, 15);
```
- 콜백함수를 사용하니 바로 플래그가 나왔다.

- ### javascript 코드 해설
- 플래그를 얻기 위해서는 꼭 버튼을 순서대로 눌러 인증서버에 버튼의 순서대로 인증을 해야한다.
- 자바스크립트 특성인 비동기식 코드실행때문에 콜백함수를 사용하지 않으면 언제든 순서가 바뀔수 있다고 생각한다.
- 그러나 payload 1 과 payload 2의 경우 첫번째 줄 코드가 실행된 뒤 결과를 기다리지 않고 바로
두번째 줄 코드를 실행하게 된다. 그렇게 된다면 비동기식 코드 실행에 의해  두번째 코드가 먼저 결과가 나오게 될 수 도 있다.
그렇게 된다면 플래그가 나올수 없게 되는 것이다. 그렇기 때문에 코드실행의 순서를 강제하기 위해 콜백함수를 사용하여야 한다.

- #### payload 4 
- tab + enter 키를 10번 누르면 플래그가 나온다.
- html코드에서 button태그의 순서를 랜덤으로 하지 않아서 가능했던 풀이 방법이다.

<br>
<br>
<br>
<br>
<br>
<br>
<br>


### Simple Login

