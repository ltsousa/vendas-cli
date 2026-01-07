from typing import List, Dict, Tuple
from decimal import Decimal, InvalidOperation
from collections import defaultdict


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


def encontrar_produto_mais_vendido(vendas: List[Dict[str, str]]) -> Tuple[str, int, List[str]]:
    contagem = {}
    for venda in vendas:
        produto = venda.get('produto', '')
        if produto:
            contagem[produto] = contagem.get(produto, 0) + 1
    
    if not contagem:
        return '', 0, []
    
    maior_quantidade = max(contagem.values())
    produtos_empatados = [produto for produto, qtd in contagem.items() if qtd == maior_quantidade]
    produtos_empatados.sort()
    
    produto_principal = produtos_empatados[0] if produtos_empatados else ''
    
    return produto_principal, maior_quantidade, produtos_empatados

def processar_vendas_com_desconto(vendas: List[Dict]) -> List[Dict]:

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
    
    resultado.sort(key=lambda item: item['valor_total'], reverse=True)
    
    return resultado


def processar_vendas(vendas: List[Dict[str, str]]) -> Dict:
    total_por_produto = calcular_total_por_produto(vendas)
    valor_total = calcular_valor_total(vendas)
    produto_mais_vendido, quantidade, produtos_empatados = encontrar_produto_mais_vendido(vendas)
    
    resultado = {
        'total_por_produto': {k: str(v) for k, v in total_por_produto.items()},
        'valor_total': str(valor_total),
        'produto_mais_vendido': produto_mais_vendido,
        'quantidade_mais_vendido': quantidade
    }
    
    if len(produtos_empatados) > 1:
        resultado['produtos_empatados'] = produtos_empatados
    
    return resultado

