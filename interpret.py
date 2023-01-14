import pandas as pd 
import matplotlib.pyplot as plt
# %matplotlib inline
df=pd.read_csv("final.csv")

#row_num,name,start_name,distance,mass,radius,gravity
n=df["star_name"].to_list()
m=df["Mass"].to_list()
r=df["Radius"].to_list()
d=df["Distance"].to_list()
g=df["Gravity"].to_list()
print(df.head())
print(n[0:9])
plt.figure(figsize=(10,5))
plt.title("star solar mass")
plt.bar(n[0:9],m[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("star solar radius")
plt.bar(n[0:9],r[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("star solar distance")
plt.bar(n[0:9],d[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("star solar gravity")
plt.bar(n[0:9],g[0:9])
plt.show()

