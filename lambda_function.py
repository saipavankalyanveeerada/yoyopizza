import json
import boto3
import uuid
dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('pizza')




def lambda_handler(event, context):
    # TODO implement
    size=event['currentIntent']['slots']['size']
    topping=event['currentIntent']['slots']['toppings']
    time=event['currentIntent']['slots']['time']
    orderid=str(uuid.uuid4())
    table.put_item(
         Item = {
            'orderid' : orderid,
            'size' : size,
            'topping' : topping,
            'time' : time
        }
        )
    response = 'We have taken your order '+size+' pizza with '+topping+' topping. THANK YOU! Have a nice day'
    return {
        "sessionAttributes":{},
        "dialogAction" : {
            "type" : "Close",
            "fulfillmentState":"Fulfilled",
            "message":{
                "contentType":"PlainText",
                "content":response
            }
        }
    }
   