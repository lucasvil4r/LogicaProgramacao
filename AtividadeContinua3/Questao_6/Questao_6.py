def mediap(vet, n):
    s=0
    cp=0
    pos=0
    while pos<n:
        if vet[pos]%2==0:
            cp=cp+1
            s=s+vet[pos]

        pos=pos+1
                    
    return s / cp

print(mediap([2, 6, 8, 9, 3, 12, 14], 7))
