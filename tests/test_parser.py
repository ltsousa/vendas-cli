import pytest
import tempfile
import os
from vendas.parser import parse_csv, filtrar_por_data


def test_parse_csv():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        f.write('produto,valor,data\n')
        f.write('Produto A,100.50,2025-01-15\n')
        f.write('Produto B,200.75,2025-02-20\n')
        temp_path = f.name
    
    try:
        vendas = parse_csv(temp_path)
        assert len(vendas) == 2
        assert vendas[0]['produto'] == 'Produto A'
        assert vendas[0]['valor'] == '100.50'
    finally:
        os.unlink(temp_path)


def test_filtrar_por_data_sem_filtro():
    vendas = [
        {'produto': 'A', 'valor': '100', 'data': '2025-01-15'},
        {'produto': 'B', 'valor': '200', 'data': '2025-02-20'}
    ]
    resultado = filtrar_por_data(vendas, None, None)
    assert len(resultado) == 2


def test_filtrar_por_data_com_start():
    vendas = [
        {'produto': 'A', 'valor': '100', 'data': '2025-01-15'},
        {'produto': 'B', 'valor': '200', 'data': '2025-02-20'},
        {'produto': 'C', 'valor': '300', 'data': '2024-12-10'}
    ]
    resultado = filtrar_por_data(vendas, '2025-01-01', None)
    assert len(resultado) == 2
    assert all('2025' in v['data'] for v in resultado)


def test_filtrar_por_data_com_end():
    vendas = [
        {'produto': 'A', 'valor': '100', 'data': '2025-01-15'},
        {'produto': 'B', 'valor': '200', 'data': '2025-02-20'},
        {'produto': 'C', 'valor': '300', 'data': '2025-03-30'}
    ]
    resultado = filtrar_por_data(vendas, None, '2025-02-28')
    assert len(resultado) == 2


def test_filtrar_por_data_com_intervalo():
    vendas = [
        {'produto': 'A', 'valor': '100', 'data': '2025-01-15'},
        {'produto': 'B', 'valor': '200', 'data': '2025-02-20'},
        {'produto': 'C', 'valor': '300', 'data': '2025-03-30'}
    ]
    resultado = filtrar_por_data(vendas, '2025-01-01', '2025-02-28')
    assert len(resultado) == 2


def test_filtrar_por_data_sem_campo_data():
    vendas = [
        {'produto': 'A', 'valor': '100'},
        {'produto': 'B', 'valor': '200', 'data': '2025-02-20'}
    ]
    resultado = filtrar_por_data(vendas, '2025-01-01', None)
    assert len(resultado) == 1


def test_filtrar_por_data_data_invalida():
    vendas = [
        {'produto': 'A', 'valor': '100', 'data': 'data-invalida'},
        {'produto': 'B', 'valor': '200', 'data': '2025-02-20'}
    ]
    resultado = filtrar_por_data(vendas, '2025-01-01', None)
    assert len(resultado) == 1

