from flask import Flask, render_template, request
from time import time
import random as r

app = Flask(__name__)

@app.route("/health",methods=["GET"])
def health():
    return "Typing test is working"

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except IndexError:
            error += 1
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/begintest', methods=['GET', 'POST'])
def begin_test():
    if request.method == 'GET':
        test_choices = ["give me attention","i am bored","this typing test is dumb","i love cotton candy"
                "i love berry", "this is me,am the problem,it's me"]
        final_choice = r.choice(test_choices)
        return render_template('test.html', final_choice=final_choice,start_time=time())

@app.route('/results', methods=['POST'])
def results():
    final_choice = request.form['final_choice']
    user_input = request.form['user_input']
    start_time = float(request.form['start_time'])
    end_time= time()
    speed = speed_time(start_time, end_time, user_input)
    error = mistake(final_choice, user_input)
    return render_template('results.html', speed=speed, error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80 , debug=True)
