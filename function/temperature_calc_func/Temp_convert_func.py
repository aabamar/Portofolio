def temp_convert(temp, init_unit, convert_unit):
  '''
  Function to convert temperature based on initial and target unit

  Parameters
  ----------
  temp : int
    temperature from initial unit
  
  init_unit : str
    initial unit ("kelvin", "celcius", and "fahreinheit")
  
  convert_unit : str
    target convert unit ("kelvin", "celcius", and "fahreinheit")

  Returns
  --------
  

  example
  --------
  input :
    temp = 20
    init_unit = 'Celcius'
    convert_unit = 'Fahrenheit'
  
  output:
    20 celcius is equal to 68 fahreinheit
  '''

  #create temperature unit & formula dictionary
  #key = init_unit
  #value = convert_unit[to_kelvin, to_celcius, to_fahreinheit]
  temp_dict = {
              "kelvin" : [temp, temp - 273, ((temp - 273) * 9/5) + 32],
              "celcius" : [temp + 273, temp, (temp * 9/5) + 32],
              "fahreinheit" : [((temp-32) * 5/9) + 273, (temp-32) * 5/9, temp] 
              }

  #convert unit to lowercase
  init_unit = init_unit.lower()
  convert_unit = convert_unit.lower()

  #check & validate unit value are kelvin, celcius & fahreinheit
  if init_unit and convert_unit not in temp_dict.keys():
    raise Exception("unit temperature not recognized") 
  else:
  #create loop for calculate temperature from initial unit with temperature unit & formula dictionary
    for unit, form in temp_dict.items():
      if init_unit == unit:
        #calculate temp to kelvin unit
        if convert_unit == "kelvin":
          convert_temp = form[0]
        #calculate temp to celcius unit
        elif convert_unit == "celcius":
          convert_temp = form[1]
        #calculate temp to fahreinheit unit
        elif convert_unit == "fahreinheit":
          convert_temp = form[2]
        #check & validate unit value are kelvin, celcius & fahreinheit
        else:
          raise Exception("unit temperature not recognized")
      #check & validate unit value are kelvin, celcius & fahreinheit
      else:
        pass
  #print putput value contain unit and temperature
  print(f'{temp} {init_unit} is equal to {int(convert_temp)} {convert_unit}')