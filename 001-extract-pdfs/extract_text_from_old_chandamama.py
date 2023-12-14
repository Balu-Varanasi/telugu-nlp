import concurrent
import io
import glob
import os
import pathlib
import pprint

import numpy as np
import layoutparser as lp
import pypdfium2 as pdfium
import warnings

from PIL import Image


warnings.filterwarnings("ignore")


HOME_DIR = pathlib.Path.home()
CURRENT_DIR = pathlib.Path(__file__).parent
DATA_DIR = os.path.join(CURRENT_DIR, "data")
BOOKS_DIR = os.path.join(DATA_DIR, "books")
EXTRACTED_TEXTS_DIR = os.path.join(DATA_DIR, "extracted-texts")

print("\n")
print(f"HOME_DIR > ", HOME_DIR)
print(f"CURRENT_DIR > ", CURRENT_DIR)
print(f"DATA_DIR > ", DATA_DIR)
print(f"BOOKS_DIR > ", BOOKS_DIR)
print(f"EXTRACTED_TEXTS_DIR > ", EXTRACTED_TEXTS_DIR)
print("\n\n")

PDF_FILES = glob.glob(os.path.join(BOOKS_DIR, "chandamama-*.pdf"))
TESSERACT_AGENT_LANGUAGE = "tel"

print(f"Found {len(PDF_FILES)} PDF files in {BOOKS_DIR}.")


def convert_pdf_to_images(pdf_file_path: str):
    pdf_file = pdfium.PdfDocument(pdf_file_path)

    page_indices = [i for i in range(len(pdf_file))]

    renderer = pdf_file.render(
        pdfium.PdfBitmap.to_pil,
        page_indices=page_indices,
    )

    final_images = []

    for i, image in zip(page_indices, renderer):
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format='jpeg', optimize=False)

        image_byte_array = image_byte_array.getvalue()
        final_images.append(dict({i: image_byte_array}))

    image_list = [list(data.values())[0] for data in final_images]

    return image_list


layout_detection_model = lp.models.Detectron2LayoutModel(
    config_path='lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config',
    model_path=f"{HOME_DIR}/.torch/iopath_cache/s/dgy9c10wykk4lq4/model_final.pth",
    label_map={
        0: "Text",
        1: "Title",
        2: "List",
        3: "Table",
        4: "Figure",
    },
    extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
)


def extract_text_from_image(image_byte_array):
    image = Image.open(io.BytesIO(image_byte_array))
    image = np.array(image)
    layout = layout_detection_model.detect(image)

    ocr_agent = lp.TesseractAgent(languages=[TESSERACT_AGENT_LANGUAGE])

    text_items = []

    for block_idx, block in enumerate(layout):
        segment_image = block.pad(
            left=5,
            right=5,
            top=5,
            bottom=5
        ).crop_image(image)

        response = ocr_agent.detect(segment_image, return_response=True)

        text = response['text']

        text_items.append(text)

        block.set(text=text, inplace=True)

    return "".join(text_items)


def process_pdf_pages_concurrently(pdf_file_path):
    """
    Process a list of images concurrently and return the combined text.
    """
    combined_text = ""

    images = convert_pdf_to_images(pdf_file_path)

    total_number_of_images = len(images)
    print(f"Processing {len(images)} images out of {total_number_of_images} in {pdf_file_path}.")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(extract_text_from_image, images)

        for result in results:
            combined_text += result + "\n\n"

    return combined_text


if __name__ == '__main__':
    file_path = PDF_FILES[0]
    output_file_path = os.path.join(EXTRACTED_TEXTS_DIR, os.path.basename(file_path).split('.')[0] + '.txt')

    print(f"Processing {file_path}...")

    book_pages = process_pdf_pages_concurrently(file_path)
    book_text = ''.join(book_pages)

    print(f"Writing {len(book_pages)} pages to {output_file_path}...")

    with open(output_file_path, 'wb') as f:
        f.write(book_text.encode('utf-8'))
