# HR Analytics Dashboard (Power BI + Python)

## Overview
This project presents an HR analytics dashboard created using **Power BI**, with all data pre-processed and cleaned in **Python**. The goal is to uncover key HR insights related to attrition, compensation, work satisfaction, and employee demographics.

---

## 🗃️ Dataset Summary
- **Source**: Provided CSV file (`HR_Analytics.csv`)
- **Rows**: 1,470 employees
- **Columns**: 38 columns covering:
  - Demographics: `Age`, `Gender`, `MaritalStatus`, `AgeGroup`
  - Compensation: `MonthlyIncome`, `HourlyRate`, `DailyRate`, `SalarySlab`
  - Satisfaction: `JobSatisfaction`, `EnvironmentSatisfaction`, `WorkLifeBalance`, etc.
  - Tenure and experience: `YearsAtCompany`, `YearsWithCurrManager`, `TotalWorkingYears`
  - Status: `Attrition`, `OverTime`

---

## 🛠️ Tools Used
- **Python**: Data cleaning with `pandas`, `numpy`, `matplotlib`
- **Power BI**: Dashboard development and visualization
- **CSV**: For importing/exporting cleaned datasets

---

## Data Cleaning (`data_cleaning.py`)
The raw data was cleaned and prepared using Python with the following steps:

- Replaced missing values in `YearsWithCurrManager` with `-1` to indicate unknown
- Dropped constant-value columns:
  - `EmployeeCount`: Same value across all rows
  - `Over18`: Only one value ("Y") — not useful for analysis
- Found that `EmpID` had fewer unique values than total rows, indicating duplicates. Cross-checked with `EmployeeNumber` to confirm duplicate entries.
- Removed fully duplicated rows (identical across all columns)
- Removed partial duplicates by `EmpID`, keeping the first occurrence
- Saved duplicate `EmpID` records for manual review in `potential_conflicts.csv`
- Exported the cleaned dataset as `cleaned_data.csv` for Power BI

---

## ✅ Data Validation (`validate_cleaned_data.py`)
Post-cleaning checks confirmed:
- No missing values remain
- No fully duplicated rows
- `EmpID` is now unique across all entries
- All columns have appropriate data types
- Final dataset contains 1,470 unique employee records

---

## 📈 Power BI Dashboard Features
- **KPI Cards**: 
  - Total Employees
  - Average Monthly Income
  - Attrition Rate
- **Visuals**:
  - Bar Chart: Monthly Income by Job Role
  - Pie Chart: Attrition distribution
  - Slicers: Gender, Department, Attrition, Age Group
  - Heatmap: Satisfaction levels across departments

---

## Project Files

| File | Description |
|------|-------------|
| `HR_Analytics.csv` | Original raw dataset |
| `data_cleaning.py` | Script to clean and prepare data |
| `validate_cleaned_data.py` | Script to validate final cleaned dataset |
| `cleaned_data.csv` | Final dataset ready for Power BI |
| `potential_conflicts.csv` | Saved duplicate `EmpID` records before resolution |
| `hr_dashboard.pbix` | Power BI dashboard (if included) |

---



---
