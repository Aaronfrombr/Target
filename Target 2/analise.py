data = {
    "faturamento": {
        "1": 5000.0,
        "2": 7000.0,
        "3": 0.0,
        "4": 6000.0,
        "5": 8000.0
    }
}

faturamento = data['faturamento']
valores = [v for v in faturamento.values() if v > 0]

menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)

dias_acima_media = sum(1 for v in valores if v > media)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Número de dias acima da média: {dias_acima_media}")
