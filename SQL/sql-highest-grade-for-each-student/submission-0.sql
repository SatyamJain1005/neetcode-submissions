-- Write your query below
with
ranked_ as (
    select
    *,
    row_number()over(
        partition by student_id
        order by score desc, exam_id
    ) rn
    from
    exam_results
)

select
student_id, exam_id, score
from
ranked_
where rn = 1