# SpigotJSON

New repo for generating `spigot.json`, directly from the sources this time.

# Usage

The tool is only supported on Linux/WSL. You need Java 21 to build it of course, but you then need Java 11 to actually generate the json file.

After all prerequesites are met:

- Run `./generate.sh` to clone/build the Spigot repos
- Run `python strip.py` to strip out stuff that Java 11 can't compile (this does exclude any functions from the final output, it just removes any errors)
- Make the changes it tells you (and run the commands it tells you to)
- Run `python consolidate.py`
