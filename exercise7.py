#ergasia7
#python 3.7.1
print("--------------------------------------")
print("PLAYER VS PC")
print("--------------------------------------")
def main(user,pc, new):
    a = sign(user,pc)
    user = a[0]
    pc = a[1]
    
    print (user)
    print (pc)
    if pc == "O" :
        print ("Ξεκινάς πρώτος")
        draw(new)
        userF(user,pc, new)
    else :
        print ("Ο  PC αρχίζει πρώτος")
        draw(new)
        pcF(user,pc, new)




new = ['','','','','','','','','']
user = ''
pc = ''
null = ''


def sign(user,pc):
    user = input("Διάλεξε X ή Ο.Αν επιλέξετε Χ παίζετε πρώτοι")
    while user not in ('x','χ','X','Χ','o','ο','O','Ο'):
        user = input("Το στοχείο που πληκτρολογήσατε δεν αντιστοιχεί στον χαρακτήρα Χ ή Ο ,ξαναπροσπαθήστε ")
    if user == 'x' or user == 'X'or user == 'χ' or user == 'Χ':
        print ("Το Χ επιλέχθηκε")
        pc = 'o'
    else:
        print ("Το O επιλέχθηκε")
        pc = 'x'
    return user.upper(), pc.upper()
    


def draw(a):
    
    print ("\n\t",a[0],"|",a[1],"|",a[2])
    print ("\t", "--------")
    print ("\n\t",a[3],"|",a[4],"|",a[5])
    print ("\t", "--------")
    print ("\n\t",a[6],"|",a[7],"|",a[8],"\n")




#Περίπτωση οπου ο χρηστης αρχιζει πρωτος
def userF(user,pc, new):
    while winn(user,pc, new) is None:
        move = user_turn(user, new)
        new[int(move)] = user
        draw(new)
        if winn(user,pc, new) != None:
            break
        else:
            pass
        print ("Ο  PC επέλεξε:",end=" ")
        p_move = pc_turn(user,pc, new)
        print (p_move)
        new[int(p_move)] = pc
        draw(new)
    w = winn(user,pc, new)
    if w == 1:
         print ("ΝΙΚΗΣΕΣ ")
    elif w == 0:
        print ("ΕΧΑΣΕΣ ")
    else:
        print ("ΙΣΟΠΑΛΙΑ!")
   



#Περίπτωση οπου ο υπολογιστης αρχιζει πρωτος
def pcF(user,pc, new):
    while not winn(user,pc, new):
        print ("Ο  PC επέλεξε:",end=" ")
        p_move = pc_turn(user,pc, new)
        print (p_move)
        new[p_move] = pc
        draw(new)
        if winn(user,pc, new) != None:
            break
        else:
            pass
        move = user_turn(user, new)
        new[int(move)] = user
        draw(new)
    w = winn(user,pc, new)
    if w == 1:
         print ("ΝΙΚΗΣΕΣ")
    elif w == 0:
         print ("ΕΧΑΣΕΣ!")
    else:
        print ("ΙΣΟΠΑΛΙΑ!")



#Οταν ειναι η σειρα του χρηστη
def user_turn(user, new): 
    a = input("Επιλέξτε μία θέση.Το κάθε κουτάκι αντιστοιχεί σε ένα αριθμό από το 0-8(νούμερο 0 το πάνω αριστερά κουτάκι,νούμερο 8 το κάτω δεξία) ")
    while True:
        if a not in ('0','1','2','3','4','5','6','7','8'):#περιπτωση που ως εισοδο δοθηκε μη επιτρεπτο στοιχειο
            a = input("Το στοχείο που πληκτρολογήσατε δεν αντιστοιχεί σε κάποια θεση,ξαναπροσπάθησε!")
        elif new[int(a)] != null:#περιπτωση που η θεση δεν ειναι κενη
            a = input("αυτή η θέση είναι ήδη συμπληρωμένει,ξαναπροσπάθησε!")
        else:
            return int(a)


#Οταν ειναι η σειρα του υπολογιστη
def pc_turn(user,pc, new):
    find=1
    for i in range(0,9):
        if new[i] == null and find==1:
            find=0
            thesi=i
    return int(thesi)



def winn(user,pc, new):
    tropoi = ((0,1,2),(0,4,8),(0,3,6),(2,4,6),(2,5,8),(3,4,5),(6,7,8),(1,4,7))
    #ελεγχος αν υπαρχει ενας συνδιασμος απο το tropoi ή αν δεν εχει απομείνει κανενας απο αυτους
    for i in tropoi:
        if new[i[0]] == new[i[1]] == new[i[2]]: 
            winner = new[i[0]]
            if winner== user:
                return 1
            elif winner==pc:
                return 0          
    if null not in new: 
        return 'TIE'    
    return None

main(user,pc, new)
input("Press enter to exit")
