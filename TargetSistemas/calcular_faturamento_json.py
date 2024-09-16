import json

def calcular_faturamento_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            
        valores = [item['valor'] for item in dados if item['valor'] > 0]
        
        if valores:
            menor_valor = min(valores)
            maior_valor = max(valores)
            media_mensal = sum(valores) / len(valores)
            dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
            
            print(f"Menor valor: R$ {menor_valor:.2f}")
            print(f"Maior valor: R$ {maior_valor:.2f}")
            print(f"Dias acima da média: {dias_acima_media}")
        else:
            print("Não há dados para processar.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")

if __name__ == "__main__":
    calcular_faturamento_json('dados.json')