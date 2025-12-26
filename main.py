import sys
from stats import count_words, count_characters,sort_characters

def get_book_text(filepath):
	with open(filepath,"r") as f:
		booktext = f.read()
	return booktext

def main():
	
	print(f"{sys.argv}")
	print(f"{len(sys.argv)}")


	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	

	book_filepath = sys.argv[1]
	frankenstein_text = get_book_text(book_filepath)
	frankenstein_words = count_words(frankenstein_text)

	frankenstein_char_counts = count_characters(frankenstein_text)
	# print(f"Character counts: {frankenstein_char_counts}")

	frankenstein_char_sort_counts = sort_characters(frankenstein_char_counts)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {frankenstein_words} total words")
	print("--------- Character Count -------")
	for entry in frankenstein_char_sort_counts:
		if entry['char'].isalpha():
			print(f"{entry['char']}: {entry['num']}")
	print("============= END ===============")

	

main()
