
def ask_question():
    print "Who is the founder of Facebook?"
    print "- Mark Zuckerberg"
    print "- Bill Gates"
    print "- Steve Jobs"
    print "- Larry Page"

ask_question()#function is called
ask_question()
ask_question()
ask_question()
ask_question()

# loop is ran over here vas this will call the function for 100 times
i=0
while i<100:
    ask_question()
    i=i+1

"""function_print_lines naam ka ek function likho jo 2 strings leta ho, aur unko neeche diye hue dhang se print karta ho.

Jaise agar hum usko "Mera naam Rishabh hai." aur "Main NavGurukul ka co-Founder hun." denge toh woh yeh print karega

Mera naam Rishabh hai.
Main NavGurukul ka co-founder hun."""

def function_print_lines(name,work_place):# here i made a function by writing def with parameters name and work place
    print "Mera naam " + name + " hai"# this will get printed whn this function will be called and in the place of name whtever there will be in the parameter while calling the function will get printed
    print "Main " + work_place + "ka co-founder hun"# same this also will be printed whn this function be called and in the place of the work place whtever will be there in the parameter will be called

function_print_lines("Rishabh","NavGurukul")# here the upper function has been called with the parameter Rishabh and NavGurukul so at the place of name Rishabh will come and at the place of work_place NavGurukul will come
