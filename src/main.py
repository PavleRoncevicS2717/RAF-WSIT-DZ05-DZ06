from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/rasporedi')
def rasporedi():
	f = open("RAF.csv", "r")
	redovi = f.readlines()

	sva_imena = [red.split(',')[2] for red in redovi]
	sve_ucionice = [red.split(',')[6] for red in redovi]

	imena = []
	ucionice = []
	for ime in sva_imena:
		if ime not in imena:
			imena.append(ime)

	sva_imena = imena.sort()

	for ucc in sve_ucionice:
		if ucc not in ucionice:
			ucionice.append(ucc)
	
	sve_ucionice = ucionice.sort()
	
	return render_template("rasporedi.html", redovi = redovi, sva_imena = imena, sve_ucionice = ucionice)
	
if __name__ == '__main__':
	app.run()