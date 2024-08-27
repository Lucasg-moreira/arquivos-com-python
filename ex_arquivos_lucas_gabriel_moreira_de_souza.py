def processar_mercadorias(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            mercadorias = []
            for linha in arquivo:
                item, preco = linha.strip().split(' = ')
                mercadorias.append((item, float(preco)))
        
        item_mais_caro = max(mercadorias, key=lambda x: x[1])
        item_mais_barato = min(mercadorias, key=lambda x: x[1])
        
        media_precos = sum(preco for _, preco in mercadorias) / len(mercadorias)
        
        print(f"Item mais caro: {item_mais_caro[0]} (custa R$ {item_mais_caro[1]:.2f})")
        print(f"Item mais barato: {item_mais_barato[0]} (custa R$ {item_mais_barato[1]:.2f})")
        print(f"Média de preços: {media_precos:.2f}")

    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    processar_mercadorias('mercadorias.txt')
