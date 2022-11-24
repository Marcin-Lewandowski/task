def palindrom(slowo):
    """
        This function performs palindrome check for a string
        Prints True or False based on argument passed
        Argument:  slowo
        
    """
    if slowo == slowo[::-1]:
        return True
    else:
        return False
    

print(palindrom("potop"))
print(palindrom("klawiatura"))