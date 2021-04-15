
/*
{
    "jobs": {
        "demo-pipeline": {
            "regexpFilterExpression": "opsk8s",
            "triggered": true,
            "resolvedVariables": {
                "header_id": "001",
                "header_name": "jenkins",
                "user_name": "lsunstack",
            },
            "regexpFilterText": "opsk8s",
            "id": 840,
            "url": "queue/item/840/"
        }
    },
    "message": "Triggered jobs."
}
*/

/*
curl --location --request POST 'http://172.16.100.99:8080/generic-webhook-trigger/invoke?token=demo-pipeline&user_name=opsk8s' \
--header 'header_name: jenkins' \
--header 'header_id: 001' \
--header 'Content-Type: application/json' \
--data-raw '{
    "jobs": {
        "demo-pipeline": {
            "regexpFilterExpression": "opsk8s",
            "triggered": true,
            "resolvedVariables": {
                "header_id": "001",
                "header_name": "jenkins",
                "user_name": "lsunstack",
            },
            "regexpFilterText": "opsk8s",
            "id": 840,
            "url": "queue/item/840/"
        }
    },
    "message": "Triggered jobs."
}'
*/
println("Get Post Souce All Data=${data}")

def data = readJSON file: '', text: "${data}"

println("data=${data}")

//data=[jobs:[demo-pipeline:[regexpFilterExpression:opsk8s, triggered:true, resolvedVariables:[header_id:001, header_name:jenkins, user_name:lsunstack], regexpFilterText:opsk8s, id:840, url:queue/item/840/]], message:Triggered jobs.]

// Get user_name
data_user_name = data["jobs"]["demo-pipeline"]["resolvedVariables"]["user_name"]

println(data_user_name)

