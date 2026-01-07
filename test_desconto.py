#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'src')

# Importar dados do arquivo vendas.py
exec(open('vendas.py').read())

# Função correta que deve ser implementada
from collections import defaultdict
from decimal import Decimal
from typing import List, Dict


def processar_vendas_com_desconto(vendas: List[Dict]) -> List[Dict]:
    """
    Agrupa vendas por produto, calcula totais, aplica desconto
    e retorna ordenado por valor total (desc).
    """
    produtos = defaultdict(lambda: {'quantidade': 0, 'valor_total': Decimal('0')})
    
    for venda in vendas:
        produto = venda['produto']
        quantidade = int(venda['quantidade'])
        preco_unitario = Decimal(str(venda['preco_unitario']))
        
        valor_venda = preco_unitario * quantidade
        
        produtos[produto]['quantidade'] += quantidade
        produtos[produto]['valor_total'] += valor_venda
    
    resultado = []
    for produto, dados in produtos.items():
        quantidade_total = dados['quantidade']
        valor_total = dados['valor_total']
        
        if quantidade_total >= 5:
            desconto = valor_total * Decimal('0.10')
            valor_final = valor_total - desconto
        else:
            desconto = Decimal('0')
            valor_final = valor_total
        
        resultado.append({
            'produto': produto,
            'quantidade_total': quantidade_total,
            'valor_total': float(valor_final),
            'desconto_aplicado': float(desconto)
        })
    
    resultado.sort(key=lambda x: x['valor_total'], reverse=True)
    
    return resultado


# Executar teste
print('=== TESTANDO FUNÇÃO processar_vendas_com_desconto ===\n')

resultado = processar_vendas_com_desconto(vendas)

print('RESULTADO:')
print('=' * 60)
for item in resultado:
    print(f"Produto: {item['produto']}")
    print(f"  Quantidade Total: {item['quantidade_total']}")
    print(f"  Valor Total: R$ {item['valor_total']:.2f}")
    print(f"  Desconto Aplicado: R$ {item['desconto_aplicado']:.2f}")
    print('-' * 60)

print('\n=== VALIDAÇÃO ===')

# Validar Camiseta (quantidade >= 5 deve ter desconto)
camiseta = next((x for x in resultado if x['produto'] == 'Camiseta'), None)
if camiseta:
    assert camiseta['quantidade_total'] == 5, f"Esperado 5, obtido {camiseta['quantidade_total']}"
    assert camiseta['valor_total'] == 225.0, f"Esperado 225.0, obtido {camiseta['valor_total']}"
    assert camiseta['desconto_aplicado'] == 25.0, f"Esperado 25.0, obtido {camiseta['desconto_aplicado']}"
    print('✅ Camiseta: OK (quantidade=5, desconto de 10% aplicado)')
else:
    print('❌ Camiseta: NÃO ENCONTRADA')

# Validar ordenação (Tênis deve ser primeiro)
assert resultado[0]['produto'] == 'Tênis', f"Esperado Tênis primeiro, obtido {resultado[0]['produto']}"
print('✅ Ordenação: OK (Tênis primeiro por valor)')

print('\n=== TODOS OS TESTES PASSARAM! ===')
