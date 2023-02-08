numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10 #actualizar
print(numbers)

numbers[-1] = 10    #actualizar
print(numbers)

#crear un elemento hacia la lista y agregarlo
numbers.append(700) #agrego un elemento al final
print(numbers)

#agrego un elemento al inicio o en cualquier posicion por q se le pasa la posicion
numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

#se unio una lista con otra lista -> la de tareas con numbers, se guarda en una nueva lista
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

#actualizar un valor, saber en q posicion esta y actualizarlo
index = new_list.index('todo 2') #con el metodo index se la posicion en la q esta y lo guardo en index
new_list[index] = 'todo changed'
print(new_list)

#ELIMINAR
new_list.remove('todo 1')
print(new_list)

new_list.pop() #elimina el ultimo elemento de la lista, tambien tiene un parametro de entrada
print(new_list)

new_list.pop(0)
print(new_list)

#VOLTEAR LA LISTA
new_list.reverse()
print(new_list)

#ORDENAR sort ordena listas del mismo tipo 
numbers_a = [1, 4, 6, 3]
numbers_a.sort(reverse=True) 
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)
