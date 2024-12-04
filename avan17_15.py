class veiculo:
    def __init__(self, placa, modelo, ano, km):
        self.placa= placa
        self.modelo = modelo
        self.ano = ano
        self.km = km

    def exibe(self):
        print(f"Veiculo placa {self.placa}")
        print(f"{self.modelo}, ano: {self.ano} - Km: {self.km}")


    def __str__(self):
        s= f"Veiculo placa {self.placa}"
        s+= f"{self.modelo}, ano: {self.ano} - Km: {self.km}"
        return s

    def __repr__(self):
        s =     'instancia da classe Veiculo, \n'
        s+=     ' carregada com os seguintes dados:\n'
        s+= f'  .{self.placa}\n'
        s += f'  .{self.modelo}\n'
        s += f'  .{self.ano}\n'
        s += f'  .{self.km}\n'
        return s

    def __len__(self):
        return 1