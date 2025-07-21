import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="generateSummary", auth_level=func.AuthLevel.ANONYMOUS)
def generateSummary(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        response_data = {
            "user": name,
            "overdue_patients": 42,
            "immunizations_this_year": 198,
            "overdue_percent": round((42 / (42 + 198)) * 100, 2)
        }
        return func.HttpResponse(
            json.dumps(response_data),
            mimetype="application/json",
            status_code=200
        )
    else:
        # Always return something, even if name is missing
        return func.HttpResponse(
            json.dumps({"error": "Missing 'name' in query or body."}),
            mimetype="application/json",
            status_code=400
        )
