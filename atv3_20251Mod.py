def f_preencherlista(n:int)->list:
	lst_dados = list()
	lst_geral = list()

	for i in range (n):
		nome = str(input())
		peso = float(input())
		altura = float(input())

		lst_dados = [nome, peso, altura]
		lst_geral.append(lst_dados)

	return lst_geral