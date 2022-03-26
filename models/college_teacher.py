from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class CollegeTeacher(models.Model):
    _name = 'college.teacher'
    _description = 'College Teacher'
    _rec_name = 'teacher_identity'

    name = fields.Char("Teacher Name", required=True)
    email = fields.Char(string="Email Id",required=True)
    active = fields.Boolean('Active', default=True)
    teacher_identity = fields.Char(string="Teacher Id No.",required=True)
    birth_date = fields.Date()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    # user_id = fields.Many2one('res.users', string='Login id')
    department_id = fields.Many2one('college.curriculum')
    phone = fields.Char(string="Phone No.",size=10)
    address = fields.Text()
    signature = fields.Binary()
    # image_1920 = fields.Image(string='Teacher Image')
    # image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512)
    department_hod = fields.Char(related='department_id.hod')
    date_time_of_joining = fields.Datetime()
    book_ids = fields.Many2many('library.book', 'library_book_teacher_rel', 'teacher_id', 'book_id', string="Books",copy=False)
    remarks = fields.Text()