import csv
import argparse
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path


def parse_csv(file_path: str) -> List[Dict[str, str]]:
    vendas = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vendas.append(row)
    return vendas


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Gerador de Relatório de Vendas'
    )
    parser.add_argument(
        'arquivo',
        type=str,
        help='Caminho do arquivo CSV de vendas'
    )
    parser.add_argument(
        '--format',
        choices=['text', 'json'],
        default='text',
        help='Formato de saída (padrão: text)'
    )
    parser.add_argument(
        '--start',
        type=str,
        help='Data inicial (YYYY-MM-DD)'
    )
    parser.add_argument(
        '--end',
        type=str,
        help='Data final (YYYY-MM-DD)'
    )
    return parser.parse_args()


def filtrar_por_data(
    vendas: List[Dict[str, str]],
    start: Optional[str],
    end: Optional[str]
) -> List[Dict[str, str]]:
    if not start and not end:
        return vendas
    
    resultado = []
    for venda in vendas:
        data_str = venda.get('data', '')
        if not data_str:
            continue
        
        try:
            data_venda = datetime.strptime(data_str, '%Y-%m-%d').date()
            
            if start:
                data_start = datetime.strptime(start, '%Y-%m-%d').date()
                if data_venda < data_start:
                    continue
            
            if end:
                data_end = datetime.strptime(end, '%Y-%m-%d').date()
                if data_venda > data_end:
                    continue
            
            resultado.append(venda)
        except ValueError:
            continue
    
    return resultado

