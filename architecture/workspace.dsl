workspace {
    name "Сервис поиска попутчиков"

    !identifiers hierarchical


    model {

        properties { 
            structurizr.groupSeparator "/"
        }

        user = person "Пользователь"

        driver = person "Водитель"


        trip_system = softwareSystem "Система поиска попутки" {
            description "Сервис по поиску попутки"

            
            user_service = container "User Service" {
                description "Сервис управления пользователями"
            }   

            trip_service = container "Trip Service" {
                description "Сервис управления поездками"
            }    

            group "Слой данных" {
                user_database = container "User Database" {
                    description "База данных с пользователями"
                    technology "PostgreSQL 15"
                    tags "database"
                }

                user_cache = container "User Cache" {
                    description "Кеш пользовательских данных для ускорения аутентификации"
                    technology "PostgreSQL 15"
                    tags "database"
                }

                route_database = container "Route Database" {
                    description "База данных маршрутов"
                    technology "MongoDB"
                    tags "database"
                }

                trip_database = container "Trip Database" {
                    description "База данных поездок"
                    technology "MongoDB"
                    tags "database"
                }

                trip_database -> route_database "Хранение данных о маршруте"
                trip_database -> user_database "Связь между поездкой и пользователем"
            }

            user_service -> user_cache "Получение/обновление данных о пользователях" 
            user_service -> user_database "Получение/обновление данных о пользователях" 

            trip_service -> user_service "Аутентификация пользователя/"

            trip_service -> trip_database "Получение/обновление данных о поездках"
            trip_service -> route_database "Получение/обновление даннх о маршрутах"

            user -> user_service "Регистрация нового пользователя"
            user -> trip_service "Поиск попутки"

            driver -> user_service "Регистрация нового водителя"
            driver -> trip_service "Публикация поездки"
        }

        user -> trip_system "Поиск попутки"
        driver -> trip_system "Публикация поездки"
    }
    
    views {
        themes default

        properties {
            structurizr.tooltips true
        }

        # !script groovy {
        #    workspace.views.createDefaultViews()
        #    workspace.views.views.findAll { it instanceof com.structurizr.view.ModelView }.each { it.enableAutomaticLayout() }
        #}

        systemContext trip_system {
            autoLayout
            include *
        }

        container trip_system {
            autoLayout
            include *
        }

        dynamic trip_system "UC01" "Добавление нового пользователя" {
            autoLayout
            user -> trip_system.user_service "Создать нового пользователя (POST /user)"
            trip_system.user_service -> trip_system.user_database "Сохранить данные о пользователе" 
        }

        dynamic trip_system "UC02" "Поиск пользователя по логину" {
            autoLayout
            trip_system.trip_service -> trip_system.user_service "Поиск пользователя по логину"
            trip_system.user_service -> trip_system.user_database "SQL запрос в базу данных"
        }

        dynamic trip_system "UC03" "Поиск пользователя по маске имя и фамилии" {
            autoLayout
            trip_system.trip_service -> trip_system.user_service "Поиск пользователя по маске имя и фамилии"
            trip_system.user_service -> trip_system.user_database "SQL запрос в базу данных"
        }

        dynamic trip_system "UC04" "Создание маршрута" {
            autoLayout
            driver -> trip_system.trip_service "Публикация маршрут"
            trip_system.trip_service -> trip_system.user_service "Аутентификация пользователя"
            trip_system.trip_service -> trip_system.route_database "В случае отсутствия маршрута создается новый маршрут"
        }

        dynamic trip_system "UC05" "Получение маршрутов пользователя" {
            autoLayout
            user -> trip_system.trip_service "Получение маршрутов пользователя"
            trip_system.trip_service -> trip_system.user_service "Аутентификация пользователя"
            trip_system.trip_service -> trip_system.trip_database "Получение связей маршрутов из поездок пользователя"
            trip_system.trip_service -> trip_system.route_database "Получение маршрутов"
        }

        dynamic trip_system "UC06" "Создание поездки" {
            autoLayout
            driver -> trip_system.trip_service "Публикует поездку по маршруту"
            trip_system.trip_service -> trip_system.user_service "Аутентификация пользователя"
            trip_system.trip_service -> trip_system.route_database "Создание маршрута"
            trip_system.trip_service -> trip_system.trip_database "Сохранение данных о поездке"
        }
        
        dynamic trip_system "UC07" "Подключение пользователей к поездке" {
            autoLayout
            user -> trip_system.trip_service "Поиск попутки по маршруту"
            trip_system.trip_service -> trip_system.user_service "Аутентификация пользователя"
            trip_system.trip_service -> trip_system.route_database "Поиск ID маршрута"
            trip_system.trip_service -> trip_system.trip_database "Поиск поездок по текущему ID маршрута"
            user -> trip_system.trip_service "Подтверждение пользоветеля"
            trip_system.trip_service -> trip_system.trip_database "Привязка пользователя к поездке"
        }
        
        dynamic trip_system "UC08" "Подключение пользователей к поездке" {
            autoLayout
            user -> trip_system.trip_service "Получение данных о поездке"
            trip_system.trip_service -> trip_system.user_service "Аутентификация пользователя"
            trip_system.trip_service -> trip_system.trip_database "Возврат данных о поездке"
        }

        styles {
            element "database" {
                shape cylinder
            }
        }
    }
}