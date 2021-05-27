class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        maximumValue = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                absoluteValue = abs(self.__elements[i] - self.__elements[j])
                if absoluteValue > maximumValue:
                    maximumValue = absoluteValue
        self.maximumDifference = maximumValue


# End of Difference class

_ = input("Number of arrays")
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
