from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError


class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'College Student'
    _rec_name = 'student_identity'

    name = fields.Char(string="Student Name", required=True)
    email = fields.Char(string="Email Id", required=True)
    active = fields.Boolean('Active', default=True)
    student_identity = fields.Char(string="Student Id No.", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    department_id = fields.Many2one('college.curriculum')
    # user_id = fields.Many2one('res.users', string='Assigned to')
    sem_id = fields.Selection(
        [('sem-1', 'Sem - 1'), ('sem-2', 'Sem - 2'), ('sem-3', 'Sem - 3'), ('sem-4', 'Sem - 4'), ('sem-5', 'Sem - 5'),
         ('sem-6', 'Sem - 6'), ('sem-7', 'Sem - 7'), ('sem-8', 'Sem - 8')])
    # sem_id = fields.Many2one('college.sem1')
    # course_id = fields.Many2one('college.course')
    phone = fields.Char(string="Phone No.", size=10)
    address = fields.Text()
    signature = fields.Binary()
    # image_1920 = fields.Image(string='Student Image')
    # image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512)
    department_hod = fields.Char(related='department_id.hod')
    date_time_of_joining = fields.Datetime()
    birth_date = fields.Date()
    deposit = fields.Float(default=10000)
    fine = fields.Float(default=0.0)
    fine_paid = fields.Float(default=25)
    fine_pending = fields.Float()
    remarks = fields.Text()
    mark = fields.Integer(string='Marks')
    result = fields.Selection([('pass', 'Pass'), ('fail', 'Fail')], compute="_compute_result", store=True)
    # result = fields.Selection(selection_add=[('absent', 'Absent'),('no_fees', 'Fee payment pending')],compute="_compute_result", store=True)
    book_ids = fields.Many2many('library.book', 'library_book_student_rel', 'student_id', 'book_id', string="Books",
                                copy=False)

    @api.depends('mark')
    def _compute_result(self):
        for record in self:
            if record.mark >= 30:
                record.result = 'pass'
            else:
                record.result = 'fail'

    @api.model
    def create(self, values):
        print(values)
        print(values.get('phone'))
        values['student_identity'] = self.env['ir.sequence'].sudo().next_by_code('school.student') or ('New')
        res = super(CollegeStudent, self).create(values)
        print(res)
        print(res.phone)
        if res.phone and len(res.phone) != 10:
            raise ValidationError(('Contact number must have 10 digit! not %s digit and change this value %s' % (
            len(res.phone), res.phone)))
        return res
