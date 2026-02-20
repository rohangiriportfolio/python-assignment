import logging

logging.basicConfig(
    filename="secondLarge.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
) 

def secondLarge(l: list) -> int:
    """
    Find the second largest element.
    Parameters:
        l (list): Input list
    Returns:
        b (int): Second largest element.
    """
    a = float('-inf')
    b = float('-inf')
    for i in l:
        if i>a:
            b=a
            a=i
        if i>b and i!=a:
            b=i
    return b

# l = [1,2,3,4,5,6]
l = eval(input())
logging.info(f"List inputted: {l}")
logging.info(f"Second largest element: {secondLarge(l)}")
