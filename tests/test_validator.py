from guardrails import Guard
from validator import GuardrailsPII

guard = Guard.from_string(
    validators=[
        GuardrailsPII(entities=["DATE_TIME"], on_fail="fix", use_local=True)
    ]
)


def test_validator_success():
    TEST_OUTPUT = "He is a soccer player."
    raw_output, guarded_output, *rest = guard.parse(TEST_OUTPUT)
    assert guarded_output == TEST_OUTPUT


def test_validator_fail():
    TEST_FAIL_OUTPUT = "Cristiano Ronaldo dos Santos Aveiro (born 5 February 1985) is a Portuguese professional footballer."
    raw_output, guarded_output, *rest = guard.parse(TEST_FAIL_OUTPUT)
    assert (
        guarded_output
        == "Cristiano Ronaldo dos Santos Aveiro (born <DATE_TIME>) is a Portuguese professional footballer."
    )
