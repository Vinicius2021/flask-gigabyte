from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Início',
        var1 = 'teste',
        var2 = 'teste',
        comidas = ['Refrigerante','Pizza','Suco','Salgado','Lanche'],
        precos = ['4.50' , '2.50' , '24.90', '5.50', '18.50']
        
        )

if __name__ == '__main__':
    app.run()