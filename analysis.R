# Load the cleaned breast cancer data
df <- read.csv("breast_cancer_clean.csv")

cat("Rows:", nrow(df), " Columns:", ncol(df), "\n")
cat("Missing values:", sum(is.na(df)), "\n\n")

# Number of tumours by diagnosis
cat("Tumours by diagnosis:\n")
print(table(df$diagnosis))

# Average radius, area and concave points by diagnosis
cat("\nAverages by diagnosis:\n")
summary_table <- aggregate(
  cbind(mean_radius, mean_area, mean_concave_points) ~ diagnosis,
  data = df, FUN = mean
)
summary_table[, -1] <- round(summary_table[, -1], 3)
print(summary_table)

# Percentage of malignant tumours
pct <- round(100 * mean(df$diagnosis == "malignant"), 1)
cat("\nPercent malignant:", pct, "%\n")

# Plot 1: radius by diagnosis
png("r_plot1_radius.png", width = 900, height = 600, res = 150)
boxplot(mean_radius ~ diagnosis, data = df,
        col = c("#2a9d8f", "#e63946"),
        main = "Mean radius by diagnosis (R)",
        xlab = "Diagnosis", ylab = "Mean radius")
dev.off()

# Plot 2: radius vs area
png("r_plot2_radius_vs_area.png", width = 900, height = 600, res = 150)
cols <- ifelse(df$diagnosis == "malignant", "#e63946", "#2a9d8f")
plot(df$mean_radius, df$mean_area, col = cols, pch = 16, cex = 0.7,
     main = "Mean radius vs mean area (R)",
     xlab = "Mean radius", ylab = "Mean area")
legend("topleft", legend = c("benign", "malignant"),
       col = c("#2a9d8f", "#e63946"), pch = 16)
dev.off()

cat("\nSaved r_plot1_radius.png and r_plot2_radius_vs_area.png\n")
