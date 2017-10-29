class FM:
    def __init__(self,string):
        self.string = string
        self.BW = None
        self.c = None
    #Creates an array that hold the BW info
    def bw(self):
        self.BW = []
        substrings = []
        for i in range(len(self.string)):
            substrings.append(self.string[i:] + str(i))
        #Sorts suffixs by lexigraphical order
        substrings.sort()
        change = True
        print(substrings)
        temp = {}
        #adds to the disctionary, to create new arrays of for each suffix starting with a particular character
        for k in range(len(substrings) - 1):
            temp1 = substrings[k]
            key = temp1[0]
            if key in temp:
                temp[key].append(temp1)
            else:
                temp[key] = [temp1]
        substrings.clear()
        print(temp)
        #Sorts each array of suffix with common starting character, by length
        for i in temp:
            temp_arr = temp[i]
            temp_arr.sort(key = len)
            for k in temp_arr:
                #adds suffixs in lexigraphical order and length
                substrings.append(k)
        print(substrings)
        print(self.BW)
        for k in substrings:
            ind = int(k[len(k) - 1])

            self.BW.append(self.string[ind - 1])
        print(self.BW)
    #Creates a dicitonary that holds the C values for each char in the string
    def char_count(self):
        self.c = {}
        temp  = list(self.string)
        temp.sort()
        self.c[temp[1]] = 1
        char = temp[1]
        print(temp)
        for k in range(len(temp)):
            if temp[k] != char:
                self.c[temp[k]] = k
                char = temp[k]
    #Returns the number of occurences of a specified char in the specified range.
    def occ(self,char,index):
        sub = self.BW[0:index]
        print(self.BW)
        print(sub)
        return(sub.count(char))
    def backwards(self,pattern):
        sp = self.c[pattern[len(pattern - 1)]]
        print(sp)
        ep = 0
        range = (0,0)

        #for i in range(len(pattern)):




if 'name == __main__' :
    fm1 = FM("acgtcga$")
    fm1.bw()
    fm1.char_count()
    fm1.backwards('ac')
