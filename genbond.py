

coupon = 0
matstart = 20
matcap = 25
cpn_incrmt = 25
pymnt_months = ['MAR','JUN','SEP','DEC']
ccy_list = ['EUR','GBP','USD']
ccy_count = 0
ccy = ccy_list[ccy_count]
otp_list = list(range(1))
cusip = None

count = 0
matcount = 0

print ('Generic Bond ID Creation Utility')
input('Please press ENTER to continue...')

# pymnt_months = str(input('Please enter a list of months: '))
pymnt = len(pymnt_months)-1
currmonth = pymnt_months[pymnt]



print (pymnt + 1)
# import subprocess
# with open('/home/hatatatch/Documents/Projects/genbond.txt','w+') as output:
#    subprocess.call(["python3", "./genbond.py"], stdout=output);

while (ccy_count < 3):
    ccy = ccy_list[ccy_count]
    while (pymnt < 4):

        while (matstart <= matcap):

            while (coupon <= 1500):
                cusip = '{0:04}'.format(coupon) + currmonth + str(matstart) + ccy
                otp_list.append(cusip)
                coupon = coupon + cpn_incrmt
                count = count + 1

            matstart = matstart + 1
            coupon = 0000

        currmonth = pymnt_months[pymnt]
        matstart = 20
        pymnt = pymnt + 1

    pymnt = 0
    ccy_count = ccy_count + 1

print ('Your List is: ', otp_list)
print ('Your insrument count is:', str(count))
# print ('Your maturity count is:', str(matcount))
