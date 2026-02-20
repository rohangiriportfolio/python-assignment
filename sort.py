import logging

logging.basicConfig(
    filename="sort.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
) 

def sorting(l: list) -> None:
    """
    Find the second largest element.
    Parameters:
        l (list): Input list
    Returns:
        None: Only prints is sorted in ascending order or not.
    """
    l1=l
    l2=sorted(l1)
    if(l2==l):
        logging.info("Sorted in ascending order!")
    else:
        logging.info("Not sorted!")
l = eval(input())
logging.info(f"List inputted: {l}")
sorting(l)