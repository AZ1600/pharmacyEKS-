import json
from uuid import uuid4

from app.infra.dynamodb import table, events


def create_drug_service(drug_data, tenant_id: str, user_id: str):
    """
    Create a tenant-scoped drug record in DynamoDB
    and publish a DrugCreated event.
    """

    payload = (
        drug_data.model_dump()
        if hasattr(drug_data, "model_dump")
        else dict(drug_data)
    )

    item = {
        **payload,
        "id": str(uuid4()),
        "tenant_id": tenant_id,
        "created_by": user_id,
    }

    table.put_item(Item=item)

    events.put_events(
        Entries=[
            {
                "Source": "pharmacy-api",
                "DetailType": "DrugCreated",
                "Detail": json.dumps(item),
                "EventBusName": "default",
            }
        ]
    )

    return {
        "message": "Drug created successfully",
        "data": item,
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
            "data": None,
        }

    return {
        "message": "Drug retrieved successfully",
        "data": item,
    }