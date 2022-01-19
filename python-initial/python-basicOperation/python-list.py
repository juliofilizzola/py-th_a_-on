# vamos criar uma váriavel que vai armazenar varios elementos em uma lista

fruits = ["orange", "apple", "grape", "pineapple"]

print("posição 0 da lista:", fruits[0])  # o acesso é feito por indices iniciados em 0


print("posição -1 da lista:", fruits[-1]);

fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("pineapple") # remove 

fruits.extend(["pear", "melon", "kiwi"]) #adiciona uma lista na lista original

print(fruits)

print(fruits.index("apple")) # retorna o index desse elemento

fruits.sort() # ordena a lista

print(fruits)