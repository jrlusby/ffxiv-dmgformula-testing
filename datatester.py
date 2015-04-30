import numpy
files = [
        "data/hsbl1.csv",
        "data/bl2.csv",
        "data/hs2.csv",
        "data/ss2.csv",
        ]
for filename in files:
    stats = []
    data = {}
    with open(filename, "r") as fin:
        stats = fin.readline().split(",")
        stats = [float(x) for x in stats]
        print stats
        headers = fin.readline().split(",")
        data = [line.split(",") for line in fin]
        damages = []
        for point in data:
            smartdata = dict(zip(headers, point))
            if smartdata["Critical"] == "T":
                smartdata["Damage"] = int(smartdata["Damage"])/1.5
            damages.append(int(smartdata["Damage"]))
        print "median", numpy.median(damages)
        print "(min+max)/2", (max(damages)+min(damages))/2.0
        print "mean", numpy.mean(damages)
        print "expected", (stats[0]/100)*(stats[1]*0.0437052+1)*(stats[2]*0.0763653+4.4581293)*(stats[3]*0.0006116+1)*1.2






