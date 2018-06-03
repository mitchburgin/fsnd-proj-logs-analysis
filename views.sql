create view articleViews as 
    select path,
                count(*) as views,
    
    from public.log
    where path like '%/article/%'
    and status = '200 OK'
    and path != '/'
    group by path
    order by views desc;

create view articleInfo as
    select title,
                slug, 
                name
    from public.articles
    join public.authors
    on public.articles.author = public.authors.id;