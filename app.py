from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Tecnologias disponíveis por grau
tecnologias_grau_1 = [
    "Telhado retrátil simples", "Painéis solares básicos", "Sistema de som analógico",
    "Assentos retráteis", "Iluminação convencional", "Banheiros ecológicos",
    "Piso antiderrapante", "Wi-Fi gratuito limitado", "Placar eletrônico simples",
    "Sistema de ventilação natural"
]

tecnologias_grau_2 = [
    "Telhado retrátil automatizado", "Painéis solares avançados", "Som digital de alta qualidade",
    "Assentos ergonômicos", "Iluminação LED inteligente", "Banheiros com autolimpeza",
    "Piso inteligente com aquecimento", "Wi-Fi de alta velocidade", "Placar LED interativo",
    "Sistema de ar-condicionado central"
]

tecnologias_grau_3 = [
    "Cobertura 100% solar com bateria", "IA para controle de multidões", "Tela 360° em LED no teto",
    "Assentos com vibração e tela", "Iluminação adaptativa por jogo", "Conectividade 5G total",
    "Segurança com reconhecimento facial", "Realidade aumentada para torcedores",
    "Banheiros com assistente virtual", "Sistema de som 4D com imersão"
]

# Custo base por capacidade (em milhões)
custos_base = {
    5000: 15,
    10000: 25,
    15000: 35,
    20000: 45,
    25000: 55,
    30000: 65,
    40000: 80,
    50000: 95,
    60000: 110,
    70000: 125,
    80000: 140,
    90000: 155,
    100000: 170
}

# Multiplicador por grau de tecnologia
multiplicadores = {
    1: 1.0,
    2: 1.3,
    3: 1.7
}

@app.route("/")
def home():
    return "Sistema de construção de estádios ativo!"

@app.route("/estadio", methods=["POST"])
def construir_estadio():
    data = request.get_json()
    nome = data.get("nome")
    capacidade = int(data.get("capacidade"))
    grau = int(data.get("grau_tecnologia"))
    estado = data.get("estado")
    cidade = data.get("cidade")

    if capacidade not in custos_base or grau not in multiplicadores:
        return jsonify({"erro": "Capacidade ou grau inválido"}), 400

    custo_base = custos_base[capacidade]
    custo_total = round(custo_base * multiplicadores[grau], 2)

    if grau == 1:
        tecnologia = random.choice(tecnologias_grau_1)
    elif grau == 2:
        tecnologia = random.choice(tecnologias_grau_2)
    else:
        tecnologia = random.choice(tecnologias_grau_3)

    return jsonify({
        "nome": nome,
        "cidade": cidade,
        "estado": estado,
        "capacidade": capacidade,
        "grau_tecnologia": grau,
        "custo_total": custo_total,
        "tecnologia_principal": tecnologia
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
