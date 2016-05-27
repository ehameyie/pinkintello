import pandas as pd
import numpy as np
import math
#from math import radians, cos, sin, asin, sqrt

__author__ = 'eunice hameyie'
__version__ = '1.0'
__date__ = '26 May 2016'

'''This algorithm is to recommend the best restaurant based on public rating and location
    Inspired by a data challenge I took with Elsevier
    I define each function separately so that the bestRestaurantFinder functions can be called
    outside of this application :)
    '''

### Step 1:  Read the file input as a csv.
#Filename location; could also import form a separate database...to add later

filename = ''
filename_output = ''

def csv_reader(filename):
    csv_file = pd.read_csv(filename)
    return csv_file

#If not using pandas, then the CSV reader is defined as:

#def csv_reader(filename):
    #where filename is filepath between ''
#    with open(filename, 'rU') as csvfile:
#        #csv_data = csv.DictReader(csvfile)
#        csv_data = csv.reader(csvfile, delimiter=',', quotechar='|')
#        csv_file=[]
#        headers = csv_data.next()
#        for row in csv_data:
#            csv_file.append(dict(zip(headers, row)))
            #csvfile.close()
#    return csv_file


### Step 2: Filter data based on zip code and city entered by user;
    #Filter must return the filtered dataset
    #Test zipcode 94104 and owner_city San Francisco

def zipFinder(csv_file,zipcode,owner_city):
    filtered_owner = csv_file[(csv_file.owner_city == owner_city) & (csv_file.owner_zip == zipcode )]
    return filtered_owner
#TEST: filtered_owner = zipFinder(csv_file,zipcode = '94104',owner_city='San Francisco')


### Step 3: Implement a second filter to compute the distance between the user's location and all restaurant within that area;
    # inputs to function are user's latitude and longitude;
    # the output is a filtered dataset of restaurants within 500 meters of user's location
    # I used the haversine formula; possibility to use other formuala such as distance on unit sphere function to calculate distance
    # Test with lat='36.1'and long='-120.40'

def distanceMapper(source_lat,source_long,filtered_owner):
    #eunice says: A quick google search suggests the haversine formula is most used for GPS comparisons
    #Used formula in wikipedia: https://en.wikipedia.org/wiki/Haversine_formula
    degrees_to_radians = math.pi/180.0
    lat_1 = degrees_to_radians * filtered_owner.latitude
    long_1 = degrees_to_radians * filtered_owner.longitude
    lat_2 = degrees_to_radians * source_lat
    long_2 = degrees_to_radians * source_long
    dlong = long_1 - long_2
    dlat = lat_1 - lat_2
    a = np.sin(dlat/2)**2
    b = np.sin(dlong/2)**2
    r_earth = 6371 #units are km....can be converted to 3959 in miles
    inside = a + np.cos(lat_2) * np.cos(lat_1) * b
    #inside = sin(dlat/2)**2 + cos(source_lat) * cos(dict_lat) * sin(dlon/2)**2
    haversine = 2 * r_earth * np.arcsin(np.sqrt(inside))
    c = haversine[haversine <=0.5]
    index_list = c.index.values
    #filtered_owner = zipFinder(csv_file,zipcode,owner_city)
    radius_lt_5 = filtered_owner.ix[index_list]
    #df[df.index.map(lambda x: x[0] in stk_list)]
    return radius_lt_5

#TEST: source_lat='36.1',source_long='-120.40'


### Step 4: Implement another filter to open and clean the public inspection
    #record of empty entries.
    # input argument is inspection file and output is filtered list of inspection ratings.

def inspectionCleaner(inspections_file):
    inspections_read = pd.read_csv(inspections_file)
    inspection_drop = inspections_read.dropna(subset=['Score'])
    inspections_cleaned = inspection_drop.sort(['business_id', 'date'], ascending=[1, 1])
    return inspections_cleaned


### Step 6: Implement the best Restaurant finder function to return
    #the best restaurant name based on the score. This function
    #takes two arguments :
    #Argument 1 - cleaned inspections list
    #Argument 2 - List of restaurants in 500 metres radius
    #Return best restaurant name

def recommender_bestresto(inspections_cleaned,radius_lt_5):
    best_restau = radius_lt_5[radius_lt_5['business_id'].isin(inspections_cleaned.business_id)]
    best_restaurant = best_restau.name
    return best_restaurant

### Step 7: This is a helper function that joins two tables
   # Use this function to perform joins on inspections
   # and business lists

def join(list1,list2,key1=None,key2=None):
    key1 = key1 or (lambda x:int(x[0]))
    key2 = key2 or (lambda x:int(x[0]))
    d0 = {};d1 = {}
    for x in list1:
        if key1(x) not in d0:
            d0[key1(x)] = x
    for y in list2:
        if key2(x) not in d1:
            d1[key2(y)] = y
    return [(k, d0[k], d1[k]) for k in d0 if k in d1]

### Step 8: Implement the main method to print the
    #recommender_bestresto program and outputs a csv with list of recommended restaurants

def main():
    filename = 'inputs/businesses_plus.csv'
    filename_output = 'outputs/recommended_bestresto.csv'
    inspections_file = 'inputs/inspections_plus.csv'
    zipcode = '94104'
    owner_city = 'San Francisco'
    source_lat = 37.791116
    source_long = -122.403816

    csv_file = csv_reader(filename)
    filtered_owner = zipFinder(csv_file,zipcode,owner_city)
    radius_lt_5 = distanceMapper(source_lat,source_long,filtered_owner)
    inspections_cleaned = inspectionCleaner(inspections_file)

    postal_group=csv_file.groupby('postal_code').count()
    postal_group.business_id.plot(kind='bar')
    max_count_restau = postal_group.business_id.max()
    MaxRestaurantsPostalCode = postal_group[postal_group.business_id==max_count_restau]
    #MaxRestaurantsPostalCode.to_csv('output/MaxRestaurantsPostalCode.csv')

    eunicerecommends = recommender_bestresto(inspections_cleaned,radius_lt_5)
    eunicerecommends.to_csv(filename_output)
    #print eunicerecommends

### Step 9: Visualization -- will try some fancy amtplotlib to map restaurant as scatter plot
    #but I want the selected one to be in red


### Step 10: Run SQL queries assuming MySQL:

# Top 20 businesses by zipcode
# select distinct businesses.business_id, businesses.business_name, inspections.score
#from businesses
#join inspections
#on businesses.business_id = inspections.business_id
#where businesses.postal_code = top_postal_code
#order by inspections.date DESC, inspections.score DESC
#limit 20;

# Overal top 10
# select distinct businesses.business_id, businesses.business_name, inspections.score
#from businesses
#join inspections
#on businesses.business_id = inspections.business_id
#where businesses.postal_code = top_postal_code
#order by inspections.date DESC, inspections.score DESC
#limit 10;


if __name__ == "__main__":
    main()
