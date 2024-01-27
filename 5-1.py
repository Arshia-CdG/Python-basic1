class MrKrabs:
    def __init__(self, dna):
        self.dna = dna

    def modify_dna(self):
        self.dna = self.dna.replace('tt', 'o')
        return self.dna


class SpongeBob:
    def __init__(self, dna):
        self.dna = dna

    def sort_dna(self):
        sorted_dna = self.mergeSort(self.dna)
        return sorted_dna


    def mergeSort(self, arr):
        if len(arr) > 1:
 
            mid = len(arr)//2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]
 
            self.mergeSort(sub_array1)
            self.mergeSort(sub_array2)
         
            i = j = k = 0
            
            while i < len(sub_array1) and j < len(sub_array2):
                if sub_array1[i] < sub_array2[j]:
                    arr[k] = sub_array1[i]
                    i += 1
                else:
                    arr[k] = sub_array2[j]
                    j += 1
                k += 1
                
            while i < len(sub_array1):
                arr[k] = sub_array1[i]
                i += 1
                k += 1
 
            while j < len(sub_array2):
                arr[k] = sub_array2[j]
                j += 1
                k += 1
        n = 100
        for kn in range(len(arr)):
            n += int(arr[kn]) * (10 ** (len(arr) - kn - 1))
        return n

class Octopus:
    def __init__(self, dna):
        self.dna = dna

    def replace_triplets(self):
        new_dna = ""
        i = 0
        j = 0
        count = 0
        while i < len(self.dna):
            if self.dna[i] == 'x' and count == 0:
                j = i
                count += 1
            while (i + 3 < len(self.dna)) and (self.dna[i] == self.dna[i + 1]) and (self.dna[i] ==self.dna[i + 2]):
                new_dna += "(0_0)"
                i += 3
            else:
                new_dna += self.dna[i]
                i += 1
        if j != 0 :
            new_dna += str(j)
        return new_dna

def main():
    input_data = input().strip()
    if input_data.startswith("m"):
        mr_krabs = MrKrabs(input_data[1:] + input_data[:10])
        print('m' + mr_krabs.modify_dna())
    elif input_data.startswith("sb"):
        sponge_bob = SpongeBob(list(str(len(input_data))))
        print(sponge_bob.sort_dna())
    elif input_data.startswith("s") and not input_data.startswith("sb"):
        octopus = Octopus(input_data[0:])
        print(octopus.replace_triplets())
    elif input_data[len(input_data) - 1] == 'm':
        input_data = input_data[::-1]
        mr_krabs = MrKrabs(input_data[1:] + input_data[:10])
        print('m' + mr_krabs.modify_dna())
    elif (input_data[len(input_data) - 1] == 's') and (input_data[len(input_data) - 2] == 'b'):
        input_data = input_data[::-1]
        sponge_bob = SpongeBob(list(str(len(input_data))))
        print(sponge_bob.sort_dna())
    elif (input_data[len(input_data) - 1] == 's') and (input_data[len(input_data) - 2] != 'b'):
        input_data = input_data[::-1]
        octopus = Octopus(input_data[0:])
        print(octopus.replace_triplets())
    else:
        print('invalid input')

if __name__ == "__main__":
    main()
