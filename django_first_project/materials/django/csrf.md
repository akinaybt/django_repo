## CSRF
CSRF (англ. cross-site request forgery — «межсайтовая подделка запроса», также известна как XSRF) — вид атак
на посетителей веб-сайтов, использующий недостатки протокола HTTP. Если жертва заходит на сайт, созданный 
злоумышленником, от её лица тайно отправляется запрос на другой сервер (например, на сервер платёжной системы), 
осуществляющий некую вредоносную операцию (например, перевод денег на счёт злоумышленника). Для осуществления данной 
атаки жертва должна быть аутентифицирована на том сервере, на 
который отправляется запрос, и этот запрос не должен требовать какого-либо подтверждения со стороны 
пользователя, которое не может быть проигнорировано или подделано атакующим скриптом.

[Межсайтовая подделка запроса](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D0%BA%D0%B0_%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0)

### Что значит CSRF значение недопустимо?
CSRF токен недействителен или отсутствует

Это сообщение означает, что вашему браузеру не удалось создать защищённые файлы куки или получить к ним доступ, чтобы авторизовать вход в вашу учетную запись.

### В чем заключается атака CSRF?
CSRF (англ. Сross Site Request Forgery — «Подделка межсайтовых запросов», также известен как XSRF) — вид атак на посетителей веб-сайтов, суть которого заключается в выполнении действий от имени пользователя без его ведома.

### Как работает защита от CSRF?
Защита от CSRF работает путём добавления ввашу форму скрытого поля, которое содержит значение, которое знаете только вы и ваш пользователь. Это гарантирует, что пользователь - а не какая-то другая сущность - отправляет данные

## [Документация CSRF Django](https://docs.djangoproject.com/en/4.1/ref/csrf/)