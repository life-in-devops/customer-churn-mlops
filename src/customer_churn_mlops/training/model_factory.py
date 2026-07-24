from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression

from customer_churn_mlops.common.constants import (
    DEFAULT_RANDOM_STATE,
    GRADIENT_BOOSTING,
    LOGISTIC_REGRESSION,
    RANDOM_FOREST,
)


class ModelFactory:
    """
    Factory class for creating ML models.
    """

    @staticmethod
    def get_models() -> dict:
        return {
            LOGISTIC_REGRESSION: LogisticRegression(
                random_state=DEFAULT_RANDOM_STATE,
                max_iter=1000,
            ),
            RANDOM_FOREST: RandomForestClassifier(
                n_estimators=200,
                random_state=DEFAULT_RANDOM_STATE,
            ),
            GRADIENT_BOOSTING: GradientBoostingClassifier(
                random_state=DEFAULT_RANDOM_STATE,
            ),
        }
