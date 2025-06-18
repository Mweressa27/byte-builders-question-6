# FUNCTION solution(A, K)
#     N ← length of A
    
#     IF N == 0 THEN
#         RETURN A
    
#     K ← K MOD N  // To handle cases where K >= N
    
#     rotatedPart ← last K elements of A (A[-K:])
#     remainingPart ← first (N - K) elements of A (A[:-K])
    
#     RETURN concatenation of rotatedPart and remainingPart

# Example
# Given A = [3, 8, 9, 7, 6] and K = 3:

# N = 5

# K % N = 3

# A[-3:] = [9, 7, 6]

# A[:-3] = [3, 8]

# Result: [9, 7, 6] + [3, 8] = [9, 7, 6, 3, 8]


def solution(A, K):
    N = len(A)
    if N == 0:
        return A  # Empty array remains the same
    K = K % N  # No need to rotate more than N times
    return A[-K:] + A[:-K]

print(solution([3, 8, 9, 7, 6], 3))  # Output: [9, 7, 6, 3, 8]
print(solution([0, 0, 0], 1))        # Output: [0, 0, 0]
print(solution([1, 2, 3, 4], 4))     # Output: [1, 2, 3, 4]


# FUNCTION solution(A, K):
#     IF A is empty OR K == 0:
#         RETURN A
#     N = length of A
#     K = K MOD N  // Effective number of rotations
#     IF K == 0:
#         RETURN A
#     rotated_part = last K elements of A
#     remaining_part = all elements of A except the last K elements
#     RETURN rotated_part + remaining_part

# Explanation
# Check for Edge Cases:

# If the input array A is empty or the number of rotations K is zero, return the array as-is since no rotation is needed.

# Calculate Effective Rotations:

# Compute K MOD N where N is the length of the array. This handles cases where K is larger than N by reducing it to the equivalent rotations within a single cycle.

# Check for No Rotation Needed:

# If the effective rotations K is zero after the modulo operation, return the original array as no rotation is needed.

# Perform Rotation:

# rotated_part: Extract the last K elements of the array.

# remaining_part: Extract all elements except the last K elements.

# Concatenate rotated_part followed by remaining_part to form the rotated array.

# Return Result:

# Return the concatenated result which is the array rotated K times to the right.


def solution(A, K):
    if not A or K == 0:
        return A
    N = len(A)
    K = K % N
    if K == 0:
        return A
    return A[-K:] + A[:-K]