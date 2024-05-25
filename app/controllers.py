import logging
from multiprocessing import Pool
from typing import List

logging.basicConfig(
    filename="logs/app.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)


def add_list_values(_list):
    try:
        return sum(_list)
    except Exception as e:
        logging.error(f"Error in summation of list values {_list}: {e}")
        raise


def process_payload(payload: List[List[int]]) -> List[int]:
    with Pool() as pool:
        result = pool.map(add_list_values, payload)
    return result
