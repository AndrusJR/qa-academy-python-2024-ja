# qa-academy-python-2024-ja


# Coding rules

## Excluded  folders
1. .venv/ floder

## Dep updates
1. Major libs version needs to be revisited once per month



# How to setup venv
1.1 Setup your venv
1.2 Cerate venv into .venv folder 
1.3 Install deps from requirements.txt file

2 Before commit
2.1 run black tool
2.2 run flake8 tool
2.3 run isort tool


# How to run the tests?
1. Execute pytest . -s - v command staying in the root of the framework
2. To form a report execute pytest . -s -v --html=logs/report.html --self-contained-html




# Structure of the framework
1. tests - folder for tests
2. logs - folder to store local test execution logs 
3. src/system_under_test - folder for system under test abstractions
4. src/config - folder for configuration of framework
5. src/helpers - folder for single-use function, 



