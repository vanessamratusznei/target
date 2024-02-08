'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;
'''

import json

with open('faturamento_mensal.json', 'r') as arquivo:
    faturamento_mensal = json.load(arquivo)

menor_valor = min(faturamento_mensal)
maior_valor = max(faturamento_mensal)

dias_com_faturamento = [valor for valor in faturamento_mensal if valor > 0] #desconsiderando dias sem faturamento
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)
