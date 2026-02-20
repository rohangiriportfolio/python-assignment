import logging

logging.basicConfig(
    filename="freq.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
) 

def freq(s: str) -> dict:
    """
    Count the frequency of each letter.
    Parameters:
        s (str): Input string
    Returns:
        dict: Frequency of each letter.
    """
    d={}
    for i in s:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d
s = input()
logging.info(f"String inputted: {s}")
logging.info(f"Frequency of letters: {freq(s)}")