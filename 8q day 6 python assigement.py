start = 12;
end = 19;
count = 0;

print("Composite Numbers between %d and %d: " % (start, end));

for start in range(start, end+1):
    for i in range(1, start+1):
        if(start % i == 0):
            count += 1;
    if(count > 2):
       print(start, end=" ")
    count = 0
