from customer_churn_mlops.training.evaluator import ModelEvaluator

y_true = [0, 1, 0, 1, 1]

y_pred = [0, 1, 0, 0, 1]

y_prob = [0.10, 0.95, 0.20, 0.40, 0.90]

metrics = ModelEvaluator.evaluate(
    y_true,
    y_pred,
    y_prob,
)

print(metrics)
