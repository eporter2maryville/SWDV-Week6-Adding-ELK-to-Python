#Index template with my edits for my logging 
### not functional python code ###
curl -XPUT http://localhost:9200/python-application-log -H "content-type: application/json" -d @- <<EOF
{
"mappings": {
"dynamic": false,
"properties": {
"level": { "type": "keyword" },
"test_boolean": { "type": "keyword" },
"test_list": { "type": "text" },
"test_integer": { "type": "text" },
"test_float": { "type": "text" },
"host": { "type": "keyword" },
"@timestamp": { "type": "date" },
"@message": { "type": "text" },
"message": { "type": "text" },
"firstNameLog_string": { "type": "keyword" },
"lastNameLog_string": { "type": "keyword" },
"ageLog_string": { "type": "keyword" },
}
}
}
EOF