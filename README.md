# Project UI android_app-autotests for Wikipedia
<!-- Technology -->

## Используемые инструменты и фреймворки:
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/logo/docker.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

<!-- Тест кейсы -->

## Что проверяют автотесты:
**Все проверки проходят в приложении Wikipedia**
* Проверка поиска, через поисковой запрос
* Проверка голосового поиска
* Проверка пустого поискового запроса
* Добавления еще одного языка

<!-- Jenkins -->

## <img width="3%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

## [Job](https://jenkins.autotests.cloud/job/diploma_mobile_tests/)

#### Когда нажимаем "Собрать сейчас" начнется сборка билда, запустятся тесты. Тесты проходят на реальном девайсе, с помощью Browserstack

![This is an image](images/screenshots/jenkins_start.png)

<!-- Browserstack -->

### <img width="3%" title="Browserstack" src="images/logo/browserstack.png"> Запуск проекта в [Browserstack](https://www.browserstack.com)
#### После запуска сборки в Jenkins, тесты стартуют удаленно, с помощью Browserstack. Здесь мы в реальном времени можем следить за результатом прохождения тестов:
#### Тесты проходят на девайсе Google Pixel 3, Android 9.0
![This is an image](images/screenshots/browserstack.png)

#### Пример прохождения теста в Browserstack:

![This is an image](images/screenshots/example_mobile_test.gif)

<!-- Allure report -->

## <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure report

#### После прохождения всех тестов, генерируется Allure отчет, в котором есть вся информация о тестах, которые были запущены
![This is an image](images/screenshots/allure_dashboard.png)

#### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

#### Во вкладке Suites находятся собранные тест кейсы, к которым прикрепляются аттачменты: в данном случае только видео прохождение тестов
![This is an image](images/screenshots/allure_attachments.png)

<!-- Telegram -->

## <img width="3%" title="Telegram" src="images/logo/tg.png"> Проект так же интегрирован с Telegram
#### По окончании прохождения тестов, бот присылает сообщение с информацией о test run'е, в сообщении содержится ссылка на Allure отчет

![This is an image](images/screenshots/telegram_notification.png)

<!-- Allure TestOps -->

## <img width="3%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps

#### Вся отчетность сохраняется в Allure TestOps, где есть вся аналогичная информация с Allure отчета

#### Dashboard:

![This is an image](images/screenshots/allure_testops_dashboard.png)

#### Launches:
![This is an image](images/screenshots/allure_testops_dashboard2.png)

#### После того, как мы запускаем сборку в Jenkins, Allure TestOps автоматически создает test suites, test cases на основе нашего кода:

![This is an image](images/screenshots/allure_testops_test_cases.png)

#### На вкладке с тестами, мы можем:
- Управлять всеми тест-кейсами (стандартный функционал для TMS)
- Запускать тесты по отдельности, если они автоматические, то они запустятся на сервере в Jenkins
- Интегрировать с Jira

#### Если мы запустили test run, то на вкладке "launches", мы можем:
- Наблюдать, как будут проходить тесты в live режиме
- Перезапускать тесты, если они со статусом broken и failed
- Перезапускать тесты мануально, если, к примеру, у нас проблема с web.driver
- Создавать дефекты

<!-- Jira -->

## <img width="3%" title="Jira" src="images/logo/jira.png"> Интеграция с Jira
#### Настроив через Allure TestOps интеграцию с Jira, мы можем отправлять тест-кейс и тест раны в Jira

![This is an image](images/screenshots/jira.png)
