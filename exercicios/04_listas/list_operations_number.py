"""
Objetivo:
    Realizar diversas operações com listas.

Etapas:
    1. Criar duas listas numéricas;
    2. Realizar união e repetição;
    3. Utilizar funções: max(), min(), sum(), sorted(), reversed();
    4. Aplicar métodos: append, insert, remove, pop, count, index, copy, extend.
"""


lista_01 = [1, 2, 3, 4]
lista_02 = [5, 6, 7, 8]

#União e a repetição
uniao = lista_01 + lista_02
print(uniao)

repeticao = uniao * 2
print(repeticao)

#Uso das funções max(), min(), sum(), sorted() e reversed()

print(f"O maior número da lista é {max(uniao)}")
print(f"O menor número da lista é {min(uniao)}")
print(f"A soma de todos os números da lista {sum(uniao)}")
print("Lista ordenada", sorted(uniao))
print("Lista invertida", list(reversed(uniao)))

#.append()
uniao.append(5)
print(uniao)

#.insert()
uniao.insert(3, 6)
print(uniao)

#.remove()
uniao.remove(2)
print(uniao)

#.pop()
uniao.pop(1)
print(uniao)

#.count()
print(uniao.count(6))

#.index()
print(uniao.index(8))

#.copy
copia = uniao.copy()
copia.append(4)

print("Lista original", uniao)
print("Cópia", copia)

#.extend()
uniao.extend(copia)
print(uniao)