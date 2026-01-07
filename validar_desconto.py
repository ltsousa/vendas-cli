#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'src')

from vendas import vendas
from vendas.core import processar_vendas_com_desconto

print('=' * 70)
print('VALIDAÇÃO DA FUNÇÃO processar_vendas_com_desconto')
print('=' * 70)
print()

# Executar função
resultado = processar_vendas_com_desconto(vendas)

print('RESULTADO OBTIDO:')
print('-' * 70)
for item in resultado:
    print(f"Produto: {item['produto']}")
    print(f"  Quantidade Total: {item['quantidade_total']}")
    print(f"  Valor Total: R$ {item['valor_total']:.2f}")
    print(f"  Desconto Aplicado: R$ {item['desconto_aplicado']:.2f}")
    print()
print('-' * 70)
print()

# Validações
print('VALIDANDO REQUISITOS:')
print('-' * 70)

erros = []

# 1. Verificar se agrupa corretamente por produto
produtos_esperados = {'Camiseta', 'Calça', 'Tênis'}
produtos_obtidos = {item['produto'] for item in resultado}

if produtos_obtidos == produtos_esperados:
    print('✅ 1. Agrupamento por produto: OK')
else:
    print(f'❌ 1. Agrupamento por produto: FALHOU')
    print(f'   Esperado: {produtos_esperados}')
    print(f'   Obtido: {produtos_obtidos}')
    erros.append('Agrupamento incorreto')

# 2. Verificar quantidade total (Camiseta = 3 + 2 = 5)
camiseta = next((x for x in resultado if x['produto'] == 'Camiseta'), None)
if camiseta and camiseta['quantidade_total'] == 5:
    print('✅ 2. Quantidade total (Camiseta): OK (3 + 2 = 5)')
else:
    print(f'❌ 2. Quantidade total (Camiseta): FALHOU')
    print(f'   Esperado: 5, Obtido: {camiseta["quantidade_total"] if camiseta else "N/A"}')
    erros.append('Quantidade total incorreta')

# 3. Verificar valor total (Camiseta = 3*50 + 2*50 = 250)
if camiseta:
    valor_sem_desconto = camiseta['valor_total'] + camiseta['desconto_aplicado']
    if abs(valor_sem_desconto - 250.0) < 0.01:
        print('✅ 3. Valor total (Camiseta): OK (150 + 100 = 250)')
    else:
        print(f'❌ 3. Valor total (Camiseta): FALHOU')
        print(f'   Esperado: 250.0, Obtido: {valor_sem_desconto}')
        erros.append('Valor total incorreto')

# 4. Verificar desconto (quantidade >= 5 deve ter 10%)
if camiseta and camiseta['quantidade_total'] >= 5:
    desconto_esperado = 250.0 * 0.10
    if abs(camiseta['desconto_aplicado'] - desconto_esperado) < 0.01:
        print('✅ 4. Desconto 10% (Camiseta): OK (250 * 10% = 25)')
    else:
        print(f'❌ 4. Desconto 10% (Camiseta): FALHOU')
        print(f'   Esperado: {desconto_esperado}, Obtido: {camiseta["desconto_aplicado"]}')
        erros.append('Desconto incorreto')
    
    valor_final_esperado = 250.0 - 25.0
    if abs(camiseta['valor_total'] - valor_final_esperado) < 0.01:
        print('✅ 4.1. Valor final com desconto: OK (250 - 25 = 225)')
    else:
        print(f'❌ 4.1. Valor final com desconto: FALHOU')
        print(f'   Esperado: {valor_final_esperado}, Obtido: {camiseta["valor_total"]}')
        erros.append('Valor final incorreto')
else:
    print(f'❌ 4. Desconto: FALHOU (quantidade < 5 ou produto não encontrado)')
    erros.append('Desconto não aplicado')

# 5. Verificar produtos sem desconto (quantidade < 5)
tenis = next((x for x in resultado if x['produto'] == 'Tênis'), None)
calca = next((x for x in resultado if x['produto'] == 'Calça'), None)

if tenis and tenis['quantidade_total'] < 5 and tenis['desconto_aplicado'] == 0:
    print('✅ 5. Sem desconto (Tênis): OK (quantidade < 5)')
else:
    print(f'❌ 5. Sem desconto (Tênis): FALHOU')
    erros.append('Desconto aplicado incorretamente')

if calca and calca['quantidade_total'] < 5 and calca['desconto_aplicado'] == 0:
    print('✅ 5.1. Sem desconto (Calça): OK (quantidade < 5)')
else:
    print(f'❌ 5.1. Sem desconto (Calça): FALHOU')
    erros.append('Desconto aplicado incorretamente')

# 6. Verificar ordenação (maior valor primeiro)
valores = [item['valor_total'] for item in resultado]
valores_ordenados = sorted(valores, reverse=True)

if valores == valores_ordenados:
    print('✅ 6. Ordenação por valor total (desc): OK')
    print(f'   Ordem: {[item["produto"] for item in resultado]}')
else:
    print(f'❌ 6. Ordenação por valor total (desc): FALHOU')
    print(f'   Esperado ordem decrescente por valor')
    print(f'   Obtido: {valores}')
    erros.append('Ordenação incorreta')

print('-' * 70)
print()

# Resultado final
if not erros:
    print('🎉 TODOS OS TESTES PASSARAM!')
    print('=' * 70)
    print('✅ A função está CORRETA e atende todos os requisitos:')
    print('   1. Agrupa vendas por produto')
    print('   2. Calcula quantidade total')
    print('   3. Calcula valor total')
    print('   4. Aplica 10% desconto se quantidade >= 5')
    print('   5. Retorna ordenado por valor total (desc)')
    print('=' * 70)
else:
    print('❌ ALGUNS TESTES FALHARAM:')
    for erro in erros:
        print(f'   - {erro}')
    print('=' * 70)
