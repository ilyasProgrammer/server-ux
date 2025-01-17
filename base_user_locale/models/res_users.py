# Copyright 2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    date_format = fields.Char(
        string="Date Format",
        help="See Settings > Translations > Languages and then "
        "click on any language to see the Legends for "
        "supported Date and Time Formats and some examples",
    )
    time_format = fields.Char(
        string="Time Format",
        help="See Settings > Translations > Languages and then "
        "click on any language to see the Legends for "
        "supported Date and Time Formats and some examples",
    )
    week_start = fields.Selection(
        string="Week Start",
        selection=[
            ("1", "Monday"),
            ("2", "Tuesday"),
            ("3", "Wednesday"),
            ("4", "Thursday"),
            ("5", "Friday"),
            ("6", "Saturday"),
            ("7", "Sunday"),
        ],
    )
    decimal_point = fields.Char(
        string="Decimal Separator",
        trim=False,
        help="See Settings > Translations > Languages and then "
        "click on any language to see the Legends for "
        "supported Date and Time Formats and some examples",
    )
    thousands_sep = fields.Char(
        string="Thousands Separator",
        trim=False,
        help="See Settings > Translations > Languages and then "
        "click on any language to see the Legends for "
        "supported Date and Time Formats and some examples",
    )

    def __init__(self, pool, cr):
        """Override of __init__ to add access rights.
        Access rights are disabled by default, but allowed
        on some specific fields defined in self.SELF_{READ/WRITE}ABLE_FIELDS.
        """
        base_user_locale_fields = [
            "date_format",
            "time_format",
            "week_start",
            "decimal_point",
            "thousands_sep",
        ]
        super(ResUsers, self).__init__(pool, cr)
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(base_user_locale_fields)
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(base_user_locale_fields)

    def preference_save(self):
        super().preference_save()
        # Do a "full" reload instead of just a context_reload to apply locale
        # user specific settings.
        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }
