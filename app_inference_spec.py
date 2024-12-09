from fastapi import HTTPException
from pydantic import BaseModel
from typing import List, Optional, cast

from validator.main import GuardrailsPII, InferenceInput as InputRequest, InferenceOutput as OutputResponse
from models_host.base_inference_spec import BaseInferenceSpec


class InferenceSpec(BaseInferenceSpec):
    model: Optional[GuardrailsPII] = None
    model_name = "guardrails_pii"

    def load(self):
        self.model = GuardrailsPII(use_local=True, entities=[
            "CREDIT_CARD",
            "CRYPTO",
            "DATE_TIME",
            "EMAIL_ADDRESS",
            "IBAN_CODE",
            "IP_ADDRESS",
            "NRP",
            "LOCATION",
            "PERSON",
            "PHONE_NUMBER",
            "MEDICAL_LICENSE",
            "URL",
            "US_BANK_NUMBER",
            "US_DRIVER_LICENSE",
            "US_ITIN",
            "US_PASSPORT",
            "US_SSN",
            "UK_NHS",
            "ES_NIF",
            "ES_NIE",
            "IT_FISCAL_CODE",
            "IT_DRIVER_LICENSE",
            "IT_VAT_CODE",
            "IT_PASSPORT",
            "IT_IDENTITY_CARD",
            "PL_PESEL",
            "SG_NRIC_FIN",
            "SG_UEN",
            "AU_ABN",
            "AU_ACN",
            "AU_TFN",
            "AU_MEDICARE",
            "IN_PAN",
            "IN_AADHAAR",
            "IN_VEHICLE_REGISTRATION",
            "IN_VOTER",
            "IN_PASSPORT",
            "FI_PERSONAL_IDENTITY_CODE"
        ])

    def process_request(self, input_request: InputRequest):
        text = input_request.text
        entities = input_request.entities  
        if not text or not entities:
            raise HTTPException(status_code=400, detail="Invalid input")
        args = (text, entities)
        kwargs = {}  
        return args, kwargs

    def infer(self, text: str, entities: List[str]) -> OutputResponse:
        # should be loaded before this method is called
        model = cast(GuardrailsPII, self.model)
        return model._inference_local(InputRequest(text=text, entities=entities))

            