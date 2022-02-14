# def solution(arr1, arr2):
#     answer=[]
#     for i in range(len(arr1)):
#         a = []
#         for j in range(len(arr1[0])):
#             a.append(arr1[i][j]+arr2[i][j])
#         answer.append(a)

#     return answer


# print(solution([[1,2], [2,3]], [[3,4], [5,6]]))

def solution(A, B):
    
    return [list(map(sum, zip(*x))) for x in zip(A, B)]

print(solution([[1,2], [2,3]], [[3,4], [5,6]]))