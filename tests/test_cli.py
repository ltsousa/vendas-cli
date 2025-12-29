import pytest
import sys
from unittest.mock import patch, mock_open, MagicMock
from vendas.cli import main


def test_cli_arquivo_nao_encontrado(capsys):
    with patch('vendas.cli.parse_args') as mock_args:
        mock_args.return_value.arquivo = '/caminho/inexistente.csv'
        mock_args.return_value.format = 'text'
        mock_args.return_value.start = None
        mock_args.return_value.end = None
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 1


def test_cli_arquivo_vazio(capsys):
    with patch('vendas.cli.parse_args') as mock_args, \
         patch('vendas.cli.Path') as mock_path, \
         patch('vendas.cli.parse_csv') as mock_parse:
        
        mock_path.return_value.exists.return_value = True
        mock_args.return_value.arquivo = 'vendas.csv'
        mock_args.return_value.format = 'text'
        mock_args.return_value.start = None
        mock_args.return_value.end = None
        mock_parse.return_value = []
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 1


def test_cli_sucesso(capsys):
    with patch('vendas.cli.parse_args') as mock_args, \
         patch('vendas.cli.Path') as mock_path, \
         patch('vendas.cli.parse_csv') as mock_parse, \
         patch('vendas.cli.filtrar_por_data') as mock_filtrar, \
         patch('vendas.cli.processar_vendas') as mock_processar, \
         patch('vendas.cli.gerar_saida') as mock_saida:
        
        mock_path.return_value.exists.return_value = True
        mock_args.return_value.arquivo = 'vendas.csv'
        mock_args.return_value.format = 'text'
        mock_args.return_value.start = None
        mock_args.return_value.end = None
        mock_parse.return_value = [{'produto': 'A', 'valor': '100', 'data': '2025-01-01'}]
        mock_filtrar.return_value = [{'produto': 'A', 'valor': '100', 'data': '2025-01-01'}]
        mock_processar.return_value = {'valor_total': '100'}
        mock_saida.return_value = 'Relatório de Vendas'
        
        main()
        
        captured = capsys.readouterr()
        assert 'Relatório de Vendas' in captured.out

