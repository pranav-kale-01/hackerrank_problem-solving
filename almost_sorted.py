from ast import pattern


def almostSorted(arr):
    pattern_desc = False
    prev_n, list_ind = arr[0], []
    desc_count, start_ind, end_ind, ind  = 0,0,0,0

    for i in arr:
        if( i < prev_n ):
            if( not pattern_desc ):
                # if the descending pattern count is less than 3
                # if there are more than 2 groups even if there is only one element in each group we can't fix the pattern using one swap
                if( desc_count < 3 ):
                    pattern_desc = True
                    start_ind = ind-1
                    desc_count += 1
                else:
                    print("no")
                    return

                # checking if this is the last element 
                if( ind+1 == len(arr) ):
                    pattern_desc = False
                    end_ind = ind
                    list_ind.append( (start_ind, end_ind ) )    
        else:
            if( pattern_desc ):
                pattern_desc = False
                end_ind = ind-1
                list_ind.append( (start_ind, end_ind ) )

        ind += 1
        prev_n = i


    # checking if the descending pattern continued till the end
    # if so adding the data to the list of indices
    if( pattern_desc ):
        list_ind.append( (start_ind, len(arr)) )

    # printing no if there are more than two points that don't follow the ascending pattern
    if( len( list_ind ) > 2 or len(list_ind) == 0):
        print("no")
        return 

    # if there are only two groups that don't follow the ascending pattern 
    elif( len( list_ind ) == 2 ): 
        # checking if the these two groups consists more than one element each
        # if so, we cannot swap and more than one element at a time so printing no and returing
        for i in list_ind:
            if( i[1] - i[0] > 1 ):
                print("no")
                return

        # checking if swapping the elements fixes the pattern
        # if so printing swap and the index for both the elements and returning
        if( arr[list_ind[0][0]] >= arr[list_ind[1][0]] and arr[list_ind[0][1]] >= arr[list_ind[1][1]] ):
            print("yes")
            print('swap', list_ind[0][0]+1, list_ind[1][1]+1 )

    # this means that there is only one point (or one group of point) that don't follow the ascending pattern  
    else:
        # checking if the group has only one element or more than one element
        if( list_ind[0][1] - list_ind[0][0] == 1 ):
            if( list_ind[0][0] == 0 and list_ind[0][1] == len(arr)-1 ):
                print("yes")
                print("swap", list_ind[0][0]+1, list_ind[0][1]+1)
                return
            else:
                if( list_ind[0][0] == 0 ):
                    if( arr[ list_ind[0][0] ] < arr[ list_ind[0][1] + 1] ):
                        print("yes")
                        print("swap", list_ind[0][0]+1, list_ind[0][1]+1)
                    else:
                        print("no")
                        return        
                elif( list_ind[0][1] == len(arr) - 1 ):
                    if( arr[ list_ind[0][0] ] < arr[ list_ind[0][1] + 1] ):
                        print("yes")
                        print("swap", list_ind[0][0]+1, list_ind[0][1]+1)
                    else:
                        print("no")
                        return      
                else:
                    if( arr[ list_ind[0][0] ] < arr[ list_ind[0][1] + 1] and arr[ list_ind[0][1] ] > arr[ list_ind[0][0] -1 ] ):
                        print("yes")
                        print("swap", list_ind[0][0]+1, list_ind[0][1]+1)
                    else:
                        print("no")
                        return      
        else:
            # checking if reversing the group of elements (sub-list) fixes the pattern
            # if so printing reverse and the start and end index and returning
            if( list_ind[0][0] == 0 and list_ind[0][1] != len(arr) ):
                if( arr[list_ind[0][0]] < arr[list_ind[0][1] + 1] ):
                    print("yes")
                    print( "reverse", list_ind[0][0]+1, list_ind[0][1] + 1 )

            elif( list_ind[0][0] != 0 and list_ind[0][1] == len(arr) ):
                if( arr[list_ind[0][1]] > arr[list_ind[0][0] - 1] ):
                    print("yes")
                    print( "reverse", list_ind[0][0]+1, list_ind[0][1] + 1 )

            elif( list_ind[0][0] != 0 and list_ind[0][1] != len(arr) ):
                if( arr[list_ind[0][1]] > arr[list_ind[0][0] - 1] and arr[list_ind[0][0]] < arr[list_ind[0][1] + 1] ):
                    print("yes")
                    print( "reverse", list_ind[0][0]+1, list_ind[0][1] + 1 )

            else:
                print("yes")
                print( "reverse", list_ind[0][0]+1, list_ind[0][1]+1 )

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
