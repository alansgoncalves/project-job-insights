from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {'max_salary': 8750, 'min_salary': 3600, 'date_posted': '2020-09-08'},
        {'max_salary': 12500, 'min_salary': 2500, 'date_posted': '2020-08-08'},
        {'max_salary': 10900, 'min_salary': 4650, 'date_posted': '2020-01-08'},
        {'max_salary': 6500, 'min_salary': 4300, 'date_posted': '2020-12-08'},
    ]

    sort_by_max_salary = [
        {'max_salary': 12500, 'min_salary': 2500, 'date_posted': '2020-08-08'},
        {'max_salary': 10900, 'min_salary': 4650, 'date_posted': '2020-01-08'},
        {'max_salary': 8750, 'min_salary': 3600, 'date_posted': '2020-09-08'},
        {'max_salary': 6500, 'min_salary': 4300, 'date_posted': '2020-12-08'},
    ]

    sort_by(jobs, 'max_salary')
    assert jobs == sort_by_max_salary
