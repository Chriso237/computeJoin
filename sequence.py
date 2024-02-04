def compute_join_point(a:int, b:int):
    def somme_chiffre(num):
        return sum(int(i) for i in str(num))
    
    def generateur_seq(number):
        var = number
        while True:
            yield var
            var = var + somme_chiffre(var)

    seq1 = generateur_seq(a)
    seq2 = generateur_seq(b)

    while True:
        value1 = next(seq1)        
        value2 = next(seq2)
        if value1 == value2 and value1 < 20000000:
            return value1


#point1= 471
#point2= 480
#print(compute_join_point(point1, point2))