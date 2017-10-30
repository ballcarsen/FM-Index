class FM:
    def __init__(self,string):
        self.string = string
        self.BW = None
        #The index in the string at which the corresponding suffix to the Burrows Wheeler exists
        self.saI = None
        self.c = None
    #Creates an array that hold the BW info
    def bw(self):
        self.BW = []
        substrings = []
        self.saI  = []
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
            self.saI.append(ind)
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
    #Returns the number of occurences of a specified char in the specified range of the BW.
    def occ(self,char,index):
        sub = self.BW[0:index]
        print(self.BW)
        print(sub)
        return(sub.count(char))
    #backwards pattern matching
    def backwards(self,pattern):
        sp = self.c[pattern[len(pattern ) - 1]]
        #what happens if it is the last lexogrpahical char?
        ep = self.c[self.findNextChar(pattern[len(pattern ) - 1])]
        for k in range(len(pattern) - 1):
            print(k)
            print(len(pattern))
            char = pattern[len(pattern) - k - 2]
            sp = self.c[char] + self.occ(char, sp - 1)  + 1
            ep = self.c[char] + self.occ(char, ep)
        print(sp, ep)

    def findNextChar(self,char):
        exists  = False
        count = 1
        while not exists:
            if chr((ord(char) + count)) in self.c:
                return chr((ord(char)+count))
                exists = True
            else:
                count += 1




if 'name == __main__' :
    fm1 = FM("acgtcga$")
    fm1.bw()
    fm1.char_count()
    fm1.backwards('cg')
