import requests

url = 'http://127.0.0.1:5000/users/upload'

def testCsvUpload(fileLocation, code, text):
    files = {'file': open(fileLocation, 'rb')}
    res = requests.post(url, files=files)
    assert res.status_code == code
    assert res.text.strip() == text

def testSuite():
    testCsvUpload('test/story1/columnLessTest.csv', 400, '{"result":"Rejected due to: [\'e0004\', \'Rubeus Hagrid\', \'3999.999\']"}')
    testCsvUpload('test/story1/columnMoreTest.csv', 400, '{"result":"Rejected due to: [\'e0003\', \'ssnape\', \'Severus Snape\', \'4000.0\', \'1231\']"}')
    testCsvUpload('test/story1/commentTest.csv', 200, '{"result":"Upload succeeded"}')
    testCsvUpload('test/story1/emptyTest.csv', 400, '{"result":"Rejected due to: Empty file"}')
    testCsvUpload('test/story1/loginTest.csv', 400, '{"result":"Rejected due to: [\'e0002\', \'hpotter\', \'Ron Weasley\', \'19234.50\']"}')
    testCsvUpload('test/story1/salaryTest.csv', 400, '{"result":"Rejected due to: [\'e0003\', \'ssnape\', \'Severus Snape\', \'4000..0\']"}')
    testCsvUpload('test/story1/test.csv', 200, '{"result":"Upload succeeded"}')
    print('Test cases ran successfully!')

testSuite()