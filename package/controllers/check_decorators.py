from package.views.custom_widgets import RequiredBox


def check_judicial_officer(func):
    def wrapper(self):
        if self.judicial_officer is None:
            message = RequiredBox("You must select a judicial officer.")
            message.exec()
        else:
            func(self)
    return wrapper


def check_case_list_selected(func):
    def wrapper(self):
        if any(key.isChecked() for key in self.daily_case_list_buttons.keys()):
            func(self)
        else:
            message = RequiredBox("You must select a case list to load. If loading a "
                                  "blank template choose any case list and leave dropdown menu blank.")
            message.exec()
    return wrapper