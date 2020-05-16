def get_sub_strs(s: str) -> list:
    sub_str = []
    for i in range(len(s)): 
        for l in range(i+1, len(s)+1 ): sub_str.append(s[i: l])
    return sub_str

def get_sub_strs_2(s: str) -> list:
    return [s[i: l] for i in range(len(s)) for l in range(i+1, len(s) + 1)]
    

print(get_sub_strs('abc'))
print(get_sub_strs_2('abc'))