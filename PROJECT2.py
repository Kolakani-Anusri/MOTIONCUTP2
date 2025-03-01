def count_words(text):
    """Function to count the number of words in a given text."""
    words = text.split()
    return len(words)


def main():
    """Main function to handle user input and display word count."""
    while True:
        text = input("Enter a sentence or paragraph (or type 'exit' to quit): ").strip()
        
        if text.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        if not text:
            print("Error: Input cannot be empty. Please enter some text.")
            continue
        
        word_count = count_words(text)
        print(f"Word Count: {word_count}\n")


if __name__ == "__main__":
    main()
