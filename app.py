from flask import Flask, render_template

app = Flask(__name__)

ranglar = ["Qizil", "Yashil", "Ko'k", "Sariq", "To'q sariq", "Binafsha"]

@app.route('/ranglar')
def ranglar_royxati():
    return render_template(
        'ranglar.html',
        ranglar=ranglar
    )

if __name__ == "__main__":
    app.run(debug=True)
