from trytond.model import ModelView, ModelSQL, fields

__all__ = ['Continent']


class Continent(ModelSQL, ModelView):
    "Continent"
    __name__ = 'continent.continent'
    name = fields.Char('Name',required=True,
           help='The full name of the continent.', select=True)
    code = fields.Char('Code', size=3, select=True,
           help='The continent code in three chars.\n'
           'You can use this field for quick search.', required=True)

    @classmethod
    def __setup__(cls):
        super(Continent, cls).__setup__()
        cls._sql_constraints += [
            ('name_uniq', 'UNIQUE(name)',
                'The name of the continent must be unique!'),
            ('code_uniq', 'UNIQUE(code)',
                'The code of the continent must be unique!'),
            ]
        cls._order.insert(0, ('name', 'ASC'))

    @classmethod
    def search_rec_name(cls, name, clause):
        if cls.search([('code',) + clause[1:]], limit=1):
            return [('code',) + clause[1:]]
        return [(cls._rec_name,) + clause[1:]]

    @classmethod
    def create(cls, vals):
        if 'code' in vals and vals['code']:
            vals = vals.copy()
            vals['code'] = vals['code'].upper()
        return super(Continent, cls).create(vals)

    @classmethod
    def write(cls, continent, vals):
        if 'code' in vals and vals['code']:
            vals = vals.copy()
            vals['code'] = vals['code'].upper()
        super(Continent, cls).write(continent, vals)

