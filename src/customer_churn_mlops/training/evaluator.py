from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

from customer_churn_mlops.common.constants import (
    ACCURACY,
    F1_SCORE,
    PRECISION,
    RECALL,
    ROC_AUC,
)


class ModelEvaluator:
    """
    Evaluates binary classification models.
    """

    @staticmethod
    def evaluate(y_true, y_pred, y_prob):
        """
        Compute evaluation metrics.

        Parameters
        ----------
        y_true : array-like
        y_pred : array-like
        y_prob : array-like
            Probability of the positive class.
        """

        return {
            ACCURACY: accuracy_score(y_true, y_pred),
            PRECISION: precision_score(y_true, y_pred),
            RECALL: recall_score(y_true, y_pred),
            F1_SCORE: f1_score(y_true, y_pred),
            ROC_AUC: roc_auc_score(y_true, y_prob),
        }
