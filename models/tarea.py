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
        string="Cliente"
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