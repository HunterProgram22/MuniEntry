"""Module for PDF Viewers and tools used by Viewers."""
import fitz

from munientry.settings import DW_APPROVED_DIR, ICON_PATH, TIMENOW


def add_approved_stamp(file):
    """Move this to a TextWriter box for centering."""
    img_rect = fitz.Rect(475, 50, 555, 130)
    img_filename = fr'{ICON_PATH}\approved_stamp.png'
    text_start_point = fitz.Point(465, 65)
    file_time = TIMENOW.toString('MMM dd, yyyy hh:mm')
    filestamp_text = \
        f'FILED\nDELAWARE\nMUNICIPAL COURT\n'\
        + f'{file_time}\nCindy Dinovo\nClerk of Court'
    document = fitz.open(file)
    page = document[0]
    page.insert_image(img_rect, filename=img_filename)
    page.insert_text(text_start_point, filestamp_text, color=(0.7, 0.0, 0.1))
    document.save(f'{DW_APPROVED_DIR}/Test.pdf')
    document.close()
