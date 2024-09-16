def calcular_percentuais(faturamento):
    total = sum(faturamento.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentuais

def imprimir_percentuais(percentuais):
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
    }
    
    percentuais = calcular_percentuais(faturamento)
    imprimir_percentuais(percentuais)
