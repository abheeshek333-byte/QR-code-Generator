from flask import Flask,render_template,request,jsonify
import qrcode
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate',methods=['POST'])
def generate():
    data = request.get_json()
    name = data['name']
    img=qrcode.make(name)
    img.save('static/my_qr.png')
    return jsonify({'image_url':'static/my_qr.png'})
    
if __name__=="__main__":
    app.run(debug=True)
    