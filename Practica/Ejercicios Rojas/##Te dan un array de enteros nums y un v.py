##Te dan un array de enteros nums y un valor val. Tenés que remover in-place todas las apariciones de val, manteniendo el orden r
#elativo de los demás elementos. No importa qué quede después de la posición final — igual que en los ejercicios anteriores, devolvés k 
# (la cantidad de elementos que no son val), y solo las primeras k posiciones del array tienen que ser correctas.
##Ejemplo 1:
##Input: nums = [3,2,2,3], val = 3
##Output: k = 2, nums = [2,2,_,_]
##Ejemplo 2:
##Input: nums = [0,1,2,2,3,0,4,2], val = 2
##Output: k = 5, nums = [0,1,4,0,3,_,_,_]
##(el orden de los elementos que quedan puede variar, mientras sean los correctos)


nums = [3,2,2,3]
val = 3

def remove_val(nums):
    k=0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

print(remove_val(nums))



# Maximum Sum Subarray of Size K
# Dado un array de enteros nums y un entero k, encontrá la suma máxima de cualquier subarray contiguo de tamaño exactamente k.
# Ejemplo:
# nums = [2, 1, 5, 1, 3, 2], k = 3
# Los subarrays de tamaño 3 son: [2,1,5]→8, [1,5,1]→7, [5,1,3]→9, [1,3,2]→6
# Output: 9 (el de [5,1,3])


nums = [2, 1, 5, 1, 3, 2]
k = 3

def sum_subarray(nums, k):
    # Paso 1: suma de la primera ventana (índices 0 a k-1)
    window_sum = sum(nums[0:k])
    mejor = window_sum

    # Paso 2 y 3: deslizar la ventana de a uno
    for i in range(k, len(nums)):
        # i = índice que entra (extremo derecho nuevo)
        # i - k = índice que sale (quedó k lugares atrás de i)
        window_sum = window_sum - nums[i - k] + nums[i]
        mejor = max(mejor, window_sum)

    return mejor


print(sum_subarray(nums, k))




def reverse_array(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums