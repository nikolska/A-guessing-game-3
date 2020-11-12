from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def guess_the_number():
    if request.method == 'GET':
        welcome_text = render_template('welcome.html')
        return welcome_text
    elif request.method == 'POST':
        options = render_template('options.html')
        answer = request.form.get('answer')
        guessing = int(request.form.get('guessing', 500))
        min_num = int(request.form.get('min'))
        max_num = int(request.form.get('max'))
        if answer == 'too big':
            max_num = guessing
        elif answer == 'too small':
            min_num = guessing
        elif answer == 'you win':
            return '<h2>I win! I guessed your number!</h2>'

        guessing = (max_num - min_num) // 2 + min_num
        return options.format(max=max_num, min=min_num, guessing=guessing)


if __name__ == '__main__':
    app.run(debug=True)
