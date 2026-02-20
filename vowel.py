import logging

logging.basicConfig(
    filename="vowel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def countVow(s: str) -> int:
    """
    Count the number of vowels in a given string.
    Parameters:
        s (str): Input string
    Returns:
        c (int): Total number of vowels in the string.
    """
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    c = 0
    for i in s:
        if i in v:
            c+=1
    return c
    
s = input()
logging.info(f"String inputted: {s}")
c=countVow(s)
logging.info(f'No of vowels: {c}')
