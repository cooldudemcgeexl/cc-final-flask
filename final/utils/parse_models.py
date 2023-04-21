import csv
from pathlib import Path

from ..constants import DATA_REGEX, UPLOAD_DIRECTORY
from ..models import Household


def parse_uploaded_files():
    for file in UPLOAD_DIRECTORY.glob("*.csv"):
        categorySearch = DATA_REGEX.search(file.name)
        if category := categorySearch.group():
            match category.lower():
                case "households":
                    parse_households(file)
                case "transactions":
                    pass
                case "products":
                    pass
                case _:
                    pass


def parse_households(csv_path: Path | str):
    households_list = []
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            normDict = {
                key.strip(): value.strip() if value.strip() != "null" else None
                for key, value in row.items()
            }
            households_list.append(
                Household(
                    hshd_num=normDict["HSHD_NUM"],
                    loyalty_flag=normDict["L"] == "Y",
                    age_range=normDict["AGE_RANGE"],
                    marital_status=normDict["MARITAL"],
                    income_range=normDict["INCOME_RANGE"],
                    hshd_size=normDict["HH_SIZE"],
                    homeowner_desc=normDict["HOMEOWNER"],
                    hshd_composition=normDict["HSHD_COMPOSITION"].strip("+"),
                    children=normDict["CHILDREN"].strip("+"),
                ),
            )
    return households_list
