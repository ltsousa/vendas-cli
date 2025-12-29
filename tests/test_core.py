import pytest
from decimal import Decimal
from vendas.core import (
    calcular_total_por_produto,
    calcular_valor_total,
    encontrar_produto_mais_vendido,
    processar_vendas
)


def test_calcular_total_por_produto():
    vendas = [
        {'produto': 'A', 'valor': '100.50'},
        {'produto': 'A', 'valor': '50.25'},
        {'produto': 'B', 'valor': '200.00'}
    ]
    resultado = calcular_total_por_produto(vendas)
    assert resultado['A'] == Decimal('150.75')
    assert resultado['B'] == Decimal('200.00')


def test_calcular_valor_total():
    vendas = [
        {'produto': 'A', 'valor': '100.50'},
        {'produto': 'B', 'valor': '200.75'},
        {'produto': 'C', 'valor': '50.25'}
    ]
    resultado = calcular_valor_total(vendas)
    assert resultado == Decimal('351.50')


def test_encontrar_produto_mais_vendido():
    vendas = [
        {'produto': 'A', 'valor': '100'},
        {'produto': 'A', 'valor': '100'},
        {'produto': 'B', 'valor': '200'},
        {'produto': 'A', 'valor': '100'}
    ]
    produto, quantidade = encontrar_produto_mais_vendido(vendas)
    assert produto == 'A'
    assert quantidade == 3


def test_encontrar_produto_mais_vendido_vazio():
    vendas = []
    produto, quantidade = encontrar_produto_mais_vendido(vendas)
    assert produto == ''
    assert quantidade == 0


def test_processar_vendas():
    vendas = [
        {'produto': 'A', 'valor': '100.50'},
        {'produto': 'A', 'valor': '50.25'},
        {'produto': 'B', 'valor': '200.00'},
        {'produto': 'B', 'valor': '200.00'},
        {'produto': 'B', 'valor': '150.00'}
    ]
    resultado = processar_vendas(vendas)
    
    assert 'total_por_produto' in resultado
    assert 'valor_total' in resultado
    assert 'produto_mais_vendido' in resultado
    assert 'quantidade_mais_vendido' in resultado
    assert resultado['produto_mais_vendido'] == 'B'
    assert resultado['quantidade_mais_vendido'] == 3


def test_calcular_total_por_produto_valor_invalido():
    vendas = [
        {'produto': 'A', 'valor': '100.50'},
        {'produto': 'A', 'valor': 'invalido'},
        {'produto': 'B', 'valor': '200.00'}
    ]
    resultado = calcular_total_por_produto(vendas)
    assert resultado['A'] == Decimal('100.50')
    assert resultado['B'] == Decimal('200.00')


def test_calcular_valor_total_valor_invalido():
    vendas = [
        {'produto': 'A', 'valor': '100.50'},
        {'produto': 'B', 'valor': 'invalido'},
        {'produto': 'C', 'valor': '50.25'}
    ]
    resultado = calcular_valor_total(vendas)
    assert resultado == Decimal('150.75')


def test_calcular_total_por_produto_com_total_venda():
    vendas = [
        {'produto': 'A', 'total_venda': '100.50'},
        {'produto': 'A', 'total_venda': '50.25'},
        {'produto': 'B', 'total_venda': '200.00'}
    ]
    resultado = calcular_total_por_produto(vendas)
    assert resultado['A'] == Decimal('150.75')
    assert resultado['B'] == Decimal('200.00')


def test_calcular_valor_total_com_total_venda():
    vendas = [
        {'produto': 'A', 'total_venda': '100.50'},
        {'produto': 'B', 'total_venda': '200.75'},
        {'produto': 'C', 'total_venda': '50.25'}
    ]
    resultado = calcular_valor_total(vendas)
    assert resultado == Decimal('351.50')

