# loja_logica.py
import banco_dados as bd

def adicionar_produto(nome, preco, quantidade):
    # O código está "espalhado": para criar um "produto", 
    # tenho que mexer em 3 listas diferentes.
    bd.produtos_nomes.append(nome)
    bd.produtos_precos.append(preco)
    bd.produtos_quantidades.append(quantidade)

def aplicar_desconto(indice, porcentagem):
    # Lógica frágil baseada em índices numéricos
    preco_atual = bd.produtos_precos[indice]
    novo_preco = preco_atual - (preco_atual * (porcentagem / 100))
    bd.produtos_precos[indice] = novo_preco
    print(f"Preço de {bd.produtos_nomes[indice]} alterado para R$ {novo_preco:.2f}")

def relatorio_estoque():
    print("--- RELATÓRIO ---")
    # Tenho que saber o tamanho de UMA das listas para percorrer TODAS
    for i in range(len(bd.produtos_nomes)):
        print(f"Produto: {bd.produtos_nomes[i]} | "
              f"Preço: R$ {bd.produtos_precos[i]} | "
              f"Qtd: {bd.produtos_quantidades[i]}")