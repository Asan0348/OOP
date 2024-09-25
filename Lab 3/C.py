def process_queries(n, a, queries):
    results = []
    
    for query in queries:
        l1, r1, l2, r2 = query
        count = 0
        
        # Проходим по каждому элементу массива a
        for c in a:
            # Проверяем, входит ли элемент в диапазон [l1, r1] или [l2, r2]
            if (l1 <= c <= r1) or (l2 <= c <= r2):
                count += 1
        
        # Запоминаем результат для данного запроса
        results.append(count)
    
    return results

# Чтение данных
n, q = map(int, input().split())
a = list(map(int, input().split()))

queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))

# Обработка запросов и вывод результатов
results = process_queries(n, a, queries)
for result in results:
    print(result)
