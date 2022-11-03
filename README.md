# ATTACK-Attributor
A Python command-line tool used to attribute a set of TTPs to APT groups. Takes in a Mitre ATTACK Navigator json file, and prints out the top 10 most similar APT groups.

# Usage
```
> .\groupmapper.py .\G1002-enterprise-layer.json
APT   | Match
G1002 | 100.0 %
G0016 | 87.5 %
G0050 | 75.0 %
G0032 | 68.75 %
G0007 | 62.5 %
G0094 | 62.5 %
G0080 | 62.5 %
G0047 | 56.25 %
G0129 | 56.25 %
G0092 | 56.25 %
```
