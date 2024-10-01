#!/usr/bin/python

import os, re

spigot = {}
spigot["org.bukkit"] = []

for root, dirs, files in os.walk("./bin/Bukkit/src/main/java/org/bukkit"):
    for name in files:
        fullname = root+"/"+name
        print("> "+fullname)
        f = open(fullname, "r+")
        lines = "".join(f.readlines())

        lines = re.sub("if \((.*)\) \{", "if (true) {",lines)
        
        f.seek(0)
        f.truncate(0)
        f.write(lines)
        f.close()

print("""
You now need to change Bukkit's pom.xml to use the json doclet.
      
Make said modifications, then run the javadoc command with the appropriate JAVA_HOME variable set:

JAVA_HOME=/usr/lib/jvm/java-11-openjdk mvn javadoc:javadoc
      
Changes to make:

Change maven.compiler.release to 11.
      
Add this to the configuration block for maven-javadoc-plugin: 
<doclet>com.raidandfade.JsonDoclet.Main</doclet>
<docletPath>[[FULL PATH]]/SpigotJSON/bin/json-jdoc.jar</docletPath>
<links>
    <link>https://guava.dev/releases/31.1-jre/api/docs/</link>
</links>
<tags>
    <tag>
        <name>apiNote</name>
        <placement>a</placement>
        <head>API Note:</head>
    </tag>
</tags>
<useStandardDocletOptions>false</useStandardDocletOptions>
      

""")