diffs=[];months=["January","February","March","April","May","June","July","August","September","October","November","December"];day=[];night=[]

for x in range(12):
  d="\nInput Daytime High for", months[x];d=input(d[0]+str(" "+d[1])+": ")
  n="Input Nighttime High for", months[x];n=input(n[0]+str(" "+n[1])+": ")
  difference = float(d)-float(n)
  while difference<0:
    print("\nThe Daytime High for", months[x], "["+str(d)+"] is lower than the Nighttime low ["+str(n)+"]. Please retype the data for Daytime High")
    d=float(input(">> "))
    difference=int(d)-int(n);
    if difference>0:
      diffs.append(round(difference,1));day.append(float(d));night.append(float(n))
  else:
    diffs.append(round(difference,1));day.append(float(d));night.append(float(n))

print("Average Annual Daytime High: ", round(sum(day)/len(day),1)); print("Average Annual Nighttime High: ", round(sum(night)/len(night),1))
print("\nDifferences by month: \n",diffs)

print("-- Maximum Difference(s) --")
if diffs.count(max(diffs)) > 1:
  for i in range(diffs.count(max(diffs))):
    print(months[diffs.index(max(diffs))],"has a difference of", max(diffs))
    diffs[diffs.index(max(diffs))]=diffs[diffs.index(max(diffs))]-1
else:
  print(months[diffs.index(max(diffs))],"has a difference of", max(diffs))

print("\n-- Minimum Difference(s) --")
if diffs.count(min(diffs)) > 1:
  for i in range(diffs.count(min(diffs))):
    print(months[diffs.index(min(diffs))],"has a difference of", min(diffs))
    diffs[diffs.index(min(diffs))]=diffs[diffs.index(min(diffs))]+1
else:
  print(months[diffs.index(min(diffs))],"has a difference of", min(diffs))