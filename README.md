# json2yaml

Command line utilities to convert between JSON and YAML while
preserving the order of associative arrays.

Preserving the mapping order is helpful to humans reading the
documents, despite not affecting their meaning.

## Install

```pip install json2yaml```

## Usage
```json2yaml input.json output.yaml```

```yaml2json input.yaml output.json```

```
$ json2yaml --help
Usage:
    json2yaml (--version|--help)
    json2yaml [<json_file>] [<yaml_file>]

Arguments:
    <json_file>    The input file containing the JSON to convert. If not
                   specified, reads from stdin.
    <yaml_file>    The output file to which to write the converted YAML. If
                   not specified, writes to stdout.
```

```
$ yaml2json --help
Usage:
    yaml2json (--version|--help)
    yaml2json [-i <indent>] [<yaml_file>] [<json_file>]

Arguments:
    -i, --indent=INDENT  Number of spaces to indent [default: 4]
    <yaml_file>          The input file containing the YAML to convert. If not
                         specified, reads from stdin.
    <json_file>          The output file to which to write the converted JSON.
                         If not specified, writes to stdout.
```

## Changelog

+  1.2.0 (October 19, 2021)
   +  support multiple yaml documents in one file
   +  learn to wrap multiple yaml documents in a JSON array (-a | --array)
   +  use yaml safe_load to prevent loading of arbitrary Python objects
+  1.1.1 (March 16, 2015)
   +  terminate json output with newline
+  1.1.0 (March 16, 2015)
   +  take indent as command line argument (-i | --indent)
   +  prevent trailing spaces in json output

## Authors
**David Bild**

+ [https://www.davidbild.org](https://www.davidbild.org)
+ [https://github.com/drbild](https://github.com/drbild)

## License
Copyright 2015 David R. Bild

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this work except in compliance with the License. You may obtain a copy of the
License from the LICENSE.txt file or at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
