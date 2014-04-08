import clr
import System
from sys import argv
from optparse import OptionParser

clr.AddReference("System.Core")

from System import *
from System.Net import *

clr.ImportExtensions(Linq)

parser = OptionParser()
parser.add_option("-u", "--url", type="string", dest="url", help="URL to check")
parser.add_option("-t", "--timeout", type="int", dest="timeout", help="Timeout (in milliseconds)")

(options, argv) = parser.parse_args()

if not options.url:
    Console.WriteLine("URL to check must be provided.")
    Environment.Exit(1)

try:
    request = WebRequest.Create(options.url)

    if options.timeout > 0:
        request.Timeout = options.timeout

    response = request.GetResponse()

    Console.WriteLine("Status Code: {0}", response.StatusDescription)

    response.Close()
except System.UriFormatException, ex:
    Console.WriteLine(ex.Message)
    Environment.Exit(1)

except System.Net.WebException, ex:
    Console.WriteLine(ex.Message)
    Environment.Exit(1)

Environment.Exit(0);
