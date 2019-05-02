# Flask를 사용한 REST API 만들기

## HTTP, FLASK

HTTP는 웹사이트를 위한 프로토콜 일종의 규약입니다. 인터넷이 이 프로토콜을 사용하여 컴퓨터, 서버간의 통신을 하고 있습니다.

가령 여러분들이 브라우져상에 사이트주소를 적고 엔터를 치는 순간 HTTP 요청이 서버쪽으로 발생하게 되는 것입니다.

구글을 예로 들면 google.com를 주소창에 치고 엔터를 치는 순간 HTTP 요청은 구글 서버로 보내지게 됩니다. 구글 서버는 이 요청을 받은 후 어떠한 요청인지 해석한 후 다시 HTTP 응답으로 필요한 정보들을 담아 웹 브라우져로 응답해주게 됩니다. 그 후 여러분이 요청한 것에 대한 응답이 브라우져에 보여지게 되는 것입니다.


## Flask

플라스크를 사용하여 서버사이드 프로세싱이 가능한 웹 어플리케이션이나 Rest API 서버를 만들 수 있습니다. 앞으로 짤 코드를 통해 HTTP 요청을 받을 수 있으며 그것을 해석하여 특정한 작업을 수행하고 다시 알맞은 응답을 할 수 있을 것입니다.

Flask는 마이크로 프레임워크로서 간단한 웹 어플리케이션을 만드는데 특화되어 있습니다.

## 환경설정

Python 3.7 이상 설치: https://www.python.org/downloads/

Python package managerd니 pip를 최신 버전으로 업그레이드

```
> pip install --upgrade pip
```

VSCode의 경우 IDE 익스텐션을 설치하면 도움이 됩니다.
- Python


### Virtual Environment 설치

Virtualenv는 파이썬 환경을 저장하여 사용할 수 있게 해주는 툴입니다. 파이썬 프로젝트를 일종의 sandbox 환경에서 사용할 수 있게 해주는 툴이라고 생각할 수 있습니다. 파이썬 버전이 여러개인 경우 특히 유용합니다.

```
> pip3 install virtualenv
Collecting virtualenv
  Downloading https://files.pythonhosted.org/packages/4f/ba/6f9315180501d5ac3e707f19fcb1764c26cc6a9a31af05778f7c2383eadb/virtualenv-16.5.0-py2.py3-none-any.whl (2.0MB)
    100% |████████████████████████████████| 2.0MB 2.7MB/s
Installing collected packages: virtualenv
Successfully installed virtualenv-16.5.0
```

### Virtual Environment 구성

```
> which virtualenv
/usr/local/bin/virtualenv
```

프로젝트 폴더에 적용하기

특정 파이썬 버전을 가상 환경에서 사용하도록 적용합니다. 사용할 파이썬 버전을 적용해주세요.
-p 플래그는 가상환경에서 사용할 파이썬 버전의 경로를 입력하면 됩니다.

```
> which python3
/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
```

방금 설치한 virtualenv 모듈을 사용하여 가상환경을 구성합니다.

```
> mkdir projects
> cd projects
> python3 -m venv env
Running virtualenv with interpreter /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
Using base prefix '/Library/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/jeffkang/Documents/Projects/Tutorials/ParseServer-EB-Tutorial-MD/sandbox/exampleproject/bin/python3
Also creating executable in /Users/jeffkang/Documents/Projects/Tutorials/ParseServer-EB-Tutorial-MD/sandbox/exampleproject/bin/python
Installing setuptools, pip, wheel...
done.
```

이것을 통해 로컬 복사본을 가상 환경에 만들 수 있으며 패키지들의 의존성을 가상환경 내에서 관리할 수 있습니다.


### Virtual Environment 실행

아래 스크립트를 실행하여 가상 환경을 실행할 수 있으며

```
> source projects/env/bin/activate
```

해당 환경에 python이 설치되어 있는것을 볼 수 있습니다.

```
> which python
```
/Users/Documents/projects/env/bin/python


해당 환경에서는 `deactivate` 를 통해 빠져나올 수 있습니다.

```
> deactivate
```

앞으로는 방금 설치한 가상환경 상에서 프로젝트를 실행하도록 하겠습니다.


### Flask 설치

가상 환경상에 pip를 업그레이드 후 flask를 설치하도록 하겠습니다.
pip를 통해 pip를 최신버전으로 업그레이드합니다.
```
> pip install --upgrade pip
```

플라스클 설치 후
```
> pip install Flask
```

확인해보면 가상환경상에 설치된 것을 확인 가능합니다.

```
> which flask
/Users/Documents/projects/env/bin/flask
```

### 의존성 관리

협업 혹은 git 등을 이용하여 소스관리를 하거나 여러 컴퓨터에서 작업을 하는 경우, 의존성의 관리가 필요합니다.

pip freeze를 통해 의존성 확인 및 관리가 가능합니다.

```
> pip freeze

Click==7.0
Flask==1.0.2
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
Werkzeug==0.15.2
```

가상환경상에서 현재 폴더에 의존성이 기록된 파일을 생성하는 방법입니다.

```
> env/bin/pip freeze > requirements.txt
```

차후 env2 환경에 같은 패키지 모듈들을 인스톨하고 싶은 경우
```
env2/bin/pip install -r requirements.txt
```

식으로 해당 패키지 모듈을 인스톨 가능합니다.

일반적으로 git을 통해 소스 관리를 하는 경우

.gitignore 파일에

`/projects/env` 를 통해 가상환경 설정폴더는 소스 관리에서 제외시키고, requirements.txt 를 통해 모듈의 인스톨, 삭제를 관리합니다.

## Flask 어플리케이션 생성

app.py

```py
from flask import Flask
app = flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/greet')
def say_hello():
  return '잘 돌아가고 있어요'

if __name__ == "__main__":
    app.run(debug=True)
```

Flask 클래스를 임포트 한 후 appd이라는 인스턴스를 만들었습니다.

파이썬 인터프리터 명령어로 스크립트가 실행되는 경우, 파이썬은 자동으로 실행되는 메인함수가 없습니다. `__name__`은 현재 모듈의 이름을 담고 있는 내장 변수이고, flask app.py 처럼 이 모듈을 직접 실행하는 경우 `__main__`으로 설정됩니다.

@는 데코레이션 방식으로 함수를 사용할수 있게 해주는 방식으로서 route를 간단히 적용할 수 있게 도와줍니다.

`if __name__ == "__main__":` 는 Python을 통해 실행할 경우 app.run이 실행되고 다른곳에서 해당 파일을 import할 경우에는 `app.run`이 실행되지 않을 것입니다.

`debug=true`는 파이썬의 에러를 웹페이지에도 표시할 수 있게 해주는 옵션으로서 개발환경에서만 사용하길 권합니다.

바로 구동하고 테스트해보도록 하겠습니다.

```
> python app.py

* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 101-546-803
127.0.0.1 - - [02/May/2019 16:32:15] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [02/May/2019 16:32:16] "GET /favicon.ico HTTP/1.1" 404
```

`http://127.0.0.1:5000/`를 통해 브라우져에서 테스트가 가능합니다.

`http://127.0.0.1:5000/greet` 로도 접속해보시고 `return` 에 있는 응답을 다른 텍스트로 변경해보세요.

## HTML, CSS 와 Flask

### HTML, Templates

일단 `home.html`이라는 HTML 파일을 만들어 보도록 하겠습니다.

templates/home.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Flask Tutorial</title>
  </head>
  <body>
    <h1> My First Try Using Flask </h1>
    <p> Flask is Fun </p>
  </body>
</html>
```

`app.py` 파일에서 해당 html 파일을 불러와 보여주도록 수정합니다.
render_tempalte import를 잊지 마세요.

app.py

```py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/greet')
def say_hello():
  return '잘 돌아가고 있어요!!'

if __name__ == "__main__":
  app.run(debug=True)
```

flask 프레임워크로부터 render_template 메쏘드를 import 하였습니다. 이것은 templates 폴더 안에 있는 템플릿(HTML) 파일들을 찾은 후 render하여 보여줍니다.

이제 다시 `http://127.0.0.1:5000/`에 접속하면 해당 HTML 파일이 출력되는 것을 볼 수 있습니다.

### 템플릿 추가하기

about.html 파일을 추가하도록 하겠습니다.

templates/about.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>About Flask</title>
  </head>
  <body>
    <h1> About Flask </h1>
    <p> Flask is a micro web framework written in Python.</p>
    <p> Applications that use the Flask framework include Pinterest,
      LinkedIn, and the community web page for Flask itself.</p>
  </body>
</html>
```

app.py

```py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/about')
def about():
  return render_template("about.html")

if __name__ == "__main__":
  app.run(debug=True)
```

다른 설명이 필요 없을 정도로 동일한 과정입니다.
이제 두 페이지를 연결해보겠습니다.

### 두 페이지 연결하기

두 페이지 연결을 위해 네비게이션 메뉴를 상단 부분에 만들도록 하겠습니다.

templates/home.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title>Flask Tutorial</title>
</head>

<body>
  <header>
    <div class="container">
      <h1 class="logo">First Web App</h1>
      <strong>
        <nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
          </ul>
        </nav>
      </strong>
    </div>
  </header>

  <h1> My First Try Using Flask </h1>
  <p> Flask is Fun </p>
</body>

</html>
```

templates/about.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title>About Flask</title>
</head>

<body>
  <header>
    <div class="container">
      <h1 class="logo">First Web App</h1>
      <strong>
        <nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
          </ul>
        </nav>
      </strong>
    </div>
  </header>

  <h1> About Flask </h1>
  <p> Flask is a micro web framework written in Python.</p>
  <p> Applications that use the Flask framework include Pinterest,
    LinkedIn, and the community web page for Flask itself.</p>
</body>

</html>
```

기존 페이지에 각각 header를 추가하고 링크를 통해 페이지를 이동할 수 있도록 하였습니다.

코드를 보시면 `url_for()`를 사용한 것을 볼 수 있습니다.이것은 인자값을 받아 여러 역할이 가능한데, 여기서는 static 파일을 읽어오는 것과, app.py에서 route에 정의된 메쏘드로 연결하는 역할을 하고 있습니다.

즉 url_for('home')일 경우는 def home()에 정의된 라우터로 연결되게 됩니다.

이것은 기존의 전통적인 html 페이지를 만드는 방식과 유사한데 페이지가 많아질 경우 <header> 의 영역을 모든 페이지에 붙여넣고 사용해야하는 번거로움과 유지 보수의 문제가 생길 것입니다. 그러므로 template 엔진의 장접을 이용해 html 파일들을 모듈화하여 사용해 보겠습니다.

### Template 장점 살리기

바로 직전에 했던것처럼 반복되는 코드의 사용을 방지하기 위해 template.html 이라는 파일을 만들고 이 파일에서 내용만 새로 불러와 변경하는 식으로 연결을 할 것입니다.

templates/template.html

```html

<!-- Start template.html -->
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title>Template</title>
  <link rel="stylesheet" href="{{ url_for('static',     filename='css/template.css') }}">
</head>

<body>
  <header>
    <div class="container">
      <h1 class="logo">First Web App</h1>
      <strong>
        <nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
          </ul>
        </nav>
      </strong>
    </div>
  </header>

{% block content %}
{% endblock %}
</body>
</html>
<!-- End template.html-->
```

여기에서

```
{% block content %}
{% endblock %}
```

이 부분은 home.html 혹은 about.html의 컨텐츠가  대체될 부분입니다. 즉 컨텐츠 블록을 지정하고 그 부분에 다른 템플릿으로부터 컨텐츠를 넣을 수 있도록 해줍니다.
그러므로 자식 페이지들(home.html, about.html)이 부모 페이지인 template.html에서 호출되어 내용이 변경될 수 있도록 할 것입니다. 그러므로 기존의 html 방식에서는 동일한 코드라도 모든 페이지에 입력하여야만 사용할 수 있는 방법을 HTML 파일을 모듈화 시켜 불러서 사용할 수 있도록 바꿔주는 것입니다.

이제 home.html, about.html 의 코드를 수정하고 tempalte.html과 연동되어 동작하도록 해보겠습니다.

templates/about.html

```html
{% extends "template.html" %}
{% block content %}
<title>Template</title>

  <h1> About Flask </h1>
  <p> Flask is a micro web framework written in Python.</p>
  <p> Applications that use the Flask framework include Pinterest,
    LinkedIn, and the community web page for Flask itself.</p>

{% endblock %}
```

templates/home.html

```html
{% extends "template.html" %}
{% block content %}

<title>Flask Tutorial</title>

<h1> My First Try Using Flask </h1>
<p> Flask is Fun </p>

{% endblock %}
```