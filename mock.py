"""mock requests"""
import random
import time
import requests

DELAY = 2
LATRANGE = [32.7065053, 0.0007]
LONRANGE = [-117.1614935, 0.001]
ZRANGE = [1, 3]
IDRANGE = [1, 5]

GESERVICE = "http://startupsges.bd.esri.com:6180/geoevent/rest/receiver/indoors-features-in-rest"

def get_feature():
    """get the feature to post to geoevent"""
    lat = random.normalvariate(LATRANGE[0], LATRANGE[1])
    lon = random.normalvariate(LONRANGE[0], LONRANGE[1])
    f_z = random.randint(ZRANGE[0], ZRANGE[1])
    uid = str(random.randint(IDRANGE[0], IDRANGE[1]))
    feature = {
        "attributes": {
            "deviceId": uid,
            "buildingId": 99,
            "lat": lat,
            "lon": lon,
            "z": f_z,
            "buildingX":11.2,
            "buildingY":12.3,
            "buildingZ":123.3
        },
        "geometry": {
            "x": lon,
            "y": lat,
            "z": f_z
        }
    }
    return feature

def post_feature(feature):
    """post the feature to geoevent"""
    req = requests.post(GESERVICE, json=feature)
    if req.status_code < 200 or req.status_code > 299:
        print "Error posting `{0}`".format(feature)
        print req.text
        return False
    return True


if __name__ == "__main__":
    print "Streaming"
    count = 0
    while True:
        try:
            p_f = get_feature()
            post_feature(p_f)
            print "posted: {0}".format(count)
            count += 1
            time.sleep(DELAY)
        except KeyboardInterrupt:
            break


    print "\nSo Long!"
