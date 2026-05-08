# Simulación API - Gestión de Tareas

## Datos que se enviarían

- nombre
- cliente_id
- fecha
- estado

## Ejemplo JSON

POST /api/tareas

```json
{
  "nombre": "Revisión contrato",
  "cliente_id": 5,
  "fecha": "2026-05-08",
  "estado": "pendiente"
}
```
# Respuesta simulada

```json
{
  "status": "ok",
  "message": "Tarea creada correctamente",
  "id": 12
}
```