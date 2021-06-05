# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damage_format(dmgs):
  dmgs_formatted = []
  for d in dmgs:
    if d == 'Damages not recorded':
      dmgs_formatted.append('Damages not recorded')
    elif d[-1] == 'M':
      dmgs_formatted.append(float(d[:-1])*1000000)
    elif d[-1] == 'B':
      dmgs_formatted.append(float(d[:-1])*1000000000)
  return dmgs_formatted

# test function by updating damages
damages_format = damage_format(damages)

# write your construct hurricane dictionary function here:
def table_create(names,months,years,max_sustained_winds,areas_affected,damages,deaths):
    i = 0
    table = {}
    while i < 34:
        table[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}
        i+=1
    return table

hurricanes = table_create(names,months,years,max_sustained_winds,areas_affected,damages_format,deaths)
print(hurricanes)

# write your construct hurricane by year dictionary function here:
def year_table(hurricanes):
    new_table = {}
    for k,v in hurricanes.items():
        if v['Year'] not in new_table:
            new_table[v['Year']] = []
        new_table[v['Year']].append(v)
    return new_table

year_hurricanes = year_table(hurricanes)
print(year_hurricanes)

# write your count affected areas function here:
def area_count(hurricanes):
    area_dict = {}
    for v in hurricanes.values():
        for area in v['Areas Affected']:
            if area not in area_dict:
                area_dict[area] = 0
            area_dict[area] += 1
    return area_dict

area_dict = area_count(hurricanes)
print(area_dict)

# write your find most affected area function here:
def most_affected(area_dict):
    ordered_area = dict(sorted(area_dict.items(), key=lambda kv: kv[1], reverse=True))
    return list(ordered_area.keys())[0], list(ordered_area.values())[0]

area,frequency = most_affected(area_dict)
print(area,frequency)

# write your greatest number of deaths function here:
def death_count(hurricanes):
    death_dict = {}
    for v in hurricanes.values():
        death_dict[v['Name']] = v['Deaths']
    ordered_death = dict(sorted(death_dict.items(), key=lambda kv: kv[1], reverse = True))
    return list(ordered_death.keys())[0],list(ordered_death.values())[0]

hurr, death = death_count(hurricanes)
print(hurr,death)

# write your catgeorize by mortality function here:
def mortality_rate(hurricanes):
    mortality = {0:[],1:[],2:[],3:[],4:[]}
    for v in hurricanes.values():
        if v['Deaths'] == 0:
            mortality[0].append(v)
        elif v['Deaths'] <= 100:
            mortality[1].append(v)
        elif v['Deaths'] <= 500:
            mortality[2].append(v)
        elif v['Deaths'] <= 1000:
            mortality[3].append(v)
        elif v['Deaths'] <= 10000:
            mortality[4].append(v)
    return mortality

mortality = mortality_rate(hurricanes)
print(mortality)

# write your greatest damage function here:
def damage_count(hurricanes):
    damage_dict = {}
    for v in hurricanes.values():
        if v['Damage'] == 'Damages not recorded':
            continue
        damage_dict[v['Name']] = v['Damage']
    ordered_damage = dict(sorted(damage_dict.items(), key=lambda kv: kv[1], reverse = True))
    return list(ordered_damage.keys())[0],list(ordered_damage.values())[0]

hurr_d, damage = damage_count(hurricanes)
print(hurr_d,damage)

# write your catgeorize by damage function here:
def damage_rate(hurricanes):
    destruction = {0:[],1:[],2:[],3:[],4:[]}
    for v in hurricanes.values():
        if v['Damage'] == 'Damages not recorded':
            continue
        if v['Damage'] == 0:
            destruction[0].append(v)
        elif v['Damage'] <= 100000000:
            destruction[1].append(v)
        elif v['Damage'] <= 1000000000:
            destruction[2].append(v)
        elif v['Damage'] <= 10000000000:
            destruction[3].append(v)
        elif v['Damage'] <= 50000000000:
            destruction[4].append(v)
    return destruction

destruction = damage_rate(hurricanes)
print(destruction)
