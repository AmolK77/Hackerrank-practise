
#find substring in string
def count_substring(string,substring):
    count=0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count+=1
        print(count)
        return count

if __name__=="__main__" :
    count_substring("amolamol","amol")