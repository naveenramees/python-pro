i,k = map(int,raw_input().split())

i = i ^ k;
k = i ^ k;
i = i ^ k;

print i, k
