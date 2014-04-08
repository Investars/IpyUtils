from sys import argv
import optparse
import clr

clr.AddReference("System.Core")

from System import *
from System.IO import *
from System.Collections.Generic import *

clr.ImportExtensions(Linq)

directory = argv[1]
str = argv[2]
pattern = argv[3]
patterns = argv.ToArray().Skip(4)

if not Directory.Exists(directory):
    raise DirectoryNotFoundException(directory)

files = patterns.SelectMany(lambda pattern: Directory.GetFiles(directory, pattern, SearchOption.AllDirectories)).Distinct()

for file in files:
    if not File.Exists(file):
        Console.WriteLine("Not found <{0}>", file)
        continue

    Console.WriteLine("Find <{0}>", file)

    content = String.Empty

    with StreamReader(file) as reader:
        content = reader.ReadToEnd()

    if content.IndexOf(pattern) != -1:
        content = content.Replace(pattern, str)
        with StreamWriter(file, False) as writer:
            writer.Write(content)
        Console.WriteLine("Update <{0}>", file)
