from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    landing = request.GET.get('from-landing')
    if landing is not None:
        counter[landing] += 1
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_test_arg = request.GET.get('ab-test-arg')
    if ab_test_arg == 'original':
        ad[ab_test_arg] += 1
        return render(request, 'landing.html')
    elif ab_test_arg == 'test':
        ad[ab_test_arg] += 1
        return render(request, 'landing_alternate.html')
    return None


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    test_conv = counter['test'] / ad['test']
    orig_conv = counter['original'] / ad['original']
    return render(request, 'stats.html', context={
        'test_conversion': test_conv,
        'original_conversion': orig_conv,
    })
