
import os
import numpy as np

def all_unique_char(s):
    
    N = len(s)
    status = np.zeros(256)
    for c in s:
        if(status[ord(c)]):
            return False
        else:
            status[ord(c)] = 1

    return True

def is_permutation(s1, s2):
    
    if(len(s1) != len(s2)):
        return False

    s1_sorted = ''.join(sorted(s1))
    s2_sorted = ''.join(sorted(s2))

    return s1_sorted == s2_sorted

def urlity(s):
    
    N = len(s)

    res = list()

    n = 0
    while n<N:
        if(s[n] == ' '):
            for m in range(n+1, N):
                if(s[m] != ' '):
                    n = m
                    break

            res.append('%20')
        else:
            res.append(s[n])
            n += 1

    return ''.join(res)

def is_permutation_of_palindrome(s):

    char_dict = dict()

    for c in s:
        if(c in char_dict):
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    num_odd  = 0
    for k in char_dict:
        if(char_dict[k] % 2 == 1):
            num_odd += 1

    return num_odd>1

def is_one_remove(s1, s2):
    if(len(s1)>len(s2)):
        s_long = s1
        s_short = s2
    else:
        s_long = s2
        s_short = s1

    ind_long = 0
    ind_short = 0

    has_diff_char = False

    while ind_long<len(s_long) and ind_short<len(s_short):
        if(s_long[ind_long]!=s_short[ind_short]):
            ind_long += 1
            if(has_diff_char is False):
                has_diff_char = True
                if(s_long[ind_long]!=s_short[ind_short]):
                    return False
            else:
                return False
        else:
            ind_long += 1
            ind_short += 1

    return True

    # for n in range(len(s_long)):
    #     s_long_removed = s_long[:n] + s_long[n+1:]
    #     if(s_long_removed == s_short):
    #         return True

    #return False

def is_one_insert(s1, s2):
    return is_one_remove(s1, s2)

def is_one_replace(s1, s2):
    count = 0
    for ind in range(len(s1)):
        if(s1[ind] != s2[ind]):
            count += 1

    return count<=1

def is_one_edit_away(s1, s2):
    N1 = len(s1)
    N2 = len(s2)

    if(N1==N2):
        return is_one_replace(s1, s2)
    elif (abs(N1-N2)==1):
        return is_one_remove(s1, s2) or is_one_insert(s1, s2)
    else:
        return False

def rotate_90(data):

    M, N = data.shape

    data2 = np.zeros((N, M))

    for r in range(M):
        for c in range(N):
            data2[N-c-1, r] = data[r, c]

    return data2

def set_zeros(data):

    M, N = data.shape

    R, C = np.where(data==0)

    for k, r in enumerate(R):
        data[r, :] = 0
        data[:, C[k]] = 0

    return data

def is_string_rotate(s1, s2):

    if(len(s1)!=len(s2)):
        return False

    ind = s1.find(s2[0])
    if(ind<0):
        return False

    if(s1[ind:]==s2[:len(s1)-ind] and s1[:ind]==s2[len(s2)-ind:]):
        return True

    return False

    M, N = data.shape

    R, C = np.where(data==0)

    for k, r in enumerate(R):
        data[r, :] = 0
        data[:, C[k]] = 0

    return data    

# test the code
if (__name__ == '__main__'):
    assert all_unique_char('test') is False
    assert all_unique_char('HUi Xue') is True
    assert all_unique_char('Hi Xue') is True

    assert is_permutation('Hi Xue', "test") is False
    assert is_permutation('estt', "test") is True

    is_permutation_of_palindrome('tocttcoa')

    print(is_one_edit_away('pale', 'pal'))
    print(is_one_edit_away('pale', 'bal'))
    print(is_one_edit_away('pale', 'bale'))

    data = np.reshape(np.arange(12), (4, 3))
    data2 = rotate_90(data)
    print(data)
    print(data2)

    data[2, 1] = 0
    print(data)
    print(set_zeros(data))

    print(is_string_rotate("abcd", "dabc"))
    print(is_string_rotate("abcd", "dcbb"))
    print(is_string_rotate("abcd", "efg"))