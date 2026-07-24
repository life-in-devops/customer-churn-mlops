from customer_churn_mlops.training.model_factory import ModelFactory

models = ModelFactory.get_models()

print("Available Models\n")

for name, model in models.items():
    print(name)
    print(model)
    print("-" * 60)
