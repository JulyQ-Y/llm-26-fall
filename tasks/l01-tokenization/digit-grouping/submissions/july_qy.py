PREDICTIONS = {
    "3.14159": ["3",".","141","59"],
    "Room 101": ["Room ","101"],
    "2024-09-16": ["202","4","-","09","-","16"],
}
MY_CASES = [
    ("000012345", ["000","012","345"]),
    ("A1234567B", ["A", "123", "456", "7", "B"])
]
NOTES = """If every ASCII digit string from length 1 through k 
including leading zeros, has its own token,the required numeric 
vocabulary is 10 entries for k = 1,1110 entries for k = 3,and 
11110 entries for k = 4.The number 123456789012 needs 12 tokens 
whenk=1, 4 tokens when k=3, and 3 tokens when k=4.Tradeoff means 
allowing longer numeric groups can shorten sequences but requires 
a much larger vocabulary. A pre-tokenization chunk is not guaranteed 
to become one BPE token, because BPE can still split that chunk 
into smaller tokens if the whole chunk is notin its vocabulary."""

def solve(text: str) -> list[str]:
    chunks = []
    i = 0

    while i < len(text):
        start = i

        if text[i].isdecimal():
            while i < len(text) and text[i].isdecimal():
                i += 1

            digits = text[start:i]

            for j in range(0, len(digits), 3):
                chunks.append(digits[j:j + 3])

        else:
            while i < len(text) and not text[i].isdecimal():
                i += 1

            chunks.append(text[start:i])

    return chunks