"""Builder module for the Competency Dialog."""
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.crim_checks import DefenseCounselChecks
from munientry.loaders.cms_case_loaders import CrimCmsNoChargeLoader
from munientry.models.case_information.criminal_case_information import CriminalCompetencyModel
from munientry.updaters.no_grid_case_updaters import CompetencyDialogUpdater
from munientry.views.competency_dialog_ui import Ui_CompetencyDialog


class CompetencyDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Competency Entry Dialog."""


class CompetencyDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Competency Entry Dialog."""

    def show_hide_condition_boxes(self):
        if self.dialog.competency_determination_box.currentText() in [
            'Found Competent', 'Found Competent - Not Insane',
        ]:
            self.dialog.final_pretrial_date.show()
            self.dialog.final_pretrial_date_label.show()
            self.dialog.final_pretrial_time_box.show()
            self.dialog.final_pretrial_time_label.show()
            self.dialog.trial_date.show()
            self.dialog.trial_date_label.show()
            self.dialog.hearing_location_box.show()
            self.dialog.hearing_location_label.show()
            self.dialog.treatment_type_box.hide()
            self.dialog.treatment_type_label.hide()
            self.dialog.in_jail_box.hide()
            self.dialog.in_jail_label.hide()
        elif self.dialog.competency_determination_box.currentText() in [
           'Not Competent - Not Restorable', 'Not Restored to Competency - Dismiss',
        ]:
            self.dialog.final_pretrial_date.hide()
            self.dialog.final_pretrial_date_label.hide()
            self.dialog.final_pretrial_time_box.hide()
            self.dialog.final_pretrial_time_label.hide()
            self.dialog.trial_date.hide()
            self.dialog.trial_date_label.hide()
            self.dialog.hearing_location_box.hide()
            self.dialog.hearing_location_label.hide()
            self.dialog.treatment_type_box.hide()
            self.dialog.treatment_type_label.hide()
            self.dialog.in_jail_box.show()
            self.dialog.in_jail_label.show()
        else:
            self.dialog.final_pretrial_date.hide()
            self.dialog.final_pretrial_date_label.hide()
            self.dialog.final_pretrial_time_box.hide()
            self.dialog.final_pretrial_time_label.hide()
            self.dialog.trial_date.hide()
            self.dialog.trial_date_label.hide()
            self.dialog.hearing_location_box.hide()
            self.dialog.hearing_location_label.hide()
            self.dialog.treatment_type_box.show()
            self.dialog.treatment_type_label.show()
            self.dialog.in_jail_box.hide()
            self.dialog.in_jail_label.hide()


class CompetencyDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Competency Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_dialog_specific_signals()

    def connect_dialog_specific_signals(self):
        self.dialog.competency_determination_box.currentTextChanged.connect(
            self.dialog.functions.show_hide_condition_boxes,
        )


class CompetencyCheckList(DefenseCounselChecks):
    """Check list for Competency Entry Dialog."""

    check_list = [
        # 'check_defense_counsel',
    ]


class CompetencyDialog(crim.CrimTrafficDialogBuilder, Ui_CompetencyDialog):
    """Dialog builder class for Competency Entry."""
    _case_information_model = CriminalCompetencyModel
    _case_loader = CrimCmsNoChargeLoader
    _info_checker = CompetencyCheckList
    _model_updater = CompetencyDialogUpdater
    _signal_connector = CompetencyDialogSignalConnector
    _slots = CompetencyDialogSlotFunctions
    _view_modifier = CompetencyDialogViewModifier
    dialog_name = 'Competency Evaluation Entry'

    def additional_setup(self):
        self.functions.show_hide_condition_boxes()
