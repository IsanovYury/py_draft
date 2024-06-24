#Description:
#Given a string, remove any characters that are unique from the string.

#Example:
#input: "abccdefee"
#output: "cceee"

def only_duplicates(st):
    string = ''
    for i in st:
        if st.count(i) > 1:
            string = string + i
    return string
