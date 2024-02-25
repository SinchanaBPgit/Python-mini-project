def madlib_generator():
   
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    madlib = f"The {adjective} {noun} likes to {verb} {adverb}."

    print("\nYour Madlib:")
    print(madlib)

madlib_generator()
