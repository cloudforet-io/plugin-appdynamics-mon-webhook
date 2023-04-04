# plugin-appdynamics-mon-webhook
webhook from Cisco AppDynamics

![Architecture](docs/en/appdynamics-webhook-architecture.png)

# Data Model

https://docs.appdynamics.com/appd/23.x/latest/en/appdynamics-essentials/alert-and-respond/actions/http-request-actions-and-templates

## HTTP Request Template (Payload)

~~~
{
"event_name": "${latestEvent.displayName}",
"event_guid": "${latestEvent.guid}",
"event_id": "${latestEvent.id}",
"policy": "${policy.name}",
"event_time": "${latestEvent.eventTime}",
"app_id": "${latestEvent.application.id}",
"app_name": "${latestEvent.application.name}",
"event_message": "${latestEvent.eventMessage}",
"severity": "${latestEvent.severity}",
"event_deep_link": "${latestEvent.deepLink}",
"controller_url": "${controllerUrl}",
"node_id": "${latestEvent.node.id}",
"node_name": "${latestEvent.node.name}",
"summary": "${latestEvent.summaryMessage}",
"event_type": "${latestEvent.eventType}",
"tier_id": "${latestEvent.tier.id}",
"tier_name": "${latestEvent.tier.name}"
#if(${latestEvent.healthRuleEvent} == true)
,"health_rule_id": "${latestEvent.healthRule.id}",
"health_rule_name": "${latestEvent.healthRule.name}",
"incident_id": "${latestEvent.incident.id}",
"incident_name": "${latestEvent.incident.name}"
#end
}
~~~

## AppDynamics to Cloudforet

Free Trial of AppDynamics
https://www.appdynamics.com/free-trial/


Webhook notification:

~~~
{
    "event_name": "New Critical Health Rule Violation",
    "event_guid": "a35260de-34ff-476f-bcb9-c44fd1afd913",
    "event_id": "33021165",
    "policy": "JAVA alert",
    "event_time": "Mon Apr 03 02:04:55 UTC 2023",
    "app_id": "108979",
    "app_name": "MyApp",
    "event_message": "AppDynamics has detected a problexm .....",
    "severity": "ERROR",
    "event_deep_link": "https://painted20230307xxxx.saas.appdynamics.com/#location=APP_EVENT_Vxxxx",
    "controller_url": "https://painted20230307xxxxx.saas.appdynamics.com",
    "node_id": "${latestEvent.node.id}",
    "node_name": "${latestEvent.node.name}",
    "summary": "AppDynamics has detected a problem with Business xxxxxx.",
    "event_type": "POLICY_OPEN_CRITICAL",
    "tier_id": "201066",
    "tier_name": "MyTier",
    "health_rule_id": "615178",
    "health_rule_name": "Business Transaction Health",
    "incident_id": "70646",
    "incident_name": "Business Transaction Health"
    }
~~~

| Field 	| Description |
| ---   	| ---     |
| account_name		| AppDynamics Account name |
| events       | List of Alert events      |
| ...  	| ... , ... , ...    |

## Event key criteria

* incident_id, if exist
* event_id, if incident_id does not exist

## monitoring.Event Data Map
| Field		| Type | Description	| Example	|
| ---      | ---     | ---           | ---           |
| event_key | str | incdent_id or event_id | ? |
| event_type |  str  | RECOVERY , ALERT based on raw_data.incident.state | RECOVERY	|
| title | str	| event_name	| New Critical Health Rule Violation	|
| description | str | event_message	| AppDynamics has detected ...		|
| severity | str  | severity | ALERT	|
| resource | dict | ...		| N/A	|
| addtional_info | dict | ... 	| {"application": "MyApp", "url" "https://...." } |
| occured_at | datetime | event_time | "2021-08-23T06:47:32.753Z" |

# Reference

https://docs.appdynamics.com/appd/23.x/latest/en/appdynamics-essentials/alert-and-respond/actions/predefined-templating-variables
