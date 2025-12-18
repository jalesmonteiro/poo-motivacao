# main.py
import loja_logica as logica

# Adicionando um novo produto
print("Adicionando Headset...")
logica.adicionar_produto("Headset Gamer", 250.00, 15)

# Aplicando desconto no Mouse (que sabemos "magicamente" que é o índice 1)
logica.aplicar_desconto(1, 10) 

# Gerando relatório
logica.relatorio_estoque()