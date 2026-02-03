def chkAnagram(str1,str2):

    if(len(str1) != len(str2)):
        print(f"{str1} and {str2} are not anagram strings")
    else:
        dict1 = {}
        dict2 = {}

        for ele in str1:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1

        for ele in str2:
            if ele in dict2:
                dict2[ele] = dict2[ele] + 1
            else:
                dict2[ele] = 1

        if(dict1 == dict2):
            print(f"{str1} and {str2} are anagram strings")
        else:
            print(f"{str1} and {str2} are not anagram strings")


str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

chkAnagram(str1,str2)