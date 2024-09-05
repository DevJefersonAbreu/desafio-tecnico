
# 3. Programa para calcular dados do faturamento diário
import json

# Carregar o arquivo JSON
with open('faturamento.json') as file:
    faturamento_diario = json.load(file)

# Inicializando variáveis
faturamentos = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)

# Calcula dias acima da média
dias_acima_da_media = len([dia for dia in faturamentos if dia > media_mensal])

# Exibe os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
