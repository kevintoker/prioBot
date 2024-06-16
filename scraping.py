from bs4 import BeautifulSoup
import requests

url = "https://www.vlr.gg/event/agents/1999/champions-tour-2024-masters-shanghai"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

viper = 1
viperCount = 0
viperIceboxCount = 0
viperSunsetCount = 0
viperLotusCount = 0
viperBreezeCount = 0
viperBindCount = 0
viperSplitCount = 0
viperAscentCount = 0

omen = 2
omenCount = 0
omenIceboxCount = 0
omenSunsetCount = 0
omenLotusCount = 0
omenBreezeCount = 0
omenBindCount = 0
omenSplitCount = 0
omenAscentCount = 0

raze = 3
razeCount = 0
razeIceboxCount = 0
razeSunsetCount = 0
razeLotusCount = 0
razeBreezeCount = 0
razeBindCount = 0
razeSplitCount = 0
razeAscentCount = 0

sova = 4
sovaCount = 0
sovaIceboxCount = 0
sovaSunsetCount = 0
sovaLotusCount = 0
sovaBreezeCount = 0
sovaBindCount = 0
sovaSplitCount = 0
sovaAscentCount = 0

kj = 5
kjCount = 0
kjIceboxCount = 0
kjSunsetCount = 0
kjLotusCount = 0
kjBreezeCount = 0
kjBindCount = 0
kjSplitCount = 0
kjAscentCount = 0

jett = 6
jettCount = 0
jettIceboxCount = 0
jettSunsetCount = 0
jettLotusCount = 0
jettBreezeCount = 0
jettBindCount = 0
jettSplitCount = 0
jettAscentCount = 0

kayo = 7
kayoCount = 0
kayoIceboxCount = 0
kayoSunsetCount = 0
kayoLotusCount = 0
kayoBreezeCount = 0
kayoBindCount = 0
kayoSplitCount = 0
kayoAscentCount = 0

cypher = 8
cypherCount = 0
cypherIceboxCount = 0
cypherSunsetCount = 0
cypherLotusCount = 0
cypherBreezeCount = 0
cypherBindCount = 0
cypherSplitCount = 0
cypherAscentCount = 0

gekko = 9
gekkoCount = 0
gekkoIceboxCount = 0
gekkoSunsetCount = 0
gekkoLotusCount = 0
gekkoBreezeCount = 0
gekkoBindCount = 0
gekkoSplitCount = 0
gekkoAscentCount = 0

fade = 10
fadeCount = 0
fadeIceboxCount = 0
fadeSunsetCount = 0
fadeLotusCount = 0
fadeBreezeCount = 0
fadeBindCount = 0
fadeSplitCount = 0
fadeAscentCount = 0

skye = 11
skyeCount = 0
skyeIceboxCount = 0
skyeSunsetCount = 0
skyeLotusCount = 0
skyeBreezeCount = 0
skyeBindCount = 0
skyeSplitCount = 0
skyeAscentCount = 0

breach = 12
breachCount = 0
breachIceboxCount = 0
breachSunsetCount = 0
breachLotusCount = 0
breachBreezeCount = 0
breachBindCount = 0
breachSplitCount = 0
breachAscentCount = 0

harbor = 13
harborCount = 0
harborIceboxCount = 0
harborSunsetCount = 0
harborLotusCount = 0
harborBreezeCount = 0
harborBindCount = 0
harborSplitCount = 0
harborAscentCount = 0

brim = 14
brimCount = 0
brimIceboxCount = 0
brimSunsetCount = 0
brimLotusCount = 0
brimBreezeCount = 0
brimBindCount = 0
brimSplitCount = 0
brimAscentCount = 0

yoru = 15
yoruCount = 0
yoruIceboxCount = 0
yoruSunsetCount = 0
yoruLotusCount = 0
yoruBreezeCount = 0
yoruBindCount = 0
yoruSplitCount = 0
yoruAscentCount = 0

astra = 16
astraCount = 0
astraIceboxCount = 0
astraSunsetCount = 0
astraLotusCount = 0
astraBreezeCount = 0
astraBindCount = 0
astraSplitCount = 0
astraAscentCount = 0

sage = 17
sageCount = 0
sageIceboxCount = 0
sageSunsetCount = 0
sageLotusCount = 0
sageBreezeCount = 0
sageBindCount = 0
sageSplitCount = 0
sageAscentCount = 0

reyna = 18
reynaCount = 0
reynaIceboxCount = 0
reynaSunsetCount = 0
reynaLotusCount = 0
reynaBreezeCount = 0
reynaBindCount = 0
reynaSplitCount = 0
reynaAscentCount = 0

chamber = 19
chamberCount = 0
chamberIceboxCount = 0
chamberSunsetCount = 0
chamberLotusCount = 0
chamberBreezeCount = 0
chamberBindCount = 0
chamberSplitCount = 0
chamberAscentCount = 0

clove = 20
cloveCount = 0
cloveIceboxCount = 0
cloveSunsetCount = 0
cloveLotusCount = 0
cloveBreezeCount = 0
cloveBindCount = 0
cloveSplitCount = 0
cloveAscentCount = 0

neon = 21
neonCount = 0
neonIceboxCount = 0
neonSunsetCount = 0
neonLotusCount = 0
neonBreezeCount = 0
neonBindCount = 0
neonSplitCount = 0
neonAscentCount = 0

phoneix = 22
phoneixCount = 0
phoneixIceboxCount = 0
phoneixSunsetCount = 0
phoneixLotusCount = 0
phoneixBreezeCount = 0
phoneixBindCount = 0
phoneixSplitCount = 0
phoneixAscentCount = 0

iso = 23
isoCount = 0
isoIceboxCount = 0
isoSunsetCount = 0
isoLotusCount = 0
isoBreezeCount = 0
isoBindCount = 0
isoSplitCount = 0
isoAscentCount = 0

deadlock = 24
deadlockCount = 0
deadlockIceboxCount = 0
deadlockSunsetCount = 0
deadlockLotusCount = 0
deadlockBreezeCount = 0
deadlockBindCount = 0
deadlockSplitCount = 0
deadlockAscentCount = 0

count = 1
rotation = 0
# Find all rows with the class "pr-matrix-row"
for row in doc.find_all("tr", class_="pr-matrix-row"):
    # Skip rows that have both classes "pr-matrix-row" and "mod-dropdown 6x1001"
    if "mod-dropdown" in row.get("class", []):
        continue
# Loop through each row
    cells = row.find_all("td")[2:]  # Skip the first two cells
    for cell in cells:
        if "mod-picked" in cell.get("class", []):
            print(1, end=' ')
            if(count == viper):
                viperCount+=1
            if(count == omen):
                omenCount+=1
            if(count == raze):
                razeCount+=1
            if(count == sova):
                sovaCount+=1
            if(count == kj):
                kjCount+=1
            if(count == jett):
                jettCount+=1
            if(count == kayo):
                kayoCount+=1
            if(count == cypher):
                cypherCount+=1
            if(count == gekko):
                gekkoCount+=1
            if(count == fade):
                fadeCount+=1
            if(count == skye):
                skyeCount+=1
            if(count == breach):
                breachCount+=1
            if(count == harbor):
                harborCount+=1
            if(count == brim):
                brimCount+=1
            if(count == yoru):
                yoruCount+=1
            if(count == astra):
                astraCount+=1
            if(count == sage):
                sageCount+=1
            if(count == reyna):
                reynaCount+=1
            if(count == chamber):
                chamberCount+=1
            if(count == clove):
                cloveCount+=1
            if(count == neon):
                neonCount+=1
            if(count == phoneix):
                phoneixCount+=1
            if(count == iso):
                isoCount+=1
            if(count == deadlock):
                deadlockCount+=1
        else:
            print(0, end=' ')
        print(count)
        count+=1
        if(count == 25):
                count = 1
                rotation+=1
        if(rotation == 11 and viperCount != 0):
            viperIceboxCount = viperCount
            omenIceboxCount = omenCount
            razeIceboxCount = razeCount
            sovaIceboxCount = sovaCount
            kjIceboxCount = kjCount
            jettIceboxCount = jettCount
            kayoIceboxCount = kayoCount
            cypherIceboxCount = cypherCount
            gekkoIceboxCount = gekkoCount
            fadeIceboxCount = fadeCount
            skyeIceboxCount = skyeCount
            breachIceboxCount = breachCount
            harborIceboxCount = harborCount
            brimIceboxCount = brimCount
            yoruIceboxCount = yoruCount
            astraIceboxCount = astraCount
            sageIceboxCount = sageCount
            reynaIceboxCount = reynaCount
            chamberIceboxCount = chamberCount
            cloveIceboxCount = cloveCount
            neonIceboxCount = neonCount
            phoneixIceboxCount = phoneixCount
            isoIceboxCount = isoCount
            deadlockIceboxCount = deadlockCount
            viperCount = 0
            omenCount = 0
            razeCount = 0
            sovaCount = 0
            kjCount = 0
            jettCount = 0
            kayoCount = 0
            cypherCount = 0
            gekkoCount = 0
            fadeCount = 0
            skyeCount = 0
            breachCount = 0
            harborCount = 0
            brimCount = 0
            yoruCount = 0
            astraCount = 0
            sageCount = 0
            reynaCount = 0
            chamberCount = 0
            cloveCount = 0
            neonCount = 0
            phoneixCount = 0
            isoCount = 0
            deadlockCount = 0
    print()  # Print a newline after each row for better readability
print(rotation)
print(count)
print(viperCount)
print(omenCount)
print(razeCount)
print(sovaCount)
print(kjCount)
print(jettCount)
print(kayoCount)
print(cypherCount)
print(gekkoCount)
print(fadeCount)
print(skyeCount)
print(breachCount)
print(harborCount)
print(brimCount)
print(yoruCount)
print(astraCount)
print(sageCount)
print(reynaCount)
print(chamberCount)
print(cloveCount)
print(neonCount)
print(phoneixCount)
print(isoCount)
print(deadlockCount)
print(viperIceboxCount)
print(omenIceboxCount)
print(razeIceboxCount)
print(sovaIceboxCount)
print(kjIceboxCount)
print(jettIceboxCount)
print(kayoIceboxCount)
print(cypherIceboxCount)
print(gekkoIceboxCount)
print(fadeIceboxCount)
print(skyeIceboxCount)
print(breachIceboxCount)
print(harborIceboxCount)
print(brimIceboxCount)
print(yoruIceboxCount)
print(astraIceboxCount)
print(sageIceboxCount)
print(reynaIceboxCount)
print(chamberIceboxCount)
print(cloveIceboxCount)
print(neonIceboxCount)
print(phoneixIceboxCount)
print(isoIceboxCount)
print(deadlockIceboxCount)





# prices = doc.find_all(string = "$")
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)
# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all("p")[0]
# tag.string = "hello"
# changed in document after modification

# print(tags.find_all("b"))