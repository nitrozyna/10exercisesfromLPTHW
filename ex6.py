x = "There are %d types of people." % 10 #putting 10 into a string called x
binary = "binary" #defining a variable
do_not = "don't" #defining a variable
y = "Those who know %s and those who %s" % (binary, do_not) #putting defined variables into a string called y (1)

print x #displaying string x
print y #displaying string y

print "I said: %r." % x # putting x into a new statement (2)
print "I also said: '%s'." % y #putting y into a statement (3)

hilarious = False #defining not funny
joke_evaluation = "Isn't that joke so funny?! %r" #creating a new statement

print joke_evaluation % hilarious #displaying a string in a string (4)
w = "This is the left side of..." #statement no.1
e = "a string with a right side." #statement no.2

print w + e #adding both strings together
