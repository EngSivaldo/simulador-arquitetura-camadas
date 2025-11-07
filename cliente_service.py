# cliente_service.py
from cliente_repository import ClienteRepository

class ClienteService:
    # Injeção de dependência (o Service recebe a instância do Repository)
    def __init__(self, repository: ClienteRepository):
        self._repository = repository

    def cadastrar_novo(self, novo_cliente_data):
        nome = novo_cliente_data.get("nome")
        cpf = novo_cliente_data.get("cpf")
        
        # **AQUI ESTÁ A LÓGICA DE NEGÓCIO (Validações)**
        if not nome or len(nome) < 3:
            raise ValueError("NEGÓCIO: Nome do cliente inválido ou muito curto.")
        
        if not self._validar_cpf(cpf):
            raise ValueError("NEGÓCIO: CPF inválido. Cadastro negado.")

        if self._repository.buscar_por_cpf(cpf):
            raise ValueError("NEGÓCIO: Cliente com este CPF já está cadastrado.")

        print("NEGÓCIO: Validações OK. Chamando a Camada de Persistência...")
        
        # Chamada à Camada de Persistência
        return self._repository.salvar(novo_cliente_data)
    
    def _validar_cpf(self, cpf):
        # Simulação de validação
        return isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit()