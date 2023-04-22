import csv
from pathlib import Path

from progress.bar import Bar

from ..app.database import db
from ..constants import DATA_REGEX, UPLOAD_DIRECTORY
from ..models import Household, Product, Transaction


def normalize_dict(dict: dict[str, str]):
    return {
        key.strip(): value.strip() if value.strip() != "null" else None
        for key, value in dict.items()
    }


def parse_uploaded_files():
    success = True
    for file in UPLOAD_DIRECTORY.glob("*.csv"):
        categorySearch = DATA_REGEX.search(file.name)
        if category := categorySearch.group():
            print(f"Parsing {category}")
            match category.lower():
                case "households":
                    data_items = parse_households(file)
                case "transactions":
                    data_items = parse_transactions(file)
                case "products":
                    data_items = parse_products(file)
                case _:
                    data_items = None

            if data_items:
                try:
                    print(f"Uploading {category}")
                    db.session.add_all(data_items)
                except:
                    print(f"Uploading {category} failed!")
                    db.session.rollback()
                    success = False
                else:
                    try:
                        db.session.commit()
                        print(f"Uploaded {category} succesfully!")
                    except:
                        print(f"Uploading {category} failed!")
                        db.session.rollback()
    return success


def parse_households(csv_path: Path | str) -> list[Household]:
    households_list = []
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in Bar("Parsing").iter(reader):
            normDict = normalize_dict(row)
            if household_size := normDict["HH_SIZE"]:
                household_size = household_size.strip("+")
            if children := normDict["CHILDREN"]:
                children = children.strip("+")
            households_list.append(
                Household(
                    hshd_num=normDict["HSHD_NUM"],
                    loyalty_flag=normDict["L"] == "Y",
                    age_range=normDict["AGE_RANGE"],
                    marital_status=normDict["MARITAL"],
                    income_range=normDict["INCOME_RANGE"],
                    hshd_size=household_size,
                    homeowner_desc=normDict["HOMEOWNER"],
                    hshd_composition=normDict["HSHD_COMPOSITION"],
                    children=children,
                ),
            )
    return households_list


def parse_transactions(csv_path: Path | str) -> list[Transaction]:
    transactions_list = []
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in Bar("Parsing").iter(reader):
            normDict = normalize_dict(row)
            transactions_list.append(
                Transaction(
                    hshd_num=normDict["HSHD_NUM"],
                    basket_num=normDict["BASKET_NUM"],
                    date=normDict["PURCHASE_"],
                    product_num=normDict["PRODUCT_NUM"],
                    spend=normDict["SPEND"],
                    units=normDict["UNITS"],
                    store_region=normDict["STORE_R"],
                    week_num=normDict["WEEK_NUM"],
                    year=normDict["YEAR"],
                ),
            )
    return transactions_list


def parse_products(csv_path: Path | str) -> list[Product]:
    products_list = []
    with open(csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in Bar("Parsing").iter(reader):
            normDict = normalize_dict(row)
            products_list.append(
                Product(
                    product_num=normDict["PRODUCT_NUM"],
                    department=normDict["DEPARTMENT"],
                    commodity=normDict["COMMODITY"],
                    brand_type=normDict["BRAND_TY"],
                    natural_organic=normDict["NATURAL_ORGANIC_FLAG"] == "Y",
                ),
            )
    return products_list
