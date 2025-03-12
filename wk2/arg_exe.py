import sys

# avg = 0
# for length in range(1,len(sys.argv)):
#     avg += int(sys.argv[length])

nums = [int(v) for v in sys.argv[1:]]
avg = sum(nums)/(len(sys.argv)-1)

if avg >= 5:
    print(f"{avg} Pass")
else:
    print(f"{avg} Fail")