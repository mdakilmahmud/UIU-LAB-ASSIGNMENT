# a
f1 = open("book_info.txt", "r")
f2 = open("Authorwise Book.txt", "w")
lines = f1.readlines()
author_name = input("Enter an author’s name: ")
f1.close()
found_books = []
for line in lines:
    parts = line.strip().split(', ')
    if len(parts) == 4:  
        book_name = parts[0]
        price = float(parts[1])
        author = parts[2]
        genre = parts[3]
        if author.lower() == author_name.lower():
            found_books.append(line.strip())
            f2.write(line)
if found_books:
    print(f"Books by {author_name} have been written to Authorwise Book.txt.")
    print()
else:
    print(f"No books found by {author_name}.")
f2.close()
# b
highest_priced_book=" "
highest_price = 0
for line in lines:
    parts = line.strip().split(', ')
    if len(parts) == 4:
        book_name = parts[0]
        price = float(parts[1])
        author = parts[2]
        genre = parts[3]
        if price > highest_price:
            highest_price = price
            highest_priced_book = line.strip()
if highest_priced_book:
    print("Book with the highest price:")
    print(highest_priced_book)