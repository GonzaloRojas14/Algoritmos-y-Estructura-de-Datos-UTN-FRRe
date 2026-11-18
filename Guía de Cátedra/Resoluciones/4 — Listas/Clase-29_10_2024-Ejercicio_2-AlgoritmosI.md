

**Fecha de inicio:** 30-10-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea

Una oficina postal quiere mejorar la organización de los pedidos y envíos diarios. Cada día, recibe una lista, doblemente enlazada, de pedidos desde el sistema central de la empresa, que contiene información sobre todos los envíos pendientes, con el siguiente formato de nodo

| prim1                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ID_Pedido`<br><br>`Estado: “pendiente”, “entregado”, “devuelto” ` <br><br>`Intentos de entrega: 0..5`<br><br>`fecha_retiro: fecha //dia a entregar el pedido`<br><br>`modalidad_envio: “domicilio”, “sucursal”`<br><br>`prioridad: 1..5`<br><br>`direccion envio`<br><br>`dni_destinatario`<br><br>`apellidoynombre_destinatario`<br> |


La oficina necesita procesar estos pedidos para optimizar las entregas diarias.

Se le solicita:

1. Generar una lista con los pedidos a enviar en el día de hoy
    

1. incluye aquellos pedidos en estado “pendiente” y con modalidad de envio “domicilio”
    
2. Ordenar la lista según el campo prioridad
    
3. El formato del nodo debe incluir:
    

1.  `ID_Pedido`
    
2. `Estado: “pendiente”, “entregado”, "devuelto"`
    
3. `Intentos de entrega: 0..5`
    
4. `fecha_retiro: fecha //dia a entregar el pedido`
    
5. `modalidad_envio: “domicilio”, “sucursal”`
    
6. `direccion_envio`
    
7. `dni_destinatario`
    
8. `prioridad: 1..5`
    
9. `apellidoynombre_destinatario`
    
10. `id_empleado_asignado`
    
11. `nombre_empleado_asignado`
    

3. Generar una lista con los pedidos en estado “pendiente” y que se deben retirar hoy de la sucursal, ordenada por apellido del destinatario.
    
4. Eliminar de la lista los pedidos en estado “entregado”
    
5. Desarrollar un procedimiento que elimine de la lista de pedidos aquellos pedidos que ya fueron regresados al remitente (estado “devuelto”) o que llevan más de 2 intentos sin poder entregarse.
    

## Resolución

## Relaciones
- [[Listas-AlgoritmosI]]

