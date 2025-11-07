# app.py
from flask import Flask, request, jsonify
from cliente_service import ClienteService
from cliente_repository import ClienteRepository

# 1. Configuração e Instanciação
app = Flask(__name__)
# Instancia as dependências (poderia ser feito com um framework de injeção mais robusto)
cliente_repository = ClienteRepository()
cliente_service = ClienteService(cliente_repository)

@app.route('/api/clientes', methods=['POST'])
def criar_cliente():
    
    cliente_data = request.json
    
    try:
        print("\nAPRESENTAÇÃO: Recebida requisição para criar cliente.")
        
        # Chamada à Camada de Negócio (Service)
        cliente_salvo = cliente_service.cadastrar_novo(cliente_data)
        
        # Retorna o resultado com status 201 Created
        return jsonify(cliente_salvo), 201
        
    except ValueError as e:
        # Se o Service lançar um erro de validação (Negócio)
        # Retorna o erro com status 400 Bad Request
        return jsonify({"erro": str(e)}), 400

# Execução (Para testar, rode este arquivo: python app.py)
if __name__ == '__main__':
    # Exemplo de uso
    cliente_teste = {"nome": "Maria Silva", "cpf": "12345678901"}
    
    # Simulação da chamada (em um ambiente real, seria via HTTP)
    with app.test_client() as client:
        # Requisição Válida
        response = client.post('/api/clientes', json=cliente_teste)
        print(f"Resposta API (Status {response.status_code}): {response.get_json()}")
        
        # Requisição Inválida (Nome muito curto, violando regra de negócio)
        cliente_invalido = {"nome": "M", "cpf": "98765432109"}
        response_erro = client.post('/api/clientes', json=cliente_invalido)
        print(f"\nResposta API (Status {response_erro.status_code}): {response_erro.get_json()}")
        
    # app.run(debug=True) # Descomente para rodar o servidor Flask de fato