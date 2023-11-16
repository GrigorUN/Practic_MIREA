import importlib.util
import pkgutil
import argparse
import graphviz

# Функция для получения зависимостей пакета
def get_package_dependencies(package_name):
    dependencies = set()
    
    try:
        # Находим спецификацию (spec) для пакета
        spec = importlib.util.find_spec(package_name)
        if spec is not None:
            # Используем pkgutil для поиска модулей внутри пакета
            for module in pkgutil.walk_packages(spec.submodule_search_locations, prefix=package_name + '.'):
                dependencies.add(module.name)
    except Exception as e:
        # В случае ошибки выводим сообщение
        print(f"Ошибка при получении зависимостей для пакета {package_name}: {e}")
    
    return dependencies

# Функция для создания и возвращения графа зависимостей
def generate_dependency_graph(package_name):
    graph = graphviz.Digraph(format='png')
    graph.node(package_name)  # Добавляем узел для основного пакета
    
    dependencies = get_package_dependencies(package_name)
    
    for dependency in dependencies:
        graph.node(dependency)  # Добавляем узел для каждой зависимости
        graph.edge(package_name, dependency)  # Соединяем основной пакет с зависимостями
    
    return graph

# Основная функция
def main():
    # Используем argparse для обработки аргументов командной строки
    parser = argparse.ArgumentParser(description='Генерация графа зависимостей для пакета.')
    parser.add_argument('package_name', type=str, help='Имя пакета')

    args = parser.parse_args()
    package_name = args.package_name

    # Генерируем граф зависимостей
    dependency_graph = generate_dependency_graph(package_name)
    
    # Выводим код Graphviz на экран
    print(dependency_graph.source)

if __name__ == "__main__":
    main()


# python 2.py requests
