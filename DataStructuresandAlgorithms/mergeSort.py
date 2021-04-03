def mergeSort(n):
    #print("Splitting ", n)
    if len(n) > 1:
        mid = len(n) // 2
        lefthalf = n[:mid]
        righthalf = n[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                n[k] = lefthalf[i]
                i=i+1
            else:
                n[k] = righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            n[k] = lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            n[k] = righthalf[j]
            j=j+1
            k=k+1