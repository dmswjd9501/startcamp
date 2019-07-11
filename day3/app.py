import random
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html') # html 파일을 보내주는거

@app.route('/hi')
def hi():
    return '<hi>용흠아 안녕!!!</hi>'
    return render_template('hi.html')

# variable routing! 경로를 변수로 활용한다.
@app.route('/hi/<string:name>')
def higyo(name):
    return render_template('hi2.html', namee=name)

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!
@app.route('/cube/<int:number>')
def cube(number):
    return f'세제곱 결과는 {number**3}입니다.'

# /lunch/사람이름

@app.route('/lunch/<string:name>')
def lunch(name):
    menu = ['한식', '스페셜A', '스페셜B']
    return render_template('lunch.html', name=name, pick=random.choice(menu))



# /lotto
# 로또 번호 6개를 추천해주는 페이지

@app.route('/lotto')
def lotto():
    numbers = random.sample(range(1, 46), 6)
    return f'이번주 당첨번호는 {numbers} !!'


if __name__ == "__main__":
    # python app.py를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)