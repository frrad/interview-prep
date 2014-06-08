def unique(input):
    seen = set()
    for char in input:
        if char in seen:
            return False
        seen.add(char)
    return True

#no extra data structures (except for verify, which we need since input str not mutable)
def unique3(input):
    verify = sorted(input)
    for i in xrange(len(input)-1):
        if verify[i]==verify[i+1]:
            return False
    return True

#like above but more pythony
def unique2(input):
    verify = sorted(input)
    for (a,b) in zip(verify[1:], verify[:-1]):
        if a==b:
            return False
    return True

def reverse(input):
    for i in xrange(len(input)/2):
        input[i], input[-1-i] = input[-1-i], input[i]
