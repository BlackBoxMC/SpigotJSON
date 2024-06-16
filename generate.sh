cd bin
java -jar BuildTools.jar latest
cd ..
echo ""
echo "You now need to change Bukkit's pom.xml to use the json doclet, then run mvn javadoc:javadoc. When you are done, run consolidate.py to create the spigot json."
echo ""
echo "Put the following in the settings for the javadoc plugin, replacing [[FULL PATH]] with the appropriate path":
echo "<doclet>capital.scalable.restdocs.jsondoclet.ExtractDocumentationAsJsonDoclet</doclet>"
echo "<docletPath>[[FULL PATH]]/SpigotJSON/bin/json-jdoc.jar</docletPath>"
echo "<links>"
echo "    <link>https://guava.dev/releases/31.1-jre/api/docs/</link>"
echo "</links>"
echo "<tags>"
echo "    <tag>"
echo "        <name>apiNote</name>"
echo "        <placement>a</placement>"
echo "        <head>API Note:</head>"
echo "    </tag>"
echo "</tags>"
echo "<useStandardDocletOptions>false</useStandardDocletOptions>"
