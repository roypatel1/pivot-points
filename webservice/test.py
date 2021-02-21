for entry in retracementLowToHigh:
    if entry['0.236'] > pricebetween2 and entry['0.236'] < pricebetween:
        clusternew.append(str(entry['0.236']) + ' : value')
    if entry['0.382'] > pricebetween2 and entry['0.382'] < pricebetween:
        clusternew.append(str(entry['0.382']) + ' : value')
    if entry['0.5'] > pricebetween2 and entry['0.5'] < pricebetween:
        clusternew.append(str(entry['0.5']) + ' : value')
    if entry['0.618'] > pricebetween2 and entry['0.618'] < pricebetween:
        clusternew.append(str(entry['0.618']) + ' : value')
    if entry['0.786'] > pricebetween2 and entry['0.786'] < pricebetween:
        clusternew.append(str(entry['0.786']) + ' : value')
    if entry['1.272'] > pricebetween2 and entry['1.272'] < pricebetween:
        clusternew.append(str(entry['1.272']) + ' : value')
    if pricebetween2 < entry['1.618'] < pricebetween:
        clusternew.append(str(entry['1.618']) + ' : value')
    if pricebetween2 < entry['2.0'] < pricebetween:
        clusternew.append(str(entry['2.0']) + ' : value')
    if pricebetween2 < entry['2.618'] < pricebetween:
        clusternew.append(str(entry['2.618']) + ' : value')

