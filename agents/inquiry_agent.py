def extract_inquiry_info(text):
    """
    Mock function for extracting inquiry details from raw text.
    Later versions can use NLP or rule-based parsing.
    """
    # Placeholder: simulate some structured data extraction
    sample_result = {
        "product": "Electric Scooter",
        "quantity": 100,
        "origin_port": "Shanghai",
        "destination_port": "Los Angeles",
        "incoterm": "FOB",
        "delivery_date": "TBD"
    }

    return {
        "status": "parsed",
        "agent": "inquiry_agent",
        "input_length": len(text),
        "data": sample_result
    }
