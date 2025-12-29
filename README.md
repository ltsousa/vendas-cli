# Gerador de Relatório de Vendas Avançado

CLI em Python para processar arquivos CSV de vendas e gerar relatórios em formato texto ou JSON.

## Instalação

```bash
pip install .
```

Ou em modo desenvolvimento:

```bash
pip install -e .
```

## Uso

### Formato texto (padrão)

```bash
vendas-cli vendas_sample.csv
```

### Formato JSON

```bash
vendas-cli vendas_sample.csv --format json
```

### Filtrar por período

```bash
vendas-cli vendas_sample.csv --format text --start 2025-01-01 --end 2025-03-31
```

### Filtrar por período em JSON

```bash
vendas-cli vendas_sample.csv --format json --start 2025-01-01 --end 2025-03-31
```

## Formato do CSV

O arquivo CSV deve conter as seguintes colunas obrigatórias:
- `produto`: Nome do produto
- `total_venda` ou `valor`: Valor total da venda (número)
- `data`: Data da venda no formato YYYY-MM-DD

O sistema suporta ambos os formatos:
- `total_venda` (formato atual)
- `valor` (formato legado, mantido para compatibilidade)

Exemplo:

```csv
order_id,data,produto,categoria,quantidade,preco_unitario,custo_unitario,receita_bruta,desconto_valor,total_venda,lucro
V000737,2024-01-01,Óleo de Milho 900ml,Alimentos Básicos,5,115.69,84.17,578.45,57.85,520.6,99.75
V000533,2024-01-01,Refrigerante Guaraná 2L,Bebidas,2,119.5,93.43,239.0,23.9,215.1,28.24
```

## Funcionalidades

- Total de vendas por produto
- Valor total de todas as vendas
- Produto mais vendido
- Filtro por intervalo de datas
- Saída em texto formatado ou JSON

## Testes

```bash
pytest
```

Para verificar cobertura de testes:

```bash
pytest --cov=src/vendas --cov-report=html
```

## Estrutura do Projeto

```
.
├── src/
│   └── vendas/
│       ├── __init__.py
│       ├── parser.py      # Parsing de CSV e argumentos
│       ├── core.py        # Lógica de cálculos
│       ├── output.py      # Formatação de saída
│       └── cli.py         # Ponto de entrada
├── tests/
│   ├── test_parser.py
│   ├── test_core.py
│   └── test_output.py
├── pyproject.toml
├── pytest.ini
└── README.md
```

