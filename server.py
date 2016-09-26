from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "ShhhSneaky"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/<color>')
def showNinja(color):
    if color == 'blue':
        return render_template('ninja.html', name='Leonardo', ninjaImage='leonardo.jpg')
    elif color == 'orange':
        return render_template('ninja.html', name='Michaelanglo', ninjaImage='michelangelo.jpg')
    elif color == 'purple':
        return render_template('ninja.html', name='Donatello', ninjaImage='donatello.jpg')
    elif color == 'red':
        return render_template('ninja.html', name='Raphael', ninjaImage='raphael.jpg')
    else:
        return render_template('ninja.html', name="April O'Neil", ninjaImage='notapril.jpg')

app.run(debug=True)
