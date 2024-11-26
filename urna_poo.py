import csv
import pickle
import os

class UrnaEletronica:
    def __init__(self):
        self.eleitores = {}
        self.candidatos = {}
        self.votos = {}
        self.carregar_dados()

    def carregar_dados(self):
        # Carrega dados de eleitores e candidatos de arquivos CSV
        try:
            with open('eleitores.csv', 'r', encoding='utf-8') as f:
                leitor = csv.DictReader(f)
                for linha in leitor:
                    self.eleitores[linha["Título"]] = Eleitor(linha["Nome completo"], linha["RG"], linha["CPF"])
            
            with open('candidatos.csv', 'r', encoding='utf-8') as f:
                leitor = csv.DictReader(f)
                for linha in leitor:
                    self.candidatos[linha["Número"]] = Candidato(linha["Número"], linha["Nome completo"])
        except FileNotFoundError as e:
            print(f"Erro ao carregar dados: {e}")

    def registrar_voto(self, numero):
        # Registra o voto no arquivo .pkl
        arquivo_votos = "votos.pkl"

        # Verifica se o arquivo já existe
        if not os.path.exists(arquivo_votos):
            # Cria um arquivo inicial vazio se ele não existir
            with open(arquivo_votos, "wb") as f:
                pickle.dump({}, f)  # Inicializa com um dicionário vazio

        # Carrega os votos existentes
        with open(arquivo_votos, "rb") as f:
            try:
                self.votos = pickle.load(f)  # Carrega os votos
            except EOFError:
                self.votos = {}  # Inicializa vazio se o arquivo estiver corrompido ou vazio

        # Registra o voto
        self.votos[numero] = self.votos.get(numero, 0) + 1

        # Salva os votos atualizados
        with open(arquivo_votos, "wb") as f:
            pickle.dump(self.votos, f)

    def verificar_eleitor(self, titulo):
        # Verifica se o título corresponde a um eleitor válido
        return self.eleitores.get(titulo)

    def verificar_candidato(self, numero):
        # Verifica se o número corresponde a um candidato válido
        return self.candidatos.get(numero)

class Eleitor:
    def __init__(self, nome, rg, cpf):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf

class Candidato:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome