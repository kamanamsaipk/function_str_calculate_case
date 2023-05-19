def count_case():
    upper_case =0
    lower_case =0
    sentence_input = input("enter the sentence : ")
    for sentence in sentence_input:
        if sentence.isupper():
            upper_case +=1
        elif sentence.islower():  
            lower_case +=1
        else:
            pass
    print ("original String: ", sentence_input)
    print ("no of uppercase: ", upper_case)
    print ("no of lowercase: ", lower_case)
count_case()