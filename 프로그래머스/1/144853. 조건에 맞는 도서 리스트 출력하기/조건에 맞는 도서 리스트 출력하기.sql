-- 코드를 입력하세요
SELECT book_id, date_format(published_date, '%Y-%m-%d') as published_date
from book
where "2021-01-01" < published_date and published_date < "2021-12-21" and category = "인문"