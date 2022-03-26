from odoo import api, models, fields


class CollegeCurriculum(models.Model):
    _name = 'college.curriculum'
    _description = 'Manage Curriculum'

    name = fields.Char(string="Department", required=True)
    hod = fields.Char(string="HOD")
    description = fields.Text()
    # sid = fields.One2many('college.student', 'sem_id' )
    student_ids = fields.One2many('college.student', 'department_id')
    sem_id1 = fields.Many2many('college.sem1', 'college_curriculum_sem1_rel', 'dept_id', 'course_id', string='Sem - 1')
    sem_id2 = fields.Many2many('college.sem2', 'college_curriculum_sem2_rel', 'dept_id', 'course_id', string='Sem - 2')
    sem_id3 = fields.Many2many('college.sem3', 'college_curriculum_sem3_rel', 'dept_id', 'course_id', string='Sem - 3')
    sem_id4 = fields.Many2many('college.sem4', 'college_curriculum_sem4_rel', 'dept_id', 'course_id', string='Sem - 4')
    sem_id5 = fields.Many2many('college.sem5', 'college_curriculum_sem5_rel', 'dept_id', 'course_id', string='Sem - 5')
    sem_id6 = fields.Many2many('college.sem6', 'college_curriculum_sem6_rel', 'dept_id', 'course_id', string='Sem - 6')
    sem_id7 = fields.Many2many('college.sem7', 'college_curriculum_sem7_rel', 'dept_id', 'course_id', string='Sem - 7')
    sem_id8 = fields.Many2many('college.sem8', 'college_curriculum_sem8_rel', 'dept_id', 'course_id', string='Sem - 8')


class CollegeSem1(models.Model):
    _name = 'college.sem1'
    _description = 'Manage Curriculum of Sem-1'

    course_id = fields.Char(string="Course Id", required=True)
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text()


class CollegeSem2(models.Model):
    _name = 'college.sem2'
    _description = 'Manage Curriculum of Sem-2'

    course_id = fields.Char(string="Course Id", required=True)
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text()


class CollegeSem3(models.Model):
    _name = 'college.sem3'
    _description = 'Manage Curriculum of Sem-3'

    course_id = fields.Char(string="Course Id", required=True)
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text()


class CollegeSem4(models.Model):
    _name = 'college.sem4'
    _description = 'Manage Curriculum of Sem-4'

    course_id = fields.Char(string="Course Id", required=True)
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text()


class CollegeSem5(models.Model):
    _name = 'college.sem5'
    _description = 'Manage Curriculum of Sem-5'

    course_id = fields.Char(string="Course Id", required=True)
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text()


class CollegeSem6(models.Model):
    _name = 'college.sem6'
    _description = 'Manage Curriculum of Sem-6'

    course_id = fields.Char(string="Course Id", required=True)
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text()


class CollegeSem7(models.Model):
    _name = 'college.sem7'
    _description = 'Manage Curriculum of Sem-7'

    course_id = fields.Char(string="Course Id", required=True)
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text()


class CollegeSem8(models.Model):
    _name = 'college.sem8'
    _description = 'Manage Curriculum of Sem-8'

    course_id = fields.Char(string="Course Id", required=True)
    course_name = fields.Char(string="Course Name", required=True)
    course_description = fields.Text()
