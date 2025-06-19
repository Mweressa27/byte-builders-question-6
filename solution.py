# PSEUDOCODE
# Function takes argumants(A, K)

#     IF A is empty
#         RETURN A

#     IF K is 0
#         RETURN A

#     SET N = length of A

#     SET K = K MOD N   // Adjust K if it is  larger than the list

#     FOR i FROM 0 TO K - 1 DO
#         SET last = last element of A
#         REMOVE last element from A
#         INSERT last at the beginning of A

#     RETURN A


def solution(A, K):
    # If the list is empty, return it
    if len(A) == 0:
        return A    

    # If no rotation is needed(K=0), return the list
    if K == 0:
        return A    

    N = len(A)

    # If K is larger than the list, rotate only K % N times
    K = K % N
    # K % N means how many extra rotations are needed after full loops

    for i in range(K):
        last = A[-1]           # Get the last element
        A.pop()                # Remove the last element
        A.insert(0, last)      # Insert it at the beginning

    return A



print(solution([3, 8, 9, 7, 6], 3))  
# [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

print(solution([1, 2, 3, 4], 4))     
# [1, 2, 3, 4] -> [4, 1, 2, 3] -> [3, 4, 1, 2] -> [2, 3, 4, 1] -> [1, 2, 3, 4]



