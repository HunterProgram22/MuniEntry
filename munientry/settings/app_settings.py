"""A module containing common variables used throughout the application."""
import socket
from types import MappingProxyType

from munientry.settings.config_settings import load_config

config = load_config()

# Version Information
version_dict: dict[str, str] = dict(config.items('version'))
VERSION_NUMBER: str = version_dict.get('version_number', '')


# Daily Case List Settings
DAILY_CASE_LIST_STORED_PROCS = MappingProxyType({
    'arraignments_cases_box': '[reports].[DMCMuniEntryArraignment]',
    'slated_cases_box': '[reports].[DMCMuniEntrySlated]',
    'pleas_cases_box': '[reports].[DMCMuniEntryPleas]',
    'pcvh_fcvh_cases_box': '[reports].[DMCMuniEntryPrelimCommContViolHearings]',
    'final_pretrial_cases_box': '[reports].[DMCMuniEntryFinalPreTrials]',
    'trials_to_court_cases_box': '[reports].[DMCMuniEntryBenchTrials]',
})


# Host (User) Information
def get_host() -> str:
    """Gets the host name of the PC that launches the application.

    If there is no key and value for the socket in the config file it sets the host to the
    socket name.
    """
    socket_dict = dict(config.items('sockets'))
    key = socket.gethostname()
    return socket_dict.get(key, key)


HOST_NAME: str = get_host()
