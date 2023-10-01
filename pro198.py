import time
import sys

d = {1: ["coffee", 2, 3],
2: ["tea",4, 2],
3: ["flour", 17.22, 4],
4: ["tent", 10.55, 5],
5: ["speaker", 69.22, 6],
6: ["drugs", 1.55, 99]
}
st =0
total =0
print("Getting your items:")
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n") 

print ("{:<8} {:<15} {:<10} {:<10} {:<10}".format('S.no','product','cost','quantity',"subtotal"))
for k, v in d.items():
    lang, perc, change = v
    st = perc * change
    total+=st
    print ("{:<8} {:<15} {:<10} {:<10} {:<10}".format(k, lang, "$"+str(perc), change ,"$"+str(st)))
    time.sleep(0.5)

time.sleep(1)    
print("Calculating Total:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n") 
time.sleep(1)
print("adding tax")

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")


print("            Total : ",total)
 

tax = ((18*total)/100)
time.sleep(1)
print("            tax +$ ",tax)
nt = tax+total
time.sleep(2)
print("            New Total : ",nt)