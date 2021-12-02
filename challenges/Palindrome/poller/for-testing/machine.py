from generator.actions import Actions
import random
import string

class Palindrome(Actions):
    def start(self):
        pass

    def banner(self):
        # Confirm the initial empty line
        self.read(delim='\n', expect='\n')
        # Confirm the actual banner
        self.read(delim='\n', expect='Welcome to Palindrome Finder\n')

    def request(self):
        # Skip the empty line
        self.read(delim='\n', expect='\n')
        # Confirm the request
        self.read(length=37, expect='\tPlease enter a possible palindrome: ')

    def palindrome(self):
        # TODO: Implement
        # generate a random halfword string
        # duplicate and invert the halfword
        # append the previous to the halfword to obtain a palindrome
        # write the palindrome
        # read from the service the message "Yes, that's a palindrome!"
        pass

    def not_palindrome(self):
        # TODO: Implement
        # generate a random word
        # verfy if the word is not a palindrome, in case it is, generate a new one
        # write the palindrome
        # read from the service the message "Nope, that's not a palindrome"
        pass

    def is_palindrome(self, word):
	for i in range(0, len(word) / 2):
		if word[i] != word[-i - 1]:
			return False
	return True

    def random_string(self, size):
        chars = string.letters + string.digits
        return ''.join(random.choice(chars) for _ in range(size))

