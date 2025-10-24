rom flask import Flask

app = Flask(__name__)

contador = 0

@app.route('/')
def home():
    global contador
    contador += 1
    return f'''
    <html>
        <head>
            <title>Projeto para Alunos</title>
            <style>
                body {{
                    font-family: Arial;
                    text-align: center;
                    margin: 50px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }}
                .container {{
                    background: rgba(255,255,255,0.1);
                    padding: 40px;
                    border-radius: 15px;
                    backdrop-filter: blur(10px);
                    max-width: 600px;
                    margin: 0 auto;
                }}
                h1 {{
                    font-size: 2.5em;
                    margin-bottom: 20px;
                }}
                .counter {{
                    font-size: 3em;
                    margin: 30px 0;
                    color: #ffeb3b;
                }}
                button {{
                    background: #ff4081;
                    color: white;
                    border: none;
                    padding: 12px 30px;
                    border-radius: 25px;
                    cursor: pointer;
                    font-size: 1.1em;
                    margin: 10px;
                }}
                .tecnologias {{
                    margin-top: 30px;
                    padding: 20px;
                    background: rgba(255,255,255,0.2);
                    border-radius: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎯 Meu Primeiro Projeto Web</h1>
                <p>Demonstração para meus alunos usando Python + Flask</p>
                
                <div class="counter">
                    👁️ {contador} visitas
                </div>
                
                <button onclick="window.location.reload()">➕ Aumentar Contador</button>
                <button onclick="alert('Python + Flask + VSCode + GitHub + Vercel = ❤️')">ℹ️ Tecnologias</button>
                
                <div class="tecnologias">
                    <h3>🚀 Stack Completa:</h3>
                    <p>VSCode (código) → GitHub (versionamento) → Vercel (deploy)</p>
                </div>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)