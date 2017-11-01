# CS-171-A Prof Mark Boady
# Homework 3
# Cameron Kelliher
# 10/29/17

import sys, math

def compute(x):
  return (x * m) + b

print('Welcome to the Linear Regression Generator')
filename = input('Enter File Name Containing Data: ')

# Read File
try:
    file = open(filename, 'r')
    file_content = file.read()
except:
    print('Error: File could not be opened.')
    sys.exit(1)

# Parse File Content
try:
    values = file_content.split('\n')
    x_label = values[0].split(',')[0]
    y_label = values[0].split(',')[1]
    values = values[1 : len(values) - 1]

    for i in range(0, len(values)):
        values[i] = values[i].split(',')
        values[i][0] = float(values[i][0])
        values[i][1] = float(values[i][1])
except:
    print('Error: A value in the file could not be read.')
    sys.exit(1)

# Compute X and Y Averages
x_avg = 0
y_avg = 0
for val in values:
    x_avg += val[0]
    y_avg += val[1]
x_avg /= len(values)
y_avg /= len(values)

# Compute `m`
m_numerator = 0
m_denominator = 0
for val in values:
    m_numerator += (val[0] - x_avg) * (val[1] - y_avg)
    m_denominator += math.pow((val[0] - x_avg), 2)
m = m_numerator / m_denominator

# Compute `b`
b = y_avg - (m * x_avg)

print('The Linear Regression Line is y=%f*x%s' % (m, '+' + str(b) if b > 0 else str(b)))

# Compute Errors
avg_error = 0
mse = 0
for val in values:
    mse += math.pow((val[1] - compute(val[0])), 2)
    avg_error += math.fabs(val[1] - compute(val[0]))
avg_error /= len(values)
mse *= 1 / (len(values) - 2)
standard_error = math.sqrt(mse)

print('Average Error for Known Values was +/-%f' % avg_error)
print('Regression Standard Error for Known Values was %f' % standard_error)

# Prediction Loop
print('System ready to make predictions.\nTo quit, type \'exit\' as the %s.' % x_label)
while True:
    prediction_x = input('Enter %s: ' % x_label)
    if prediction_x == 'exit':
        break
    try:
        prediction_x = float(prediction_x)
        print('Prediction when %s = %f is %s = %f' % (x_label, prediction_x, y_label, compute(prediction_x)))
    except:
        print('Input could not be understood. Please try again.')
