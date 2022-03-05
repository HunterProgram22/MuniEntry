class DiversionDialogViewModifier(object):
    def __init__(self):
        super().modify_view()
        diversion_pay_days_to_add = set_future_date(97, None, 1)
        self.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        jail_report_days_to_add = set_future_date(97, None, 4)
        self.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        self.show_jail_report_date_box()
        self.show_other_conditions_box()