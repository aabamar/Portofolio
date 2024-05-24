import pandas as pd

def nik_extract(nik):
  '''
  Function to extract information from NIK

  Parameters
  ----------
  nik : int
    Nomor induk kependudukan
  
  Returns
  --------
  nik_extract : dict
    dict contain information based on given NIK
  example
  --------
  input :
    nik = 1571011709860003
  
  output:
    {'province': 'JAMBI',
    'city/district': 'KOTA JAMBI',
    'sub-district': 'Telanaipura',
    'gender': 'male',
    'date-of-birth': '17-09-86'}
  '''

  #convert nik into string type
  nik = str(nik)

  #area code extraction from first six digit for NIK identification
  #import ID area code based on Permendagri No. 72/2019
  area_code = pd.read_csv("base.csv", names=['code', 'area'])
  #remove '.' from area code
  area_code['code'] = area_code['code'].str.replace('.', '')
  area_code.set_index('code', inplace=True)

  #split area code into smaller group (province, city/district, and subdistrict)
  #and convert into dictionary
  province_code = area_code[area_code.index.str.len() == 2]
  city_code = area_code[area_code.index.str.len() == 4]
  subdistrict_code = area_code[area_code.index.str.len() == 6]
  
  #define area from nik number
  nik_province = province_code['area'].loc[nik[0:2]]
  nik_city = city_code['area'].loc[nik[0:4]]
  nik_subdistrict = subdistrict_code['area'].loc[nik[0:6]]

  #gender and birth of date extraction from second six digit for NIK identification
  #extract gender and birth of date
  if (int(nik[6:8]) - 40) <= 0:
    nik_gender = "male"
    nik_dob = nik[6:8] + '-' + nik[8:10] + '-' + nik[10:12]
    
  else:
    nik_gender = "female"
    nik_date = int(nik[6:8]) - 40
    nik_dob = str(nik_date) + '-' + nik[8:10] + '-' + nik[10:12]
  
  #collect information base on given NIK
  nik_extract = {"province" : nik_province,
                 "city/district" : nik_city,
                 "sub-district" : nik_subdistrict,
                 "gender" : nik_gender,
                 "date-of-birth" : nik_dob}
  
  #return output value
  return nik_extract    