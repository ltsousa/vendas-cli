from typing import List, Dict, Tuple
from decimal import Decimal, InvalidOperation


def calcular_total_por_produto(vendas: List[Dict[str, str]]) -> Dict[str, Decimal]:
    totais = {}
    for venda in vendas:
        produto = venda.get('produto', '')
        valor_str = venda.get('total_venda', venda.get('valor', '0'))
        
        try:
            valor = Decimal(valor_str)
            totais[produto] = totais.get(produto, Decimal('0')) + valor
        except (ValueError, TypeError, InvalidOperation):
            continue
    
    return totais


def calcular_valor_total(vendas: List[Dict[str, str]]) -> Decimal:
    total = Decimal('0')
    for venda in vendas:
        valor_str = venda.get('total_venda', venda.get('valor', '0'))
        try:
            total += Decimal(valor_str)
        except (ValueError, TypeError, InvalidOperation):
            continue
    return total


def encontrar_produto_mais_vendido(vendas: List[Dict[str, str]]) -> Tuple[str, int]:
    contagem = {}
    for venda in vendas:
        produto = venda.get('produto', '')
        if produto:
            contagem[produto] = contagem.get(produto, 0) + 1
    
    if not contagem:
        return '', 0
    
    produto_mais_vendido = max(contagem.items(), key=lambda x: x[1])
    return produto_mais_vendido


def processar_vendas(vendas: List[Dict[str, str]]) -> Dict:
    total_por_produto = calcular_total_por_produto(vendas)
    valor_total = calcular_valor_total(vendas)
    produto_mais_vendido, quantidade = encontrar_produto_mais_vendido(vendas)
    
    return {
        'total_por_produto': {k: str(v) for k, v in total_por_produto.items()},
        'valor_total': str(valor_total),
        'produto_mais_vendido': produto_mais_vendido,
        'quantidade_mais_vendido': quantidade
    }

