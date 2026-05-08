# Consultas ORM realizadas

## 1. Tareas por clientes

```python
    cliente_id = 7

    tareas = env["gestion.tarea"].search([
        ("cliente_id","=",cliente_id)
    ])

    for tarea in tareas:
        print(tarea.nombre, tarea.cliente_id.name, tarea.estado)
```
### Explicación

Esta consulta obtiene todas las tareas asociadas

---
## 2. Consultas de tareas pendientes

```python
tareas_pendientes = env["gestion.tarea"].search([
    ("estado", "=", "pendiente")
])

for tarea in tareas_pendientes:
    print(tarea.nombre, tarea.estado)
```
### Explicación

Esta consulta obtiene las tareas pendientes
---
## 3. Optimización básica aplicada

Se utilizan dominios ORM específicos

```
("cliente_id", "=", cliente_id)
```
y
```python
("estado", "=", "pendiente")
```

Esto evita cargar todos los registros de la base de datos