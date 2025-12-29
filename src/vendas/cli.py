import sys
import logging
from pathlib import Path
from .parser import parse_csv, parse_args, filtrar_por_data
from .core import processar_vendas
from .output import gerar_saida


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    try:
        args = parse_args()
        
        arquivo = Path(args.arquivo)
        if not arquivo.exists():
            logger.error(f'Arquivo não encontrado: {args.arquivo}')
            sys.exit(1)
        
        logger.info(f'Processando arquivo: {args.arquivo}')
        vendas = parse_csv(str(arquivo))
        
        if not vendas:
            logger.warning('Nenhuma venda encontrada no arquivo')
            sys.exit(1)
        
        vendas_filtradas = filtrar_por_data(vendas, args.start, args.end)
        
        if not vendas_filtradas:
            logger.warning('Nenhuma venda encontrada no período especificado')
            sys.exit(1)
        
        resultado = processar_vendas(vendas_filtradas)
        saida = gerar_saida(resultado, args.format)
        
        print(saida)
        
    except Exception as e:
        logger.error(f'Erro ao processar: {e}', exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()

