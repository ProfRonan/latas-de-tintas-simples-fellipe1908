print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
qtd_de_latas = metros_quadrados // 54
qtd_de_latas2 = metros_quadrados / 54
valor_total = 0
if qtd_de_latas2 > qtd_de_latas :
    lt = qtd_de_latas + 1
    v = lt * 80
    print(f"Serão necessárias {lt} latas totalizando R$ {v}")
else:
    qtd_de_latas
    valor = qtd_de_latas * 80
    print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor}")