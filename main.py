from flask import Flask, render_template, request, redirect
import pandas as pd
import shutil


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sekmes')
def sekmes():
    status = request.args.get('status')
    return render_template('sekmes.html', veiksmigi = status)

@app.route('/iedvesmai')
def iedvesmai():
    return render_template('iedvesmai.html')

@app.route('/sekmes_man', methods=["POST", "GET"])
def sekmes_man():
    file = pd.read_csv("sekmes_man.csv")
    file.to_html("sekmes_man.html")
    html_file = file.to_html()
    original = r'C:\Users\Lietotajs\Documents\itais\ieskaite_flask\sekmes_man.html'
    target = r'C:\Users\Lietotajs\Documents\itais\ieskaite_flask\templates\sekmes_man.html'
    shutil.copyfile(original, target)
    return render_template('sekmes_man.html')

@app.route('/postData', methods = ['POST', 'GET'])
def postData():
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
       # izvelkam datus
        prieksmets = request.form.get('prieksmets')
        atzime = request.form.get('atzime')
        # izveidojam sarakstu
        saraksts = list((prieksmets, atzime))
        #pārbaudām sarakstu
        print(saraksts)
        # ar Pandas bibliotēku izveidojam csv datni, kur saglabāties
        df = pd.DataFrame([saraksts])
        df.to_csv('sekmes_man.csv', mode='a', index=False, header=False)
        return redirect('/sekmes?status=1')
    else:
        return "This method not supported!"

    
if __name__ == '__main__':
    app.run(port=80, debug=True)