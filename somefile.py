print "From file changed where are you"

def process(input):
    if not "please" in input:
        return "Won't do, no please in input"
    elif len(input) < 10:
        return "Input to short"
    else:
        return "Here you are! {}".format(input)