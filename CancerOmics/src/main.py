from load_data import (
    load_expression,
    load_models,
    load_prism,
    load_treatment_info,
)


expression = load_expression()
models = load_models()
prism = load_prism()
treatments = load_treatment_info()

print("Expression:", expression.shape)
print("Models:", models.shape)
print("PRISM:", prism.shape)
print("Treatments:", treatments.shape)
