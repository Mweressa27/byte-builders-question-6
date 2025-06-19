# PSEUDOCODE
FUNCTION RotateListRight(A, K)
    IF A is empty OR K is 0
        RETURN A

    SET N = length of A

    SET K = K MOD N   

    REPEAT K times:
        SET last = last element of A
        REMOVE last element from A
        INSERT last at the beginning of A

    RETURN A


def solution(A, K):
    # If the list is empty or no rotation is needed, return it as it is
    if not A or K == 0:
        return A

    N = len(A)

    # If K is larger than the list, rotate only K % N times
    K = K % N

    for _ in range(K):
        last = A[-1]           # Get the last element
        A.pop()                # Remove the last element
        A.insert(0, last)      # Insert it at the beginning

    return A



print(solution([3, 8, 9, 7, 6], 3))  # [9, 7, 6, 3, 8]
print(solution([1, 2, 3, 4], 4))     # [1, 2, 3, 4]



