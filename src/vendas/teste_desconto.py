import sys
sys.path.insert(0, './src')

from vendas import vendas
from vendas.core import processar_vendas_com_desconto

print("Processar vendas com desconto")


resultado = processar_vendas_com_desconto(vendas)

print("Resultado:")
print("=" * 60)

for item in resultado:
    print(f"Produto: {item['produto']}")
    print(f"  Quantidade Total: {item['quantidade_total']}")
    print(f"  Valor Total: R$ {item['valor_total']:.2f}")
    
    if item['desconto_aplicado'] > 0:
        print(f"  Desconto Aplicado: R$ {item['desconto_aplicado']:.2f}")
    else:
        print("  Desconto Aplicado: Nenhum")
    print("-" * 60)