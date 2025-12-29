import pytest
import json
from vendas.output import formatar_texto, formatar_json, gerar_saida


def test_formatar_texto():
    resultado = {
        'total_por_produto': {'A': '100.50', 'B': '200.75'},
        'valor_total': '301.25',
        'produto_mais_vendido': 'B',
        'quantidade_mais_vendido': 5
    }
    saida = formatar_texto(resultado)
    
    assert 'RELATÓRIO DE VENDAS' in saida
    assert 'A: R$ 100.50' in saida
    assert 'B: R$ 200.75' in saida
    assert 'R$ 301.25' in saida
    assert 'Produto Mais Vendido: B (5 vendas)' in saida


def test_formatar_json():
    resultado = {
        'total_por_produto': {'A': '100.50'},
        'valor_total': '100.50',
        'produto_mais_vendido': 'A',
        'quantidade_mais_vendido': 1
    }
    saida = formatar_json(resultado)
    
    dados = json.loads(saida)
    assert dados['valor_total'] == '100.50'
    assert dados['produto_mais_vendido'] == 'A'


def test_gerar_saida_texto():
    resultado = {
        'total_por_produto': {'A': '100.50'},
        'valor_total': '100.50',
        'produto_mais_vendido': 'A',
        'quantidade_mais_vendido': 1
    }
    saida = gerar_saida(resultado, 'text')
    assert 'RELATÓRIO DE VENDAS' in saida


def test_gerar_saida_json():
    resultado = {
        'total_por_produto': {'A': '100.50'},
        'valor_total': '100.50',
        'produto_mais_vendido': 'A',
        'quantidade_mais_vendido': 1
    }
    saida = gerar_saida(resultado, 'json')
    dados = json.loads(saida)
    assert 'valor_total' in dados

