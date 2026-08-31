import torch
from presidio_analyzer import EntityRecognizer, RecognizerResult
from gliner import GLiNER
from .constants import PRESIDIO_TO_GLINER, GLINER_TO_PRESIDIO


class GLiNERRecognizer(EntityRecognizer):
    def __init__(self, supported_entities, model_name, use_gpu=True):
        self.model_name = model_name
        self.supported_entities = supported_entities
        self.use_gpu = use_gpu
        self.device = self._get_device()

        gliner_entities = set()

        for entity in supported_entities:
            if entity not in PRESIDIO_TO_GLINER:
                continue
            gliner_entities.update(PRESIDIO_TO_GLINER[entity])
        self.gliner_entities = list(gliner_entities)

        super().__init__(supported_entities=supported_entities)

    def _get_device(self):
        """Determine the device to use for inference"""
        if self.use_gpu and torch.cuda.is_available():
            return torch.device("cuda")
        return torch.device("cpu")

    def load(self) -> None:
        """Load the model and move it to the appropriate device"""
        self.model = GLiNER.from_pretrained(self.model_name)
        self.model = self.model.to(self.device)
        if self.use_gpu and torch.cuda.is_available():
            self.model.eval()

    def analyze(self, text, entities=None, nlp_artifacts=None):
        """Analyze text using GPU-accelerated GLiNER model"""
        # Ensure model is on correct device
        if hasattr(self.model, 'device') and self.model.device != self.device:
            self.model = self.model.to(self.device)
        
        # Run inference with gradient disabled for efficiency
        with torch.no_grad():
            results = self.model.predict_entities(text, self.gliner_entities)
        return [
            RecognizerResult(
                entity_type=GLINER_TO_PRESIDIO[entity["label"]],
                start=entity["start"],
                end=entity["end"],
                score=entity.get("score"),
                recognition_metadata={
                    RecognizerResult.RECOGNIZER_NAME_KEY: self.name,
                    RecognizerResult.RECOGNIZER_IDENTIFIER_KEY: self.id,
                },
            )
            for entity in results
        ]
