from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer import RecognizerRegistry
from guardrails_grhub_guardrails_pii.gliner_recognizer import GLiNERRecognizer  # type: ignore[import]
from guardrails_grhub_guardrails_pii.analyzer_engine import AnalyzerEngine  # type: ignore[import]


gliner_recognizer = GLiNERRecognizer(
    supported_entities=[
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "DOMAIN_NAME",
        "IP_ADDRESS",
        "DATE_TIME",
        "LOCATION",
        "PERSON",
        "URL",
    ],
    model_name="urchade/gliner_small-v2.1",
)
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
registry.add_recognizer(gliner_recognizer)
pii_analyzer = AnalyzerEngine(
    registry=registry, supported_languages=["en"]
)
pii_anonymizer = AnonymizerEngine()