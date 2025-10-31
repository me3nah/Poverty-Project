

# Install needed packages (only once)
if (!require("tidyverse")) install.packages("tidyverse")
if (!require("zoo")) install.packages("zoo")

library(tidyverse)
library(zoo)

# --- 1. Load the data ---------------------------------------------------------
data_path <- "analysis/food-insecurity/data/eu_silc_meal_data.csv"
df <- read_csv(data_path)

# --- 2. Define 3-year rolling average function --------------------------------
roll3 <- function(x) rollapply(x, width = 3, FUN = mean, fill = NA, align = "center")

# --- 3. Define plotting function ----------------------------------------------
plot_country <- function(country) {
  cols <- c(paste0(country, "_Total"),
            paste0(country, "_Female"),
            paste0(country, "_Male"))
  
  data_long <- df %>%
    select(Year, all_of(cols)) %>%
    mutate(across(all_of(cols), roll3)) %>%
    pivot_longer(cols = -Year, names_to = "Group", values_to = "Value") %>%
    mutate(Group = recode(Group,
                          !!paste0(country, "_Total") := "Total",
                          !!paste0(country, "_Female") := "Single female",
                          !!paste0(country, "_Male") := "Single male"))
  
  ggplot(data_long, aes(x = Year, y = Value, color = Group, linetype = Group)) +
    geom_line(size = 1.1) +
    scale_color_manual(values = c("blue", "red", "darkgreen")) +
    labs(
      title = paste(country, ": Inability to afford a meal every second day (%)"),
      subtitle = "3-year rolling average (Eurostat ilc_mdes03)",
      y = "Percent", x = "Year"
    ) +
    theme_minimal(base_size = 14) +
    theme(legend.title = element_blank(),
          plot.title = element_text(face = "bold"))
}

# --- 4. Save plots ------------------------------------------------------------
ggsave("analysis/food-insecurity/visuals/germany_meal_affordability_smoothed.png",
       plot_country("Germany"), width = 8, height = 5, dpi = 300)

ggsave("analysis/food-insecurity/visuals/uk_meal_affordability_smoothed.png",
       plot_country("UK"), width = 8, height = 5, dpi = 300)

cat("✅ Plots saved successfully in analysis/food-insecurity/visuals/\n")
