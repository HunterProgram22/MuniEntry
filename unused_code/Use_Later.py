def get_dialog_fields(self):
    self.fields_dict = {
        'defendant_name' : self.defendant_name.text(),
        'case_no' : self.case_no.text(),
        'defendant_address' : defendant_address,
        'defendant_city' : defendant_city,
        'defendant_state' : defendant_state,
        'defendant_zipcode' : defendant_zipcode,
        }
    try:
        defendant_address = self.defendant_address.text()
        defendant_city = self.defendant_city.text()
        defendant_state = self.defendant_state.currentText()
        defendant_zipcode = self.defendant_zipcode.text()
    except AttributeError:
        """This may need to be modified to address if user leaves fields
        blank but the data is required."""
        defendant_address = None
        defendant_city = None
        defendant_state = None
        defendant_zipcode = None

    return self.fields_dict
