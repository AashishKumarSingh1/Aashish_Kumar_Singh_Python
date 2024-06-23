t = int(input())
if 1 <= t <= 100:
    for _ in range(t):
        n = int(input())  # length of string s
        s = input().strip()  # read the DNA sequence

        if 1 <= n <= 100 and all(char in 'ATGC' for char in s):
            complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

            result = ''.join(complement[char] for char in s)

            print(result)


# # cook your dish here
# t=int(input())
# if t>=1 and t<=100:
#     for _ in range(t):
#         n=int(input())#length of string s
#         s=input()
#         dna=['A','T','G','C']
#         if n>=1 and n<=100 and s in dna:
#             # dna_c=[None for _ in range(4)]
#             dna_c=[]
#             for char in dna:
#                 if char=='A':
#                     dna_c.append("T")
#                     print('T',end="")
#                     pass
#                 elif char=="T":
#                     dna_c.append("A")
#                     print('A',end="")
#                     pass
#                 elif char=="G":
#                     dna_c.append("C")
#                     print('C',end="")
#                     pass
#                 elif char=="C":
#                     dna_c.append("G")
#                     print("G",end="")
#                     pass
#                 else:
#                     pass
            
#             # print("".join(map(str,)))
                    
        