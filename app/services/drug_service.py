from app.infra.dynamodb import table, sqs, events


def create_drug_service(drug_data: dict):
    """
    Creates a new drug record in DynamoDB.
    """

    response = table.put_item(
        Item=drug_data
    )

    # Optional: send event to EventBridge
    events.put_events(
        Entries=[
            {
                "Source": "pharmacy-api",
                "DetailType": "DrugCreated",
                "Detail": str(drug_data),
                "EventBusName": "default"
            }
        ]
    )

    return {
        "message": "Drug created successfully",
        "data": drug_data,
        "dynamodb_response": response
    }


def get_drug_service(drug_id: str):
    """
    Fetch a drug by ID from DynamoDB.
    """

    response = table.get_item(
        Key={"id": drug_id}
    )

    item = response.get("Item")

    if not item:
        return {
            "message": "Drug not found",
            "data": None
        }

    return {
        "message": "Drug retrieved successfully",
        "data": item
    }