Lets say we have a file with following data:

unordered-data-file:
{"id":"3234", "brand": "xyz", "binary":"fdsjl2j3jrl90i0ife"}
{"id":"4332", "brand": "abc", "binary":"hshgfdgfdsl90i0fsf"}
{"id":"2542", "brand": "wtr", "binary":"gfdgf22332l90i0ife"}
{"id":"9922", "brand": "kjl", "binary":"fdsjl23gssdsfwe223"}

I want to sort this data according to id and output to a file

expected output:
{"id":"2542", "brand": "wtr", "binary":"gfdgf22332l90i0ife"}
{"id":"3234", "brand": "xyz", "binary":"fdsjl2j3jrl90i0ife"}
{"id":"4332", "brand": "abc", "binary":"hshgfdgfdsl90i0fsf"}
{"id":"9922", "brand": "kjl", "binary":"fdsjl23gssdsfwe223"}

When I try to run below function I am getting issue with single quotations
