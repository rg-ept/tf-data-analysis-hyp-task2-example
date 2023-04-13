import pandas as pd
import numpy as np


chat_id = 42877418

def solution(x: np.array, y: np.array) -> bool:
   res = stats.cramervonmises_2samp([x, y])

    if res.pval < 0.02:
        return True
    else:
        return False
