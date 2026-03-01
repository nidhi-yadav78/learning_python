arr=[45,23,67,89,12,90,45,67]
key=90
for i in range(len(arr)):
 if arr[i]==key:
     print("element found at index of",i)
     break
else:
    print("element is not found")


