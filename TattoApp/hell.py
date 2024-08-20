from lasagna import *

def bake_time_remaining(cooked_time):
    cooked_time = int(cooked_time)
    remaining_time = EXPECTED_BAKE_TIME - cooked_time

    return f"Tiempo restante: {remaining_time} minutos."


cooked_time = 30 
print(bake_time_remaining(cooked_time)) 

###############################################################

layers = 3

# Calcula el tiempo de preparación
time_needed = preparation_time_in_minutes(layers)



new_variable = elapsed_time_in_minutes(2, 20)
tiempo_trancurrido = time_needed + new_variable
print(tiempo_trancurrido) 





