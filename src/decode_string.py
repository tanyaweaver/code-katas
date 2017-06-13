def decodeString(s):
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            substr = ''
            while len(stack) > 0:
                cur = stack.pop()
                if cur != '[':
                    substr += cur
                else:
                    break
            if cur == '[':
                num = ''
                while len(stack) > 0:
                    cur = stack.pop()
                    if cur.isdigit():
                        num += cur
                    else:
                        stack.append(cur)
                        break
            new_string = int(num[::-1]) * substr[::-1]
            for x in new_string:
                stack.append(x)
    return ''.join(stack)

# 
# def decodeString_recursive(s):
#     if not s: return ''
#     if s[0].isdigit():
#         i = s.find('[')
#         bal = 0
#         for j in xrange(i, len(s)):
#             bal += s[j] == '['
#             bal -= s[j] == ']'
#             if bal == 0: break
#         return decodeString(s[i+1:j]) * int(s[:i]) + decodeString(s[j+1:])
#     else:
#         return s[0] + decodeString(s[1:])


if __name__ == '__main__':
    s = "sd2[f2[e]g]i"
    print 'answer', decodeString(s)
