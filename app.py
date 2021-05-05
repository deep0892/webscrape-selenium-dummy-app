import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome()
# driver.get("https://www.paisabazaar.com/axis-bank/business-loan/")

arr = ["https://www.paisabazaar.com/allahabad-bank/business-loan/",
"https://www.paisabazaar.com/amex-bank/business-loan/", "https://www.paisabazaar.com/andhra-bank/business-loan/",
"https://www.paisabazaar.com/axis-bank/business-loan/", "https://www.paisabazaar.com/bandhan-bank/business-loan/",
"https://www.paisabazaar.com/bank-of-barodabusiness-loan/", "https://www.paisabazaar.com/bank-of-indiabusiness-loan/",
"https://www.paisabazaar.com/bank-of-maharashtrabusiness-loan/", "https://www.paisabazaar.com/canara-bankbusiness-loan/",
"https://www.paisabazaar.com/central-bank-of-indiabusiness-loan/", "https://www.paisabazaar.com/citibank/business-loan/",
"https://www.paisabazaar.com/city-union-bank/business-loan/", "https://www.paisabazaar.com/corporation-bank/business-loan/",
"https://www.paisabazaar.com/dcb-bank/business-loan/", "https://www.paisabazaar.com/dena-bank/business-loan/",
"https://www.paisabazaar.com/deutsche-bank/business-loan/", "https://www.paisabazaar.com/dhanlaxmi-bank/business-loan/",
"https://www.paisabazaar.com/dbs-bank/business-loan/", "https://www.paisabazaar.com/federal-bank/business-loan/",
"https://www.paisabazaar.com/hdfc-bank/business-loan/", "https://www.paisabazaar.com/hsbc-bank/business-loan/",
"https://www.paisabazaar.com/icici-bank/business-loan/", "https://www.paisabazaar.com/idbi-bank/business-loan/",
"https://www.paisabazaar.com/idfc-bank/business-loan/", "https://www.paisabazaar.com/indian-bank/business-loan/",
"https://www.paisabazaar.com/indian-overseas-bank/business-loan/", "https://www.paisabazaar.com/indusind-bank/business-loan/",
"https://www.paisabazaar.com/jammu-kashmir-bank/business-loan/", "https://www.paisabazaar.com/karnataka-bank/business-loan/",
"https://www.paisabazaar.com/karur-vysya-bank/business-loan/", "https://www.paisabazaar.com/kotak-mahindra-bank/business-loan/",
"https://www.paisabazaar.com/lakshmi-vilas-bank/business-loan/", "https://www.paisabazaar.com/nainital-bank/business-loan/",
"https://www.paisabazaar.com/oriental-bank-of-commerce/business-loan/","https://www.paisabazaar.com/punjab-and-sind-bank/business-loan/",
"https://www.paisabazaar.com/punjab-national-bank/business-loan/","https://www.paisabazaar.com/rbl-bank/business-loan/",
"https://www.paisabazaar.com/south-indian-bank/business-loan/", "https://www.paisabazaar.com/standard-chartered-bank/business-loan/",
"https://www.paisabazaar.com/sbi-bank/business-loan/", "https://www.paisabazaar.com/syndicate-bank/business-loan/",
"https://www.paisabazaar.com/tamilnad-mercantile-bank/business-loan/", "https://www.paisabazaar.com/uco-bank/business-loan/",
"https://www.paisabazaar.com/union-bank-of-india/business-loan/", "https://www.paisabazaar.com/united-bank-of-india/business-loan/",
"https://www.paisabazaar.com/vijaya-bank/business-loan/", "https://www.paisabazaar.com/yes-bank/business-loan/"]

err = []
for element in arr:
  print(element)
  driver.get(element)
  elem = driver.find_elements_by_class_name("overflow__hide--Xscroll")
  # print(len(elem))
  if not len(elem):
    elem = driver.find_elements_by_class_name("wpb_text_column")
  # print(elem)
  df = pd.DataFrame()
  x = element.split('/')
  bankname = x[len(x) - 3]
  print(bankname)
  writer = pd.ExcelWriter(bankname + '.xlsx', engine='xlsxwriter')
  for index, el in enumerate(elem):
    try : 
      # print('index', index)
      table = el.find_element_by_tag_name('table')
      if table:
        print('inside table found')
        outerHTML = table.get_attribute('outerHTML')
        df1 = pd.DataFrame(pd.read_html(outerHTML)[0])
        # print(df1)
        df1.to_excel(writer, sheet_name=str(index))
        writer.save()
    except:
      print('something went wrong')
driver.close()


# elem = driver.find_elements_by_class_name("overflow__hide--Xscroll")
# df = pd.DataFrame()
# writer = pd.ExcelWriter(r'axis-bank.xlsx', engine='xlsxwriter')
# for index,el in enumerate(elem):
#   print('index', index)
#   table = el.find_element_by_tag_name('table').get_attribute('outerHTML')
#   df1 = pd.DataFrame(pd.read_html(table)[0])
#   df1.to_excel(writer, sheet_name=str(index))
# writer.save()
# driver.close()