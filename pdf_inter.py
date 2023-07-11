import os
import fitz  # PyMuPDF
import io
from PIL import Image

class generetPdf:
    filename: str
    def __int__(self, filename):
        self.filename = filename
    def save(self):
        otput_format = 'png'
        min_with = 100
        min_height = 100
        if not os.path.exists('pdf'):
            os.makedirs('pdf')




