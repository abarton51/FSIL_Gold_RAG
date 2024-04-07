from pypdf import PdfReader
from tqdm import tqdm
import os

## class to hold parsing sec complaint pdfs
class SECComplaintParser():

    def get_pdf_text(pdf_filepath: str) -> str:
        """
        Takes in filepath to pdf in as input, reads in and outputs document text

        args:
            pdf_filepath (str): filepath to pdf to read in

        returns:
            pdf_text (str): text of pdf at filepath location
        """

        reader = PdfReader(pdf_filepath)

        return " ".join([page.extract_text() for page in reader.pages])

    def check_faulty_pdf(pdf_text: str) -> bool:
        """
        Check if pdf text is faulty. For example, if very minimal text was extracted

        args:
            pdf_text: the text present in the pdf

        returns:
            bool: True if pdf is faulty, false otherwise
        """

        MIN_LENGTH_THRESHOLD = 300

        if len(pdf_text) < MIN_LENGTH_THRESHOLD:

            return True
        
        return False

    def get_all_pdf_texts(pdf_directory: str, save_text: bool = False, save_directory: str = None) -> dict[str: str]:
        """
        Takes in a directory name, reads in text of all pdfs in directory

        args:
            pdf_directory (str): path to directory to read in

        returns:
            dict(str: str): dict matching pdf name to pdf text
        """

        directory_texts = {}
        
        for filename in tqdm(os.listdir(pdf_directory)):

            pdf_text = get_pdf_text(os.path.join(pdf_directory, filename)).lower()

            #if there is something wrong with the pdf, do not include it in the dataset
            if check_faulty_pdf(pdf_text):

                continue

            directory_texts[filename.split(".")[0]] = pdf_text

            if save_text:

                if save_directory is None:

                    raise RuntimeError("Need to specify a save directory")

                with open(os.path.join(save_directory, filename.split(".")[0] + ".txt"), "w", encoding="utf-8") as save_file:

                    save_file.write(pdf_text)

        return directory_texts

    def load_pdf_texts(directory_path: str) -> dict[str: str]:
        """
        Takes in a directory name, reads in text of all txt files in directory

        args:
            directory_path (str): path to directory to read in

        returns:
            dict(str: str): dict matching pdf name to pdf text
        """

        directory_texts = {}

        for filename in tqdm(os.listdir(directory_path)):

            with open(os.path.join(directory_path, filename), encoding="utf-8") as txt_file:

                directory_texts[filename.split(".")[0]] = txt_file.read()

        return directory_texts

    def section_text(text: str) -> dict[str: str]:
        """
        Split block of text into sections based on identified section headers

        args:
            text (str): block of text to be sectioned

        returns:
            dict(str: str): dict matching section header to section
        """

    def extract_violated_regulations(filing_texts: dict[str: str]) -> list[str]:
        """
        Extract violated regulations given filing text

        args:
            filing_texts: dictionary of filings and texts

        returns:
            list[str]: list of violated regulations
        """

        cfr_headers = ["claims for relief", "claims for action", "claim for relief", "claim for action", "cause of action"]

        violation_lines = {}

        for filing_name in filing_texts:

            newline_sep_filing = filing_texts[filing_name].split("\n")

            for line in newline_sep_filing:

                if "section" in line:

                    if filing_name in violation_lines:

                        violation_lines[filing_name].append(line)

                    else:

                        violation_lines[filing_name] = [line]

        return violation_lines