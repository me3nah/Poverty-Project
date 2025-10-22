# Steps of R code - mhi

The following are the steps that R code takes to generate the table of results using mhi as the aggregate.

| Code Step | LIS Functionality | DART Compliance and Explanation |
|---|---|---|
| 1. Aggregate Construction | `map(data_list, ~ mutate(.x, mhi = hifactor + hiprivate + hi33))` | The code explicitly selects 'mhi' and constructs the variable: mhi = hifactor + hiprivate + hi33. This aligns with the definition of Market Household Income (pre-tax/transfer income), assuming these LIS variables collectively define the pre-tax, pre-transfer market income aggregate. |
| 2. Outlier Handling (Coding) | `apply_iqr_top_bottom_coding("mhi", "hwgt", times = 3)` | The DART methodology mandates bottom- and top-coding to constrain extreme income values. The code applies this standard IQR-based treatment. In the process, the function sets all negative incomes to zero. |
| 3. Currency Adjustment (PPP) | `apply_ppp_adjustment("mhi", database = "lis", transformation = "lisppp")` | DART indicators, such as the Median, are reported in PPP-adjusted International Dollars to ensure cross-country comparability over time. This step standardizes the monetary variable. |
| 4. Equivalisation | `apply_sqrt_equivalisation("mhi")` | This step implements the DART-mandated square-root equivalence scale to adjust household income for size differences, yielding income at the individual level. |
| 5. Filtering | `filter(.x, !!sym(chosen_aggregate) > 0, !is.na(.data[[chosen_aggregate]]), !is.na(ppopwgt))` | Compliant with the requirement to exclude data points with invalid income or weight values. The code filters out missing weights and non-positive income values. |
| 6. Median Calculation | `run_weighted_percentiles(chosen_aggregate, "ppopwgt", probs = 0.5)` | This computes the median (50th percentile) of the equivalised and weighted income distribution, using the person-level adjusted weight (ppopwgt). |
| 7. Poverty Line Definition | `mutate(pl = alpha * median)` | The code defines the poverty line (pl) as α (set to 0.5) times the median. This directly implements the Relative Poverty Rate at 50% of the Median definition. |
| 8. Poverty Rate Calculation | `map_dbl(data_with_pl, ~ weighted.mean(.x$below_pl, .x$ppopwgt, na.rm = TRUE))` | The final step calculates the weighted percentage of the population whose equivalised income is below the newly calculated poverty line. |
