# import pytest
#
# from munientry.appsettings.paths import CASE_LISTS_PATH
# from munientry.data.excel_getters import return_cases_data_from_excel
# from munientry.data.excel_functions import load_active_worksheet, get_excel_file_headers, \
#     create_headers_dict
#
#
# all_daily_case_list_excel_files = [
#     (f'{CASE_LISTS_PATH}Arraignments.xlsx', 21),
#     (f'{CASE_LISTS_PATH}Final_Pretrials.xlsx', 28),
#     (f'{CASE_LISTS_PATH}PCVH_FCVH.xlsx', 30),
#     (f'{CASE_LISTS_PATH}Pleas.xlsx', 28),
#     (f'{CASE_LISTS_PATH}Slated.xlsx', 28),
#     (f'{CASE_LISTS_PATH}Trials_to_Court.xlsx', 28),
# ]
#
#
# @pytest.mark.parametrize("db_file, sub_case_count", all_daily_case_list_excel_files)
# def test_return_cases_data_from_excel(db_file, sub_case_count):
#     """Should return the total number of sub cases in a case SSRS Excel file."""
#     case_count = len(return_cases_data_from_excel(db_file))
#     assert case_count == sub_case_count
#
#
# all_daily_case_list_excel_columns = [
#     (f'{CASE_LISTS_PATH}Arraignments.xlsx', 12),
#     (f'{CASE_LISTS_PATH}Final_Pretrials.xlsx', 12),
#     (f'{CASE_LISTS_PATH}PCVH_FCVH.xlsx', 12),
#     (f'{CASE_LISTS_PATH}Pleas.xlsx', 12),
#     (f'{CASE_LISTS_PATH}Slated.xlsx', 12),
#     (f'{CASE_LISTS_PATH}Trials_to_Court.xlsx', 12),
# ]
#
#
# @pytest.mark.parametrize("db_file, total_col", all_daily_case_list_excel_columns)
# def test_get_excel_file_headers(db_file, total_col):
#     worksheet = load_active_worksheet(db_file)
#     total_columns = len(get_excel_file_headers(worksheet))
#     assert total_columns == total_col
#
#
# all_daily_case_list_header_check = [
#     (f'{CASE_LISTS_PATH}Arraignments.xlsx', 1),
#     (f'{CASE_LISTS_PATH}Final_Pretrials.xlsx', 4),
#     (f'{CASE_LISTS_PATH}PCVH_FCVH.xlsx', 4),
#     (f'{CASE_LISTS_PATH}Pleas.xlsx', 4),
#     (f'{CASE_LISTS_PATH}Slated.xlsx', 4),
#     (f'{CASE_LISTS_PATH}Trials_to_Court.xlsx', 4),
# ]
#
#
# @pytest.mark.parametrize("db_file, first_name_col", all_daily_case_list_header_check)
# def test_create_headers_dict(db_file, first_name_col):
#     worksheet = load_active_worksheet(db_file)
#     header_list = get_excel_file_headers(worksheet)
#     header_dict = create_headers_dict(header_list)
#     assert header_dict['DefFirstName'] == first_name_col
#