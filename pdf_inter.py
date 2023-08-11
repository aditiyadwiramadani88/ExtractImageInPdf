import os
import fitz
import io
from PIL import Image
import  time
import  shutil

class GetPdf:
    image = list
    filename: str
    zipfile: str
    def __init__(self, filename):
        self.filename = filename
    def save(self):
        otput_format = 'png'
        data = self._save_image(otput_format)
        self.image = data[0]
        self.zipfile = data[1]
        return  self
    def _save_image(self, otput_format):
        image_folder =  str(time.time())
        os.mkdir("upload/images/" + image_folder)
        data_file = []
        pdf_file = fitz.open("upload/"+self.filename)
        for page_index in range(len(pdf_file)):
            # get page
            page = pdf_file[page_index]
            # get list image
            image_list = page.get_images(full=True)
            for image_index, img in enumerate(image_list, start=1):
                    # Get the XREF of the image
                    xref = img[0]
                    # Extract the image bytes
                    base_image = pdf_file.extract_image(xref)
                    image_bytes = base_image["image"]
                    # Get the image extension
                    image_ext = base_image["ext"]
                    # Load it to PIL
                    image = Image.open(io.BytesIO(image_bytes))
                    data_file.append(f"{page_index + 1}_{image_index}.{otput_format}")
                    image.save(
                open(os.path.join(f"upload/images/{image_folder}", f"{page_index + 1}_{image_index}.{otput_format}"), "wb"),
                format=otput_format.upper())
        # remove pdf
        os.remove("upload/" + self.filename)
        shutil.make_archive(f"upload/{image_folder}", "zip", "upload/images/"+ image_folder)
        self._delete_image(image_folder)
        return  [data_file, image_folder + ".zip"]
    def get_image(self):
        return  [self.image, self.zipfile]
    def _delete_image(self, folder_name):
        os.system("rm -rf upload/images/" + folder_name)
        return  True



