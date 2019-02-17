arxh = "0"
lista=[]
print("Πατήστε ENTER για να σταματήσετε την εκχώρηση.")
while arxh!="" :
    arxh = input("Πληκτρολογήστε τον πρώτο αριθμό του διαστήματος")
    if arxh != "":
        arxh = int(arxh)
        telos = int(input("Πληκτρολογήστε τον δεύτερο αριθμό του διαστήματος"))
        lista.append([arxh,telos])
print(lista)

def sumIntervals(lista):
    array_length = len(lista)
    for i in range(array_length):
        for j in range(array_length):
            if i!=j:
                z=1
                v=1
                a=(lista[i][1])-(lista[j][1])
                b=(lista[j][1])-(lista[i][0])
                c=(lista[i][1])-(lista[j][0])
                if lista[i][1]==0 and lista[i][0]==0:
                    z=0
                if lista[j][1]==0 and lista[j][0]==0:
                    v=0
                if a>0 and b>=0 and lista[i][0]>=lista[j][0] and z==1 and v==1:
                    lista[i][0]=lista[j][0]
                    lista[j][0]=0
                    lista[j][1]=0
                elif c>0 and lista[j][1]>lista[i][1] and z==1 and v==1:
                    lista[i][1]=lista[j][1]
                    lista[j][0]=0
                    lista[j][1]=0
        q=0
        for i in range(array_length):
            q=q+(lista[i][1] - lista[i][0])
        print("Το άθροισμα του μήκους των διαστημάτων είναι:",q)
print(sumIntervals(lista))
