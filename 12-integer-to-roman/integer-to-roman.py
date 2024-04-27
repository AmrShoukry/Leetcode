class Solution:
    def intToRoman(self, num: int) -> str:
        final_string = ""
        chars = [
            {
                "value": 1000,
                "letter": 'M'
            },
            {
                "value": 900,
                "letter": 'CM'
            },
            {
                "value": 500,
                "letter": 'D'
            },
            {
                "value": 400,
                "letter": 'CD'
            },
            {
                "value": 100,
                "letter": 'C'
            },
            {
                "value": 90,
                "letter": 'XC'
            },
            {
                "value": 50,
                "letter": 'L'
            },
            {
                "value": 40,
                "letter": 'XL'
            },
            {
                "value": 10,
                "letter": 'X'
            },
            {
                "value": 9,
                "letter": 'IX'
            },
            {
                "value": 5,
                "letter": 'V'
            },
            {
                "value": 4,
                "letter": 'IV'
            },
            {
                "value": 1,
                "letter": 'I'
            }
        ]

        while num > 0:
            for item in chars:
                while num >= item["value"]:
                    num -= item["value"]
                    final_string += item["letter"]
        return final_string