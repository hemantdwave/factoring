#    Copyright 2020 D-Wave Systems Inc.

#    Licensed under the Apache License, Version 2.0 (the "License")
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http: // www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from subprocess import Popen, PIPE,STDOUT
import unittest
import time
import os

class IntegrationTests(unittest.TestCase):

    def test_factoring(self):
        cwd=os.getcwd()
        p = Popen(["python",  cwd+"/demo.py"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
        p.stdin.write(b'49\n')
        time.sleep(5)
        output = p.communicate()[0]
        output=str(output)
        print("Example output \n"+output)

        with self.subTest(msg="Verify if output contains 'results': [{'a': 7, \n"):
            self.assertIn("'results': [{'a': 7,".upper(),output.upper())
        with self.subTest(msg="Verify if output contains 'b': 7 \n"):
            self.assertIn("'b': 7,".upper(),output.upper())
        with self.subTest(msg="Verify if error string contains in output \n"):
            self.assertNotIn("ERROR",output.upper())
        with self.subTest(msg="Verify if warning string contains in output \n"):
            self.assertNotIn("WARNING",output.upper())

if __name__ == '__main__':
    unittest.main()