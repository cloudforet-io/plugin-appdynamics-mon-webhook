# plugin-cisco-appdynamics-mon-webhook
webhook for Cisco AppDynamics

![Architecture](docs/en/appdynamics-webhook-architecture.png)
# Data Model

## AppDynamics to Cloudforet


Webhook notification: 

~~~
Sample Data
~~~

| Field 	| Example |
| ---   	| ---     |
| title		| Dastabase Size alert |
| message       | Database xxxxxx      |
| ...  	| ... , ... , ...    |

## Event key criteria
Hash key of ```raw_data.incident.incident_id```.


## SpaceONE Event Model
| Field		| Type | Description	| Example	|
| ---      | ---     | ---           | ---           |
| event_id | str  | auto generation | event-1234556  |
| event_key | str | raw_data.incident.incident_id | 1234 |
| event_type |  str  | RECOVERY , ALERT based on raw_data.incident.state | RECOVERY	|
| title | str	| raw_data.incident.summary	| Test Incident	|
| description | str | raw_data.incident.summary	| Test Incident		|
| severity | str  | ... | ALERT	|
| resource | dict | ...		| N/A	|
| raw_data | dict | ...  | {"title": "Database Size Alert", "dashboardId": 1, ... } |
| addtional_info | dict | ... 	| {"org_id": "1.0", "rule_url" "https://...." } |
| occured_at | datetime | webhook received time | "2021-08-23T06:47:32.753Z" |
| alert_id | str | mapped alert_id	| alert-3243434343 |
| webhook_id | str  | webhook_id	| webhook-34324234234234 |
| project_id | str	| project_id	| project-12312323232    |
| domain_id | str	| domain_id	| domain-12121212121	|
| created_at | datetime | created time | "2021-08-23T06:47:32.753Z"	|

## cURL Requests examples
This topic provides examples of calls to the Cloudforet monitoring webhook using cURL.

Here's a cURL command that works for getting the response from webhook, you can test the following on your local machine.
```
curl -X POST https://your_spaceone_monitoring_webhook_url -d '{
  "dashboardId": xx,
  "evalMatches": [
    {
      "value": xxx,
      "metric": "xxx",
      "tags": {}
    }
  ],
  "ruleUrl": "xxx",
  "imageUrl": "xxx",
  "message": "xxx",
  "orgId": xx,
  "panelId": xx,
  "ruleId": xx,
  "ruleName": "xxx",
  "ruleUrl": "xxx",
  "state": "xxx",
  "tags": {
    "xxx": "xxx"
  },
  "title": "xxx"
}
```

# Reference

https://docs.appdynamics.com/appd/4.5.x/en/appdynamics-essentials/alert-and-respond/actions/http-request-actions-and-templates
