from src.jobs import read


def get_unique_job_types(path):
    csv_file = read(path)
    # for in para retornar os valores da coluna job_type
    return list({job["job_type"] for job in csv_file})


def filter_by_job_type(jobs, job_type):
    # cria variável para armazenar o a lista de empregos
    jobs_list = []
    # for in em jobs onde:
    for job in jobs:
        # se a coluna "job_title" corresponder ao parâmetro job_title,
        if job["job_type"] == job_type:
            # adiciona o emprego no array jobs_list
            jobs_list.append(job)

    return jobs_list


def get_unique_industries(path):
    csv_file = read(path)
    # for in para retornar os valores da coluna industry
    return list({ind["industry"] for ind in csv_file if ind["industry"]})


def filter_by_industry(jobs, industry):
    # cria variável para armazenar o a lista de empregos
    industries_list = []
    # for in em jobs onde:
    for job in jobs:
        # se a coluna "indistry" corresponder ao parâmetro industry,
        if job["industry"] == industry:
            # adiciona a industria no array industries_list
            industries_list.append(job)

    return industries_list


def get_max_salary(path):
    csv_file = read(path)

    max_salary_filter = max(
        # map: HOF que aplica uma função a cada item da lista
        map(
            # lambda: função anônima em python
            # filter: HOF para filtrar da mesma forma que em JS
            lambda job: int(job["max_salary"]), filter(
                # isdigit: retorna True se todos os caracteres forem dígitos
                lambda job: job["max_salary"].isdigit(), csv_file
            )
        )
    )
    return max_salary_filter


def get_min_salary(path):
    csv_file = read(path)

    min_salary_filter = min(
        # map: HOF que aplica uma função a cada item da lista
        map(
            # lambda: função anônima em python
            # filter: HOF para filtrar da mesma forma que em JS
            lambda job: int(job["min_salary"]), filter(
                # isdigit: retorna True se todos os caracteres forem dígitos
                lambda job: job["min_salary"].isdigit(), csv_file
            )
        )
    )
    return min_salary_filter


def matches_salary_range(job, salary):
    # Retorna ValueErrorse atender as condições abaixo:
    # Se `job["min_salary"]` or `job["max_salary"]` não existir
    # Se `job["min_salary"]` or `job["max_salary"]` não forem do tipo integers
    # Se `job["min_salary"]` for maior do que `job["max_salary"]`
    # Se `salary` não fordo tipo integer
    if(
        "min_salary" not in job or "max_salary" not in job
        or type(job["min_salary"]) != int or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError()

    # Retorna False se salary informado não estiver no range de salario do job:
    if salary < job["min_salary"] or salary > job["max_salary"]:
        return False
    return True


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
