#​ ​there​ ​must​ ​be​ ​different​ ​way​ ​and​ ​test​ ​5,​ ​6,​ ​7​ ​are​ ​failed​ ​because​ ​to​ ​
#​ ​​ ​time​ ​exceeded

#​ ​*******************************************
#​ ​getting​ ​xor​ ​from​ ​1​ ​-​ ​n​ ​
def​ ​get_Xor(n):
​ ​​ ​​ ​​ ​if​ ​n​ ​%​ ​4​ ​==​ ​0:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​n
​ ​​ ​​ ​​ ​elif​ ​n​ ​%​ ​4​ ​==​ ​1:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​1
​ ​​ ​​ ​​ ​elif​ ​n​ ​%​ ​4​ ​==​ ​2:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​n​ ​+​ ​1
​ ​​ ​​ ​​ ​
​ ​​ ​​ ​​ ​return​ ​0

#​ ​when​ ​xor​ ​of​ ​1->(l-1)​ ​and​ ​xor​ ​1​ ​->​ ​r​ ​are​ ​xored​ ​it​ ​return​ ​xor​ ​of​ ​uncommon
#​ ​part::​ ​l​ ​->​ ​r​ ​
def​ ​xor_with_range(left,right):
​ ​​ ​​ ​​ ​return​ ​(get_Xor(left​ ​-1)​ ​^​ ​get_Xor(right))
​ ​​ ​​ ​​ ​
​ ​​ ​​ ​​ ​
def​ ​solution(start,​ ​length):
​ ​​ ​​ ​​ ​#​ ​Your​ ​code​ ​here
​ ​​ ​​ ​​ ​ans​ ​=​ ​0
​ ​​ ​​ ​​ ​to_left​ ​=​ ​0
​ ​​ ​​ ​​ ​
​ ​​ ​​ ​​ ​for​ ​_​ ​in​ ​range(length):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​right​ ​=​ ​start​ ​+​ ​length​ ​-​ ​1​ ​-​ ​to_left
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​start​ ​<​ ​2000000001:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​right​ ​>​ ​2000000000:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​ans​ ​^=​ ​xor_with_range(start,​ ​2000000000)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​ans
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​ans​ ​^=​ ​xor_with_range(start,​ ​right)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​else:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​ans
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​to_left​ ​+=​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​start​ ​=​ ​start​ ​+​ ​length​ ​

​ ​​ ​​ ​​ ​return​ ​ans