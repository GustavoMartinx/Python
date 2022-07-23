# Pack: packed x parameters inside a tuple
def sum(*nums):
    total = 0
    for n in nums:
        total += n
    return total


# Pack: packed x parameters inside a dictionary
def final_result(**kwargs):
    status = 'Approved' if kwargs['score'] >= 6 else 'Disapproved'
    return f'{kwargs["name"]} was {status}'
