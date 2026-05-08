from odoo import models, fields, api

class Tarea(models.Model):
    _name = "gestion.tarea"
    _description = "Tarea"
    _order = "fecha desc, id desc"

    name = fields.Char(
        string="Nombre de la tarea", 
        required=True
    )

    cliente_id = fields.Many2one(
        cmodel_name="res.partner",
        string="Cliente",
        required=True
    )

    fecha = fields.Date(
        string="Fecha de la tarea",
        required=True
    )

    estado = fields.Selection(
        selection=[
            ("pendiente", "Pendiente"),
            ("finalizada", "Finalizada"),
            ],
        string="Estado",
        default="pendiente",
        required=True
    )

    def action_marcar_como_finalizada(self):
        for tarea in self:
            tarea.estado = "finalizada"
    
    def obtener_tareas_por_clientes(self, cliente_id):
        return self.search([
            ("cliente_id", "=", cliente_id)
        ])

    def obtener_tareas_pendientes(self):    
        return self.search([
            ("estado", "=", "pendiente")
        ])