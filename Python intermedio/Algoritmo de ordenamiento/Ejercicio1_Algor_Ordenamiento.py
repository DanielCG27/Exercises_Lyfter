def bubble_sort(list_to_sort):

    for outer_index in range(0, len(list_to_sort) -1):

        # Usamos esta variable para revisar si hemos movido elementos
        has_made_changes = False

    # iteramos la lista con el for, desde el índice/rango 0 a todo el tamaño de la lista que se hace con len, al len debo restarle 1 para que llegue hasta el penúltimo
    #para que no se repitan ciclos que ya se ejecutaron, le resto al for el outer_index
        for index in range(0, len(list_to_sort) -1 - outer_index):
        # Guardamos los valores del elemento actual y el siguiente, al siguiente se le suma 1 y los 2 se guardan en el índice
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]
        # Luego se imprime el índice, el elemento actual y el siguiente elemento
            print(f'-- Iteration {index}. Current element: {current_element}. Next element {next_element}')

        # Luego pongo si el actual > al siguiente, intercambiemos sus posiciones
            if current_element > next_element:
                print('The current element is bigger than the next element. Change them')

                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                has_made_changes = True

        if not has_made_changes:
            return

# Luego hago el test de prueba
my_test_list = [100, 2, 7, 9, 1, 3]
bubble_sort(my_test_list)

print(my_test_list)