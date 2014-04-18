from flask import Flask, render_template, request
import posical

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/design")
def design():
    return render_template('design.html')

@app.route("/display", methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        new_cal = posical.AlternateCal(int(request.form['w_i_month']),
                                       int(request.form['d_i_week']),
                                       int(request.form['year_1']))
        layout = new_cal.print_month()
        return render_template('display.html', cal_month = layout)

if __name__ == "__main__":
    app.debug = True
    app.run()