# cliente_repository.py

class ClienteRepository:
    # Simulação do 'banco de dados'
    _clientes_db = []
    _next_id = 1

    def salvar(self, cliente_data):
        # Cria um novo dicionário de cliente com ID e salva
        cliente = {
            "id": self._next_id,
            "nome": cliente_data.get("nome"),
            "cpf": cliente_data.get("cpf")
        }
        self._clientes_db.append(cliente)
        self._next_id += 1
        
        print(f"PERSISTÊNCIA: Cliente {cliente['nome']} salvo no 'banco'.")
        return cliente

    def buscar_por_cpf(self, cpf):
        # Simula uma consulta no banco
        for cliente in self._clientes_db:
            if cliente["cpf"] == cpf:
                return cliente
        return None