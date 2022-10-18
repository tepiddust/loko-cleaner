cleaner_doc = '''
### Description
CLEANER is the Loko AI component which allows to clean input data by removing duplicates from a JSON objects list or by replacing None or empty values with a specified non-empty value
### Configuration
The switch ***Output as a list*** allows user to output cleaned data inside a single list, instead of iterating through each output value.
Users can decide whether clean duplicates or replace None/empty values or both with the corresponding switches.
If ***Remove Duplicates*** is switched on and input data is a JSON objects list, users can specify a discriminating key to decide wheter there is a duplicate or not, users can also ignore "missing key" errors by toggling the ***Ignore error*** switch.
If ***Replace None or empty values*** is switched on, users can specify a custom value. This value is used to fill None or empty values of the input data.

### Input
A list of JSON objects or a list of heterogeneous and non-heterogeneous values

### Output
Same as input but without duplicates or with None/empty values filled with the custom value 
'''