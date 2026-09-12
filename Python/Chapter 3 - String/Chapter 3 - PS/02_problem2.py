from datetime import date

current_date = date.today()
name = input("Enter your name: ")

letter = f'''  
Dear {name},  
You are selected!  
Date: {current_date}  
'''

print(letter)


# letter = '''Dear <|Name|>, 
# You are selected! 
# <|Date|> '''

# print(letter.replace("<|Name|>", "Harry").replace("<|Date|", "24 September 2050"))