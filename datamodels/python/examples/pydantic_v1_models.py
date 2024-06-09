import json
from urllib.request import Request, urlopen

from datagovgr_datamodels.pydantic_v1 import VaccinationData


url = "https://data.gov.gr/api/v1/query/mdg_emvolio?date_from=2021-01-01&date_to=2021-01-01"
# Add your own Authorization token, this is a dummy one.
headers = {"Authorization": "Token 87a465af94af31194a24dcadf7e12b3c9e22b366"}
request = Request(url, headers=headers)

response = urlopen(request)
response_body = response.read().decode("utf-8")

data = json.loads(response_body)

vaccination = VaccinationData.parse_obj(data[1])
print(
    f"Total vaccinations in '{vaccination.area}' "
    f"for {vaccination.referencedate.date()}: "
    f"{vaccination.totalvaccinations}."
)
