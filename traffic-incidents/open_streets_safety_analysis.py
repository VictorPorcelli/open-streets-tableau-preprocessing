import pandas as pd
import json
from shapely.geometry import shape, Point, Polygon, MultiPolygon, MultiLineString
import geopy.distance

accidents_coded = open("accidents_coded_19-21.csv","w")
accidents_coded.write("Open Street (yes/no), Latitude, Longitude \n")

with open("Open Streets Locations.geojson") as f:
    open_streets_js = json.load(f)

with open("traffic_accidents_19-21.geojson") as d:
    accidents_js = json.load(d)

tot_city_pre = 0
tot_open_pre = 0

cycle_city_pre = 0
cycle_open_pre = 0

ped_city_pre = 0
ped_open_pre = 0

motor_city_pre = 0
motor_open_pre = 0

tot_city_post = 0
tot_open_post = 0

cycle_city_post = 0
cycle_open_post = 0

ped_city_post = 0
ped_open_post = 0

motor_city_post = 0
motor_open_post = 0

for accident_feature in accidents_js['features']:
    date = accident_feature['properties']['date_time']
    date = date[:date.index("Z")]
    date = pd.to_datetime(date, yearfirst = True)

    if date > pd.to_datetime("2019-04-27T00:00:00", yearfirst = True) and date < pd.to_datetime("2021-04-27T00:00:00", yearfirst = True):
        pre = date<pd.to_datetime("2020-04-27T00:00:00", yearfirst = True)
        
        try:
            point = Point(accident_feature['geometry']['coordinates'])
            found = False
            
            for open_street_feature in open_streets_js['features']:
                try:
                    multi_string = MultiLineString(open_street_feature['geometry']['coordinates'])
                    '''
                    line_string = multi_string.convex_hull
                    coordinates = []
                    for index, point2 in enumerate(line_string.coords):
                        if index == 0:
                            first_pt = point2
                        coordinates.append(point2)

                    coordinates.append(first_pt)
                    polygon = Polygon(coordinates)
                            
                    if polygon.intersects(point) or polygon.contains(point):
                        print("TRUE")
                        found = True
                    #equivalent of within 5 feet
                    '''
                    if multi_string.distance(point) < (0.0001) and found == False:
                        found = True
                        accidents_coded.write("yes,"+str(point.x)+","+str(point.y)+"\n")
                    
                except:
                    pass

            if found == False:
                accidents_coded.write("no,"+str(point.x)+","+str(point.y)+"\n")
                if pre:
                    ped_city_pre += int(accident_feature['properties']['number_of_pedestrian_killed'])
                    ped_city_pre += int(accident_feature['properties']['number_of_pedestrian_injured'])

                    motor_city_pre += int(accident_feature['properties']['number_of_motorist_killed'])
                    motor_city_pre += int(accident_feature['properties']['number_of_motorist_injured'])

                    cycle_city_pre += int(accident_feature['properties']['number_of_cyclist_killed'])
                    cycle_city_pre += int(accident_feature['properties']['number_of_cyclist_injured'])

                    tot_city_pre += int(accident_feature['properties']['number_of_persons_killed'])
                    tot_city_pre += int(accident_feature['properties']['number_of_persons_injured'])
                else:
                    ped_city_post += int(accident_feature['properties']['number_of_pedestrian_killed'])
                    ped_city_post += int(accident_feature['properties']['number_of_pedestrian_injured'])

                    motor_city_post += int(accident_feature['properties']['number_of_motorist_killed'])
                    motor_city_post += int(accident_feature['properties']['number_of_motorist_injured'])

                    cycle_city_post += int(accident_feature['properties']['number_of_cyclist_killed'])
                    cycle_city_post += int(accident_feature['properties']['number_of_cyclist_injured'])

                    tot_city_post += int(accident_feature['properties']['number_of_persons_killed'])
                    tot_city_post += int(accident_feature['properties']['number_of_persons_injured'])
            else:
                if pre:
                    ped_open_pre += int(accident_feature['properties']['number_of_pedestrian_killed'])
                    ped_open_pre += int(accident_feature['properties']['number_of_pedestrian_injured'])

                    motor_open_pre += int(accident_feature['properties']['number_of_motorist_killed'])
                    motor_open_pre += int(accident_feature['properties']['number_of_motorist_injured'])

                    cycle_open_pre += int(accident_feature['properties']['number_of_cyclist_killed'])
                    cycle_open_pre += int(accident_feature['properties']['number_of_cyclist_injured'])

                    tot_open_pre += int(accident_feature['properties']['number_of_persons_killed'])
                    tot_open_pre += int(accident_feature['properties']['number_of_persons_injured'])
                else:
                    ped_open_post += int(accident_feature['properties']['number_of_pedestrian_killed'])
                    ped_open_post += int(accident_feature['properties']['number_of_pedestrian_injured'])

                    motor_open_post += int(accident_feature['properties']['number_of_motorist_killed'])
                    motor_open_post += int(accident_feature['properties']['number_of_motorist_injured'])

                    cycle_open_post += int(accident_feature['properties']['number_of_cyclist_killed'])
                    cycle_open_post += int(accident_feature['properties']['number_of_cyclist_injured'])

                    tot_open_post += int(accident_feature['properties']['number_of_persons_killed'])
                    tot_open_post += int(accident_feature['properties']['number_of_persons_injured'])
            
        except:
            try:
                if pre:
                    ped_city_pre += int(accident_feature['properties']['number_of_pedestrian_killed'])
                    ped_city_pre += int(accident_feature['properties']['number_of_pedestrian_injured'])

                    motor_city_pre += int(accident_feature['properties']['number_of_motorist_killed'])
                    motor_city_pre += int(accident_feature['properties']['number_of_motorist_injured'])

                    cycle_city_pre += int(accident_feature['properties']['number_of_cyclist_killed'])
                    cycle_city_pre += int(accident_feature['properties']['number_of_cyclist_injured'])

                    tot_city_pre += int(accident_feature['properties']['number_of_persons_killed'])
                    tot_city_pre += int(accident_feature['properties']['number_of_persons_injured'])
                else:
                    ped_city_post += int(accident_feature['properties']['number_of_pedestrian_killed'])
                    ped_city_post += int(accident_feature['properties']['number_of_pedestrian_injured'])

                    motor_city_post += int(accident_feature['properties']['number_of_motorist_killed'])
                    motor_city_post += int(accident_feature['properties']['number_of_motorist_injured'])

                    cycle_city_post += int(accident_feature['properties']['number_of_cyclist_killed'])
                    cycle_city_post += int(accident_feature['properties']['number_of_cyclist_injured'])

                    tot_city_post += int(accident_feature['properties']['number_of_persons_killed'])
                    tot_city_post += int(accident_feature['properties']['number_of_persons_injured'])
            except:
                pass

tot_city_post += tot_open_post
cycle_city_post += cycle_open_post
motor_city_post += motor_open_post
ped_city_post += ped_open_post

tot_city_pre += tot_open_pre
cycle_city_pre += cycle_open_pre
motor_city_pre += motor_open_pre
ped_city_pre += ped_open_pre

pct_change_cycle_open = (cycle_open_post - cycle_open_pre)/cycle_open_pre
pct_change_cycle_city = (cycle_city_post - cycle_city_pre)/cycle_city_pre

pct_change_ped_open = (ped_open_post - ped_open_pre)/ped_open_pre
pct_change_ped_city = (ped_city_post - ped_city_pre)/ped_city_pre


pct_change_motor_open = (motor_open_post - motor_open_pre)/motor_open_pre
pct_change_motor_city = (motor_city_post - motor_city_pre)/motor_city_pre

pct_change_tot_open = (tot_open_post - tot_open_pre)/tot_open_pre
pct_change_tot_city = (tot_city_post - tot_city_pre)/tot_city_pre

outfile = open("open_streets_safety_analysis.csv","w")

outfile.write(", 12-months Pre, 12-months Post, Percent Change \n")
outfile.write("Biking-Open,"+str(cycle_open_pre)+","+str(cycle_open_post)+","+str(pct_change_cycle_open)+"\n")
outfile.write("Biking-City,"+str(cycle_city_pre)+","+str(cycle_city_post)+","+str(pct_change_cycle_city)+"\n")
outfile.write("Pedestrians-Open,"+str(ped_open_pre)+","+str(ped_open_post)+","+str(pct_change_ped_open)+"\n")
outfile.write("Pedestrians-City,"+str(ped_city_pre)+","+str(ped_city_post)+","+str(pct_change_ped_city)+"\n")
outfile.write("Motorists-Open,"+str(motor_open_pre)+","+str(motor_open_post)+","+str(pct_change_motor_open)+"\n")
outfile.write("Motorists-City,"+str(motor_city_pre)+","+str(motor_city_post)+","+str(pct_change_motor_city)+"\n")
outfile.write("Total-Open,"+str(tot_open_pre)+","+str(tot_open_post)+","+str(pct_change_tot_open)+"\n")
outfile.write("Total-City,"+str(tot_city_pre)+","+str(tot_city_post)+","+str(pct_change_tot_city)+"\n")

outfile.close()
accidents_coded.close()


