# Student Performance Dataset - Initial Information

This file summarizes the dataset selected for the statistical part of the project.

## Source and Context

The dataset describes student achievement in secondary education in two Portuguese schools. The data was collected using school reports and questionnaires. It contains demographic, social, school-related, and academic variables.

Two datasets are available:

- `student-mat.csv` - Mathematics course,
- `student-por.csv` - Portuguese language course.

The dataset was used by Cortez and Silva (2008) for classification and regression tasks related to student performance.

## Important Modeling Note

The target variable `G3` is the final grade. It is strongly correlated with `G1` and `G2`, because:

- `G1` is the first period grade,
- `G2` is the second period grade,
- `G3` is the final grade.

For the main regression analysis, it is better to exclude `G1` and `G2` from the model. This makes the model more useful because it tries to explain final performance using student characteristics and school-related factors rather than earlier grades.

## Variables

### Demographic and Family Variables

| Variable | Description |
| --- | --- |
| `school` | Student's school: `GP` - Gabriel Pereira, `MS` - Mousinho da Silveira |
| `sex` | Student's sex: `F` - female, `M` - male |
| `age` | Student's age, from 15 to 22 |
| `address` | Home address type: `U` - urban, `R` - rural |
| `famsize` | Family size: `LE3` - less or equal to 3, `GT3` - greater than 3 |
| `Pstatus` | Parents' cohabitation status: `T` - living together, `A` - apart |
| `Medu` | Mother's education: 0 - none, 1 - primary, 2 - 5th to 9th grade, 3 - secondary, 4 - higher |
| `Fedu` | Father's education: 0 - none, 1 - primary, 2 - 5th to 9th grade, 3 - secondary, 4 - higher |
| `Mjob` | Mother's job: `teacher`, `health`, `services`, `at_home`, `other` |
| `Fjob` | Father's job: `teacher`, `health`, `services`, `at_home`, `other` |
| `guardian` | Student's guardian: `mother`, `father`, `other` |

### School and Study Variables

| Variable | Description |
| --- | --- |
| `reason` | Reason for choosing the school: `home`, `reputation`, `course`, `other` |
| `traveltime` | Home-to-school travel time: 1 - below 15 min, 2 - 15 to 30 min, 3 - 30 min to 1 hour, 4 - above 1 hour |
| `studytime` | Weekly study time: 1 - below 2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, 4 - above 10 hours |
| `failures` | Number of past class failures: `n` if 1 <= n < 3, else 4 |
| `schoolsup` | Extra educational support: yes or no |
| `famsup` | Family educational support: yes or no |
| `paid` | Extra paid classes within the course subject: yes or no |
| `activities` | Extra-curricular activities: yes or no |
| `nursery` | Attended nursery school: yes or no |
| `higher` | Wants to take higher education: yes or no |
| `internet` | Internet access at home: yes or no |

### Social and Lifestyle Variables

| Variable | Description |
| --- | --- |
| `romantic` | Student is in a romantic relationship: yes or no |
| `famrel` | Quality of family relationships, from 1 - very bad to 5 - excellent |
| `freetime` | Free time after school, from 1 - very low to 5 - very high |
| `goout` | Going out with friends, from 1 - very low to 5 - very high |
| `Dalc` | Workday alcohol consumption, from 1 - very low to 5 - very high |
| `Walc` | Weekend alcohol consumption, from 1 - very low to 5 - very high |
| `health` | Current health status, from 1 - very bad to 5 - very good |
| `absences` | Number of school absences, from 0 to 93 |

### Grade Variables

| Variable | Description |
| --- | --- |
| `G1` | First period grade, from 0 to 20 |
| `G2` | Second period grade, from 0 to 20 |
| `G3` | Final grade, from 0 to 20; main target variable |

## Planned Use in the Project

The dataset will be used for:

- exploratory data analysis,
- hypothesis testing,
- multiple regression analysis,
- residual analysis and model diagnostics.

The queueing theory part of the course project will be developed later as a separate module.
