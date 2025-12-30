import json
from typing import Dict


def formatar_texto(resultado: Dict) -> str:
    linhas = []
    linhas.append('=' * 50)
    linhas.append('RELATÓRIO DE VENDAS')
    linhas.append('=' * 50)
    linhas.append('')
    
    linhas.append('Total por Produto:')
    linhas.append('-' * 50)
    for produto, total in resultado['total_por_produto'].items():
        linhas.append(f'  {produto}: R$ {total}')
    linhas.append('')
    
    linhas.append(f"Valor Total: R$ {resultado['valor_total']}")
    linhas.append('')
    
    produto = resultado['produto_mais_vendido']
    quantidade = resultado['quantidade_mais_vendido']
    
    if produto:
        if 'produtos_empatados' in resultado and len(resultado['produtos_empatados']) > 1:
            produtos = resultado['produtos_empatados']
            produtos_str = ', '.join(produtos)
            linhas.append(f'Produtos Mais Vendidos (empatados): {produtos_str} ({quantidade} vendas cada)')
        else:
            linhas.append(f'Produto Mais Vendido: {produto} ({quantidade} vendas)')
    else:
        linhas.append('Produto Mais Vendido: N/A')
    
    linhas.append('=' * 50)
    
    return '\n'.join(linhas)


def formatar_json(resultado: Dict) -> str:
    return json.dumps(resultado, indent=2, ensure_ascii=False)


def gerar_saida(resultado: Dict, formato: str) -> str:
    if formato == 'json':
        return formatar_json(resultado)
    return formatar_texto(resultado)

