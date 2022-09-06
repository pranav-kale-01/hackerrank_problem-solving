from ast import pattern


def almostSorted(arr):
    pattern_desc = False
    prev_n, list_ind = arr[0], []
    desc_count, start_ind, end_ind, ind  = 0,0,0,0

    for i in arr:
        if( i < prev_n ):
            if( not pattern_desc ):
                pattern_desc = True
                start_ind = ind-1
                desc_count += 1

                # checking if this is the last element 
                if( ind+1 == len(arr) ):
                    end_ind = ind
                    list_ind.append( (start_ind, end_ind ) )    
        else:
            if( pattern_desc ):
                pattern_desc = False
                end_ind = ind-1
                list_ind.append( (start_ind, end_ind ) )

        ind += 1
        prev_n = i

    print( list_ind )
    
    # printing no if there are more than two points that don't follow the ascending pattern
    if( len( list_ind ) > 2 ):
        print("no")
        return 

    # checking if there are only two points that don't follow the ascending pattern 
    elif( len( list_ind ) > 1 ): 
        # checking if these two points consist only one element or more than one element
        # if they consist more than one element then printing no and returning
        for i in list_ind:
            if( i[1] - i[0] > 1 ):
                print("no")
                return

        # if there are only two elements that does not follow the pattern checking if we can fix the pattern by swapping them


    # this means that there is only one point (or one group of point) that don't follow the ascending pattern  
    else:
        # checking if the group has only one element or more than one element
        if( list_ind[0][1] - list_ind[0][1] == 1 ):
            # this means that the group consists of only one group and only one element. so the list can't be sorted by any means
            print("no")
            return
        else:
            # checking if swapping the element will fix the pattern
            pass



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
