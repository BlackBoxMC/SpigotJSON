#!/usr/bin/python

import os, json

spigot = {}
spigot["org.bukkit"] = []

for root, dirs, files in os.walk("./bin/Bukkit/target/site/apidocs/docs/"):
    for name in files:
        if name.endswith((".json")):
            f = open(os.getcwd()+"/bin/Bukkit/target/site/apidocs/docs/"+name)
            j = json.loads("\n".join(f.readlines()))
            spigot["org.bukkit"].append(j)
            f.close()

f = open(os.getcwd()+"/spigot.json","w+")
f.write(json.dumps(spigot))
f.close() 
