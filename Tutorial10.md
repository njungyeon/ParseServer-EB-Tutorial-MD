
## 클라이언트 연동하기

이제 지금까지 구현한 서버 api를 호출하여 사용하는 클라이언트를 만들어 보겠습니다.

일단 미리 만들어져 있는 `header-footer.html`, `header-footer.css`를 다운받아 `templates` 폴더에 넣어주세요.

header-footer.html: https://drive.google.com/open?id=1A-7xvzIQ7sbj8qwHOSzPLOaqOKEakTXX
header-footer.css: https://drive.google.com/open?id=10LBOnOjeiZOadvEqm7kKRxgC0_3vh17F


### 1. 메인화면 만들기

기존에 작성한 `templates/idol-list.html` 을 활용할 것입니다.
header와 footer는 `header-footer.html` 에서 복사 붙여넣기를 통해 사용해주세요.

이미지는 적당히 넣어주세요.

![client1](images/client1.png)

pages/index.html

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>IDOL </title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" media="screen" href="../css/index.css">
</head>

<body>
  <div class="body">
    <div class="header">
      <div class="header-contents">
        <a href="../pages/index.html" class="logo col-s-6">
          <h1>IDOL POP</h1>
        </a>
        <a href="javascript:void(0);" class="icon col-s-6" onclick="hamburgBarToggle()">
          <img src="../../images/ic-menu.svg" class="ic_menu">
        </a>
        <nav id="headerNav" class="topnav">
          <button class="close-button" onclick="hamburgBarToggle()">
            <img src="../../images/ic-leave.svg">
          </button>
          <div class="nav-items">
            <a href="#" class="active Header-Text">HOME</a>
            <a href="#" class="Header-Text">MyIdol</a>
          </div>
          <a  href="../pages/login.html" class="login-container">
            Login
          </a>
        </nav>
      </div>
    </div>

    <div class="full-width-contents">
      <img src="../images/slide-banner.png">
    </div>

    <div class="contents">
      <div class="idol-lists-container">
        <div class="title view-all-container row-container">
          <div class="Big-Title">IDOL Lists</div>
          <a class="Header-Text" href="javascript:void(0);">
            View All
          </a>
        </div>

        <div class="category">

          <div class="container">
            <div class="img-title-tag-list" id="dynamic-list"></div>
          </div>
        </div>

      </div>

    </div>

    <div class="footer">
      <div class="contents">
        <div class="bottom-container">
          <div class="term">
            <div class="link-container Tab-Selected">
              <a>IDOL POP</a>
            </div>
            <a>jeffgukang@gmail.com</a>
            <div class="row-container">
              <a>Term of Service</a>&nbsp | &nbsp<a>Privacy Policy</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
<script>
  function hamburgBarToggle() {
    var x = document.getElementById("headerNav");
    if (x.className === "topnav") {
      x.className += " re sponsive";
    } else {
      x.className = "topnav";
    }
  }
</script>
<script src="../js/parse.min.js"></script>
<script src="../js/parseApis.js"></script>
<script src='../templates/idol-list.js'></script>
<script>
  getIdolList();
</script>

</html>
```


css/index.css

```css
@import url(./default.css);
@import url(../templates/header-footer.css);
@import url(../templates/idol-list.css);

.idol-lists-container {
	margin-top: 80px;
}

.view-all-container {
	justify-content: space-between;
	align-items: flex-end;
	color: var(--brown-grey);
}

.view-all-container a {
	display: flex;
	align-items: center;
}

.space-between {
	justify-content: space-between;
}

.category {
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	justify-content: space-around
}

.category .container {
	display: flex;
	flex-direction: column;
	align-items: center;
	min-width: 315px;
	margin-top: 53px;
	/* border: 1px solid; */
}

.category .container .title-text {
	font-family: aritadsb;
	font-size: 22px;
	color: #646464;
	width: 305px;
}

.category .container .subtitle {
	text-align: left;
	width: 305px;
	margin-top: 9px;
}

.category .container > .img-title-tag-list {
	display: flex;
	align-items: center;
	flex-direction: column;
	margin-top: 20px;
}

.new-idol-container {
	margin-top: 80px;
}

.new-idol-container .img-title-list {
	margin-top: 51px;
}

.spotlight-container {
	margin-top: 80px;
}

.spotlight-container .img-desc-list {
	margin-top: 40px;
}

.community-container {
	margin-top: 80px;
}

.footer {
	margin-top: 100px;
}
```

### 2. 로그인 화면 만들기

이제 회원가입, 로그인, 로그아웃 을 적용하도록 하겠습니다.

![client2](images/client2.png)

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>IDOL </title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" media="screen" href="../css/index.css">
  <link rel="stylesheet" type="text/css" media="screen" href="../css/login.css">
</head>

<body>
  <div class="body">
    <!-- 기존 header 부분을 추가합니다. -->

    <div class="full-width-contents">
      <img src="../images/slide-banner.png">
    </div>

    <div class="contents" id="login-body">
      <div class="contents-container">
        <div class="login-form-container col-6 col-s-12">
          <div class="Title-Text">Login to Your Account</div>
          <div class="icinputs-container">
            Username: <input type="text" id="input-username" placeholder="username"
              class="Text-Input input-text input-text-email" />
            <div class="input-help-container">
              Password: <input type="password" id="input-password" placeholder="Password"
                class="Text-Input input-text input-text-password" />
            </div>
          </div>

          <button onclick="signIn()" class="submit Button-Text">
            Login
          </button>

          <br />
          <a  href="../pages/signup.html">
            Do you want to sign up?
          </a>

        </div>
      </div>
    </div>

    <!-- 기존 footer 부분을 추가합니다. -->
</body>
<script>
  function hamburgBarToggle() {
    var x = document.getElementById("headerNav");
    if (x.className === "topnav") {
      x.className += " re sponsive";
    } else {
      x.className = "topnav";
    }
  }
</script>
<script src="../js/parse.min.js"></script>
<script src="../js/parseApis.js"></script>
<script>
  async function signIn() {
    const username = document.getElementById('input-username').value;
    const password = document.getElementById('input-password').value;
    console.log(username, password);

    try {
      const result = await ParseApi.signIn(username, password);
      console.log(result);
      if (result.error) {
        alert(result.error);
      }

      location.href = '../pages/index.html';
    } catch(error) {
      alert(error);
    }
  }
</script>

</html>
```

Javascript 코드를 유의깊게 보세요.
로그인 스크립트를 살짝 수정하여 에러 메세지가 alert창을 통해 출력되도록 하였습니다.

cs/login.css

```css
@import url(./default.css);
@import url(../templates/header-footer.css);

#login-body {
  display: flex;
    flex-direction: column;
    justify-content: center;
  align-items: center;
  font-family: aritadm;
}

.contents-container {
  max-width: var(--contents-max-width);
  width: 100%;
  min-height: 900px;
  display: flex;
    flex-direction: column;
    align-items: center;
}

.login-form-container {
  display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  margin-top: 71px;
}

.login-form-container .ic_header_logo {
  min-width: 130px;
  align-self: flex-start;
}

.login-form-container .title-text {
  font-family: aritadsb;
  margin-top: 35px;
}

.img-background {
  background: pink;
  background: url(../images/photo.png) no-repeat top left;
  background-size: cover;
}

.icinputs-container {
  width: 100%;
  max-width: 400px;
}

.icinputs-container > * {
  margin-top: 26px;
}

.login-form-container button {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  width: 300px;
  height: 50px;
  border-radius: 5px;
  background-color: var(--tab-button);
    border: none;
    color: white;
    font-size: 25px;
}

.login-form-container button.submit {
  margin-top: 34px;
}
```

로그인 테스트도 해보세요.

### 3. 회원가입 화면 만들기

기존 login.html과 거의 동일합니다.
pages/signup.html

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>IDOL </title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" media="screen" href="../css/index.css">
  <link rel="stylesheet" type="text/css" media="screen" href="../css/login.css">
</head>

<body>
  <div class="body">
    <div class="header">
      <div class="header-contents">
        <a href="../pages/index.html" class="logo col-s-6">
          <h1>IDOL POP</h1>
        </a>
        <a href="javascript:void(0);" class="icon col-s-6" onclick="hamburgBarToggle()">
          <img src="../../images/ic-menu.svg" class="ic_menu">
        </a>
        <nav id="headerNav" class="topnav">
          <button class="close-button" onclick="hamburgBarToggle()">
            <img src="../../images/ic-leave.svg">
          </button>
          <div class="nav-items">
            <a href="#" class="active Header-Text">HOME</a>
            <a href="#" class="Header-Text">MyIdol</a>
          </div>
          <a  href="../pages/login.html" class="login-container">
            Login
          </a>
        </nav>
      </div>
    </div>

    <div class="full-width-contents">
      <img src="../images/slide-banner.png">
    </div>

    <div class="contents" id="login-body">
      <div class="contents-container">
        <div class="login-form-container col-6 col-s-12">
          <div class="Title-Text">SignUp</div>
          <div class="icinputs-container">
            Username: <input type="text" id="input-username" placeholder="username"
              class="Text-Input input-text input-text-email" />
            <div class="input-help-container">
              Password: <input type="password" id="input-password" placeholder="Password"
                class="Text-Input input-text input-text-password" />
            </div>
          </div>

          <button onclick="signUp()" class="submit Button-Text">
            SignUp
          </button>

          <br />
          <a  href="../pages/login.html">
            Already have account.
          </a>

        </div>
      </div>
    </div>

    <div class="footer">
      <div class="contents">
        <div class="bottom-container">
          <div class="term">
            <div class="link-container Tab-Selected">
              <a>IDOL POP</a>
            </div>
            <a>jeffgukang@gmail.com</a>
            <div class="row-container">
              <a>Term of Service</a>&nbsp | &nbsp<a>Privacy Policy</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
<script>
  function hamburgBarToggle() {
    var x = document.getElementById("headerNav");
    if (x.className === "topnav") {
      x.className += " re sponsive";
    } else {
      x.className = "topnav";
    }
  }
</script>
<script src="../js/parse.min.js"></script>
<script src="../js/parseApis.js"></script>
<script>
  async function signUp() {
    const username = document.getElementById('input-username').value;
    const password = document.getElementById('input-password').value;
    console.log(username, password);

    try {
      const response = await ParseApi.signUp(username, password);
      if (response.error) {
        alert(response.error);
      } else {
        console.log(response);
        alert(`Welcome, ${response.result.username} \n SignUp Finished`);
        location.href = '../pages/login.html';
      }
    } catch(error) {
      alert(error);
    }
  }
</script>

</html>
```

signUp 부분으로 변경된 함수들을 유의하세요. 회원가입 성공시 웰컴메시지와 함께 로그인 화면으로 이동시키는 코드입니다.

### 4. 로그아웃 만들기

로그아웃은 기존 login 화면에 추가하도록 하겠습니다.

pages/login.html

```html
<button onclick="signIn()" class="submit Button-Text">
  Login
</button>

<br />
<a  href="../pages/signup.html" class="login-container">
  Do you want to sign up?
</a>

<br />
or
<button onclick="logout()" class="submit Button-Text">
  Logout
</button>
```

`signin()` 하단에 logout 관련 함수 역시 추가해줍니다.

```html
<script>
  ...
async function logout() {
  try {
    Parse.User.logOut();
    location.href = '../pages/index.html';
  } catch(error) {
    alert(error);
  }
}
</script>
```

로그인, 로그아웃을 누르며 로컬 스토리지가 어떻게 변하는지 테스트해보세요.

### 4. 로그인한 유저 정보가 저장되어 있는 경우의 처리

Parse SDK를 쓰면 별도의 세션관리를 하지 않아도 유저가 로그인했을때 그 정보를 Local Storage를 이용하여 저장하고 다른 요청에 사용합니다.

메인 화면에서 유저가 로그인 되어 있는지 확인 한 후 헤더를 변경하는 동작을 구현하도록 하겠습니다.

js/parseApis.js

```js
static checkCurrentUser() {
    const user = Parse.User.current();

    if (user) {
      return user.toJSON();
    } else {
      return false;
    }
  }
```

유저가 존재할경우 유저 정보를 리턴하는 함수입니다.
이제  기존 메인화면에 유저 정보를 체크한 후 유저네임을 헤더에 표시하도록 해보겠습니다.

pages/index.html후

```html
<script>
  getIdolList();

  const user = ParseApi.checkCurrentUser();
  if (user) {
    console.log(user);
    const ele = document.querySelector('.header .login-container')
    ele.innerHTML = user.username;
  }
</script>
```

유저 정보를 확인 후 헤더에 이름을 표시해주는 동작을 수행합니다.

### 5. 아이돌 주식 유저 구매 연동하기

이제 클라이언트(웹페이지)에서 유저가 아이돌의 주식을 구매하는 코드를 작성해봅시다.

앞에서 `purchaseItem` 등 서버에서 필요한 동작은 미리 구현이 되어 있으므로 클라이언트만 구현하면 됩니다.

js/parseApis.js

```js
static async purchaseItem({objectId, count}) {
  try {
    const result = await Parse.Cloud.run('purchaseItem', {objectId, count});
    if (result) {
      return  result.toJSON();
    } else {
      throw 'Something Wrong';
    }
  } catch (error) {
    throw error;
  }
}
```

기존 idol-list.js에서 생성하는 엘레먼트에 `<button class="buy-button" onclick="purchaseItem('${objectId}')">Buy</button>` 을 추가해줍니다.

templates/idol-list.js

```js
const { name, price, group, description, count, imgUrl,  objectId} = element; // Add objectId

      const html =  `<div class="item row-container" id="${objectId}">` + // Edit this line
        `<img src="${imgUrl}" class="profile">` +
        `<div class="column-container">` +
            `<div class="title idol-Name">${name}</div>` +
            `<div class="description">${description}</div>` +
            `<div class="tags Hashtag">` +
                `<span class="tag">${group}</span>` +
            `</div>` +
        `</div>` +
        `<div class="column-container subinfo-container">` +
            `<span class="Sub-Text quantity">Quantity: ${count}</span>` + // Add class called quantity
            `<span class="Sub-Text">$${price}</span>` +
        `</div>` +
        `<button class="buy-button" onclick="purchaseItem('${objectId}')">Buy</button>` + // Add this line
    `</div>`;
```

코드를 이해하고 넘어가세요.

templates/idol-list.css 에 css 역시 추가해줍니다. 구매 버튼 말고 차후 사용할수 있는 sell-button 관련 스타일도 추가해주겠습니다.

templates/idol-list.css

```css
...
.img-title-tag-list .item .buy-button {
    border: none;
    background: var(--lightish-blue);
    color: white;
    font-size: 20px;
}

.img-title-tag-list .item .sell-button {
    border: none;
    background: red;
    color: white;
    font-size: 20px;
}
```

![client3](images/client3.png)

이제 메인 페이지에서 Buy 버튼을 누를시 서버와의 통신을 하고 정상적으로 응답을 받으면 남은 수량을 수정하는 코드를 짜보도록 하겠습니다.

pages/index.html

```html
<script>
  async function purchaseItem(id) {
    const ele = document.getElementById(id);

    const item = {
      objectId: id,
      count: 1
    }
    try {
      const result = await ParseApi.purchaseItem(item);
      console.log(result);

      ele.querySelector('.quantity').innerHTML = 'Quantity: ' + result.count;
    } catch (error) {
      alert(error);
    }
  }
</script>
```

위 코드는 정상적으로 구매가 될 경우 수량을 갱신하고, 오류 발생시 alert창을 띄우는 코드입니다. 로그아웃 후에 구매시도를 하면 세션 정보(유저 정보)가 지워진 상태이므로 에러 메세지가 뜨는것이 정상입니다.

![client4](images/client4.png)



## 과제

![homework](images/homework.png)


지금까지 배운것을 응용하면 여러가지 기능을 구현할 수 있습니다. 그 중 서버에 이미 구현이 되어 있는 API를 활용해 추가적인 작업을 진행해보세요.

### 1. 유저가 구매한 내역을 화면에 보여주기

유저의 구매 내역을 출력하는 코드는 이미 구현이 되어 있고 Postman을 통해 응답값을 확인할 수 있었습니다.
메인 페이지에 유저의 구매 내역을 출력하는 코드를 작성해보세요.

- 코드 완성 및 프론트엔드(웹페이지) 동작 스크린샷

1.	index.html 페이지 접속시에 로그인한 유저가 보유한 아이돌 주식내역을 화면에 리스트로 보여주는 서버 api를 생성하세요.

js/parseApi.js

```js
//   과제:  유저가 구매한 아이템 리스트를 서버에게 요청하고 응답값을 json으로 바꿔 배열로 리턴한다.
static async getUserItemList() {
  try {
    const response = await Parse.Cloud.run('getUserItemList', {});
    let result = [];
    console.log('getUserItemList', response);
    if (response) {
        response.forEach(element => {
        result.push(element.toJSON());
      });

      return  result;
    } else {
      throw 'Something Wrong';
    }
  } catch (error) {
    throw error;
  }
}
```

index.html 에서 사용할 코드

```html
<div class="container">
  <div class="img-title-tag-list" id="purchased-list">
    <!-- 유저가 구매한 내역을 담을 영역 -->
  </div>
</div>
```

```js
  // 유저가 구매한 아이템 리스트를 화면에 출력해준다.
  async function showPurchasedItem() {
    const container = document.getElementById('purchased-list');
    const result = await ParseApi.getUserItemList();

    let htmls = [];
    result.forEach(element => {
        const { count, objectId } = element;
        const { name, price, group, description, imgUrl} = element.character;

       const html =  `<div class="item row-container" id="${objectId}">` +
        `<img src="${imgUrl}" class="profile">` +
        `<div class="column-container">` +
            `<div class="title idol-Name">${name}</div>` +
            `<div class="description">${description}</div>` +
            `<div class="tags Hashtag">` +
                `<span class="tag">${group}</span>` +
            `</div>` +
        `</div>` +
        `<div class="column-container subinfo-container">` +
            `<span class="Sub-Text quantity">보유 수량: ${count}</span>` +
            `<span class="Sub-Text">$${price}</span>` +
        `</div>` +
        `<button class="sell-button sell" onclick="sell('${objectId}')">Sell</button>` +
    `</div>`;

    const e = document.createElement('div');
    e.innerHTML = html;

    container.appendChild(e);
    });
  }

  showPurchasedItem();
```

!!서버에서 사용할 코드(과제), 아래를 참고하여 작성해주세요.

cloud/functions/index.js

```js

// 요청한 유저가 보유하고 있는 UserCharacter 데이터를 리턴한다.
Parse.Cloud.define('getUserItemList', async (req) => {
  const user = req.user;

  if (user == null) {
    throw Error('There is no user');
  }

  const ????? = Parse.Object.extend('?????'); // Get class from database table
  const query = ????? // TODO: 클래스로부터 쿼리를 생성한다.
  ????? // TODO: 요청한 유저가 보유한 아이템만을 선택해야 한다.
  query.include('character');

  try {
    const result = await query.find(); // Get all datas
    return result;
  } catch (error) {
    throw error;
  }
});
```

### 2. 유저가 보유한 아이템 판매하는 기능

유저가 보유한 아이템을 하나씩 판매하는 API를 서버에 구현해보고 테스트해보세요.

- 코드 완성 및 프론트엔드 동작 스크린샷

1. POSTMAN으로 테스트
2. 실제 클라이언트로 테스트

#### 힌트
'purchastItem' api 를 참고하세요.

cloud/function/index.js

```js
// 과제2: 유저가 보유한 아이템을 하나씩 판매하는 API를 서버에 구현해보고 테스트해보세요.
// 힌트: 'purchaseItem' Api를 참고
Parse.Cloud.define('sellUserItem', async (req) => {
  const user = req.user;
  const objectId = req.params.objectId;

  if (user == null) {
    throw Error('There is no user');
  }

  const UserCharacter = Parse.Object.extend('UserCharacter'); // Get class from database
  let userCharacter = new UserCharacter();

  // TODO: obejectId를 통해 유저가 보유한 아이템을 매치시킨다.
  ?????
  // TODO: 매치한 아이템 정보를 DB로부터 불러온다.
  ?????

  let originalCharacter = await userCharacter.get('character').fetch(); // character 포인터 정보를 가져온다.
  const characterPrice = ????? // character 가격 정보를 가져온다.

  try {
    const count = userCharacter.get('count');
    if (count <= 0) {
      throw Error('Not enought quantity');
    }
    ????? // TODO: 오리지널 아이템(아이돌) 갯수를 1만큼 늘린다.
    ????? // TODO: 유저가 보유한 아이템(아이돌) 갯수를 1만큼 감소시킨다.
    ????? // TODO: 유저가 보유한 캐쉬를 아이템 가격만큼 늘린다.

    await user.save(null, {useMasterKey: true});
    return userCharacter.save(); // 유저가 보유한 아이템 정보를 저장 후 리턴한다.
  } catch (error) {
    throw Error(error);
  }
```

js/parseApis.js

```js
  // 과제2: 유저가 보유한 아이템을 하나씩 판매하는 API를 서버에 구현해보고 테스트해보세요.
  // 유저가 보유한 주식을 판매하는 요청을 서버에 보내고 응답을 받는 함수
  static async sellUserItem(objectId) {
    try {
      const result = await Parse.Cloud.run('sellUserItem', { objectId: objectId });
      if (result) {
        return  result.toJSON();
      } else {
        throw 'Something Wrong';
      }
    } catch (error) {
      throw error;
    }
  }
```

index.html에서

유저 아이템 판매 버튼인
```html
<button class="sell-button sell" onclick="sell('${objectId}')">Sell</button>
```
를 통해 아래 코드가 수행됩니다.

pages/index.html

```js
  // js/parseApis.js 의 sellUserItem을 호출하고 응답을 받아 유저가 보유한 아이템 갯수를 갱신하는 함수
  async function sell(id) {
    const ele = document.getElementById(id);

    try {
      const result = await ParseApi.sellUserItem(id);
      console.log(result);

      ele.querySelector('.quantity').innerHTML = '보유 수량: ' + result.count;
    } catch (error) {
      alert(error);
    }
  }
```

### 3. 여러 수량 한꺼번에 판매하기

2번과제는 현재 하나의 수량씩 판매가 되도록 되어 있습니다.
이것을 여러 수량을 한꺼번에 판매하도록 서버 API를 편집하고 포스트맨에서 테스트해보고 응답값을 스크린샷으로 찍어주세요.

### 4. 여러 수량 한꺼번에 구매하기 (보너스)

현재는 한번에 하나의 수량만 구매할 수 있도록 웹페이지가 구현이 되어 있습니다. 이것을 갯수를 선택해서 구매할 수 있도록 웹페이지를 편집해보세요.
힌트는 idol-list.js, index.html 파일입니다. 현재 사용중인 서버 api는 `purchaseItem` API입니다.

프론트엔드 코드만 수정하면 됩니다.

## Conclusion

지금까지 서버, 클라이언트 간의 통신을 통한 애플리케이션 구축을 해 보았습니다. 현재는 웹페이지를 클라이언트로 사용했지만, 모바일 애플리케이션 또한 동일한 방법으로 서버와 통신을 하며 서비스를 구축할 수 있을 것입니다.

여기서 Javascript의 장점 중 하나인 한 언어로 서버, 클라이언트를 모두 다룰 수 있는 것을 보았습니다. 또한 Parse SDK를 활용하여 손쉽게 API 서버를 구축하고, 프론트엔드와 통신을 할 수 있었습니다.

이것을 응용하면 벡엔드부터 프론트엔드까지 하나의 시스템을 다룰 수 있을 것입니다.