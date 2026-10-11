from pathlib import Path
P=Path(__file__).resolve().parent.parent/'proekt/схемы'
P.mkdir(parents=True,exist_ok=True)
D={}
D[1]='''left to right direction
actor Читатель as R
actor Библиотекарь as L
rectangle "Онлайн-библиотека" {
usecase "Найти книгу" as Search
usecase "Бронировать книгу" as Reserve
usecase "Продлить срок" as Renew
usecase "Проверить доступность" as Check
usecase "Выдать книгу" as Issue
usecase "Принять книгу" as Return
usecase "Добавить книгу" as Add
}
R -- Search
R -- Reserve
R -- Renew
L -- Issue
L -- Return
L -- Add
Reserve ..> Check : <<include>>
Issue ..> Check : <<include>>'''
D[2]='''left to right direction
actor Клиент as C
actor "Банковская система" as B
rectangle Банкомат {
usecase "Снять наличные" as W
usecase "Проверить баланс" as Bal
usecase "Пополнить телефон" as Tel
usecase "Сменить ПИН-код" as Change
usecase "Проверить ПИН-код" as Pin
usecase "Напечатать чек" as Receipt
}
C -- W
C -- Bal
C -- Tel
C -- Change
B -- Pin
B -- W
B -- Bal
B -- Tel
B -- Change
W ..> Pin : <<include>>
Bal ..> Pin : <<include>>
Tel ..> Pin : <<include>>
Change ..> Pin : <<include>>
Receipt ..> W : <<extend>>\\n[клиент запросил чек]'''
D[3]='''left to right direction
actor Гость as G
actor Покупатель as C
actor Администратор as A
C --|> G
rectangle "Интернет-магазин" {
usecase "Просмотреть каталог" as Cat
usecase "Зарегистрироваться" as Reg
usecase "Оформить заказ" as Order
usecase "Оплатить заказ" as Pay
usecase "Управлять товарами" as Manage
}
G -- Cat
G -- Reg
C -- Order
C -- Pay
A -- Manage'''
D[4]='''left to right direction
actor Пациент as P
actor "Сервис уведомлений" as N
rectangle "Запись к врачу" {
usecase "Найти врача" as Find
usecase "Записаться на приём" as Book
usecase "Проверить свободное время" as Check
usecase "Отправить подтверждение" as Send
}
P -- Find
P -- Book
Book ..> Check : <<include>>
Book ..> Send : <<include>>
N -- Send'''
D[5]='''class Университет {
-название: String
-адрес: String
+добавитьФакультет()
}
class Факультет {
-название: String
+создатьГруппу()
}
class Группа {
-код: String
-годНабора: Integer
+зачислить(студент)
}
class Студент {
-номер: String
-ФИО: String
}
class Преподаватель {
-номер: String
-ФИО: String
+вестиЗанятие()
}
Университет "1" *-- "1..*" Факультет
Факультет "1" -- "0..*" Группа
Группа "0..1" o-- "0..*" Студент
Факультет "1" -- "0..*" Преподаватель
Преподаватель "0..*" -- "0..*" Группа : преподаёт'''
D[6]='''class Книга {
-ISBN: String
-название: String
+найтиЭкземпляр()
}
class Экземпляр {
-инвентарныйНомер: String
-статус: String
+выдать()
+вернуть()
}
class Читатель {
-номерБилета: String
-ФИО: String
+оформитьВыдачу()
}
class Выдача {
-датаВыдачи: Date
-срокВозврата: Date
-датаВозврата: Date [0..1]
+закрыть()
}
Книга "1" *-- "0..*" Экземпляр
Читатель "1" -- "0..*" Выдача
Экземпляр "1" -- "0..*" Выдача
note bottom of Выдача
{Для экземпляра не более
одной незакрытой выдачи}
end note'''
D[7]='''abstract class ТранспортноеСредство {
#номер: String
#скорость: Real
{abstract} +двигаться(): void
}
class Автобус {
+двигаться(): void
}
class Трамвай {
+двигаться(): void
}
class Такси {
+двигаться(): void
}
ТранспортноеСредство <|-- Автобус
ТранспортноеСредство <|-- Трамвай
ТранспортноеСредство <|-- Такси
note bottom of ТранспортноеСредство
Операция двигаться() переопределена
в каждом конкретном подклассе.
end note'''
D[8]='''interface Оплачиваемое {
+суммаКОплате(): Decimal
+оплатить(): void
}
class Заказ {
-итог: Decimal
+суммаКОплате(): Decimal
+оплатить(): void
}
class Штраф {
-сумма: Decimal
+суммаКОплате(): Decimal
+оплатить(): void
}
class Подписка {
-тариф: Decimal
+суммаКОплате(): Decimal
+оплатить(): void
}
Оплачиваемое <|.. Заказ
Оплачиваемое <|.. Штраф
Оплачиваемое <|.. Подписка'''
D[9]='''class Покупатель {
-id: UUID
-email: String
+создатьЗаказ(): Заказ
}
class Заказ {
-номер: String
-статус: String
+рассчитатьСумму(): Decimal
+подтвердить(): void
}
class ПозицияЗаказа {
-количество: Integer
-ценаНаМоментЗаказа: Decimal
+подытог(): Decimal
}
class Товар {
-артикул: String
-название: String
-цена: Decimal
+изменитьЦену(цена): void
}
class Категория {
-название: String
+добавитьТовар(товар): void
}
Покупатель "1" -- "0..*" Заказ
Заказ "1" *-- "1..*" ПозицияЗаказа
ПозицияЗаказа "0..*" --> "1" Товар
Категория "1" -- "0..*" Товар
note bottom of ПозицияЗаказа
{количество > 0; цена >= 0}
end note'''
D[10]='''class Студент {
-номер: String
-ФИО: String
}
class Дисциплина {
-код: String
-название: String
}
class РезультатЭкзамена {
-оценка: Integer
-дата: Date
}
Студент "0..*" -- "0..*" Дисциплина : сдаёт
(Студент, Дисциплина) .. РезультатЭкзамена
note bottom of РезультатЭкзамена
Один результат для пары
Студент–Дисциплина.
end note'''
D[11]='''object "иванов:Читатель" as R {
номерБилета = "R001"
ФИО = "Иванов"
}
object "книга1:Книга" as B1 {
название = "Алгоритмы"
}
object "книга2:Книга" as B2 {
название = "Компьютерные сети"
}
object "экз1:Экземпляр" as E1 {
инвентарныйНомер = "E101"
}
object "экз2:Экземпляр" as E2 {
инвентарныйНомер = "E202"
}
object "выдача1:Выдача" as L1 {
датаВыдачи = "2026-10-01"
датаВозврата = null
}
object "выдача2:Выдача" as L2 {
датаВыдачи = "2026-10-01"
датаВозврата = null
}
R -- L1
R -- L2
L1 -- E1
L2 -- E2
B1 *-- E1
B2 *-- E2'''
D[12]='''package Студенты as S
package "Учебный процесс" as U
package Расписание as T
package Отчёты as R
package "Общие сервисы" as C
U ..> S : использует контракты
T ..> U : учебные планы
R ..> S : контингент
R ..> U : успеваемость
R ..> T : расписание
S ..> C
U ..> C
T ..> C
R ..> C'''
D[13]='''left to right direction
skinparam componentStyle uml2
component "Веб-интерфейс" as Web
component Каталог as Cat
component Заказы as Ord
component Оплата as Pay
component "База данных" as DB
interface ICatalog as IC
interface IOrders as IO
interface IPayment as IP
interface IData as ID
Cat - IC
Ord - IO
Pay - IP
DB - ID
Web ..> IC
Web ..> IO
Ord ..> IC
Ord ..> IP
Cat ..> ID
Ord ..> ID
Pay ..> ID
legend bottom
Сплошная связь: предоставляет интерфейс
Пунктирная стрелка: требует интерфейс
endlegend'''
D[14]='''top to bottom direction
node "Смартфон пациента" as Phone {
artifact "Браузер / мобильный клиент" as Client
}
node "Веб-сервер" as Web {
artifact "Статические файлы + reverse proxy" as Proxy
}
node "Сервер приложений" as App {
artifact "booking.jar" as API
}
node "Сервер БД" as DB {
artifact "booking_db" as Data
}
node "Внешний SMS-шлюз" as SMS {
artifact "SMS API" as SMSAPI
}
Phone -- Web : HTTPS / TCP 443
Web -- App : HTTPS / TCP 8443
App -- DB : PostgreSQL + TLS / TCP 5432
App -- SMS : HTTPS / TCP 443'''
D[15]='''start
:Выбрать напиток;
if (Вода есть?) then (да)
fork
:Нагреть воду;
fork again
:Смолоть зёрна;
end fork
:Приготовить кофе;
:Выдать напиток;
else (нет)
:Показать ошибку «Нет воды»;
endif
stop'''
D[16]='''|Покупатель|
start
:Оформить корзину;
|Система|
:Проверить данные заказа;
|Склад|
:Проверить наличие;
if (Товар есть?) then (нет)
|Система|
:Сообщить об отсутствии товара;
stop
else (да)
endif
|Склад|
:Зарезервировать товар;
|Покупатель|
:Выбрать способ оплаты;
if (Онлайн?) then (да)
|Система|
:Провести оплату;
if (Оплата успешна?) then (да)
:Подтвердить заказ;
else (нет)
|Склад|
:Снять резерв;
|Система|
:Сообщить об ошибке оплаты;
stop
endif
else (при получении)
|Система|
:Подтвердить оплату при получении;
endif
|Склад|
:Собрать и передать заказ;
|Покупатель|
:Получить результат;
stop'''
D[17]='''start
:Подать документы;
repeat
:Проверить комплектность;
if (Комплект полный?) then (нет)
:Сообщить о недостающих документах;
:Доработать и подать пакет;
else (да)
endif
repeat while (Комплект неполный?) is (да) not (нет)
:Проверить условия приёма;
if (Условия выполнены и есть место?) then (да)
:Зачислить;
else (нет)
:Оформить мотивированный отказ;
endif
stop'''
D[18]='''start
:Проверить читательский билет;
if (Билет действителен?) then (да)
:Проверить задолженность;
if (Задолженность отсутствует?) then (да)
:Найти доступный экземпляр;
if (Экземпляр найден?) then (да)
:Оформить выдачу;
:Карточка выдачи; <<object>>
:Выдать книгу и карточку;
else (нет)
:Предложить бронь;
endif
else (нет)
:Отказать до погашения задолженности;
endif
else (нет)
:Отказать: билет недействителен;
endif
stop'''
D[19]='''state Создан
state Оплачен
state Собран
state Доставлен
state Отменён
[*] --> Создан : создать
Создан --> Оплачен : оплатить [платёж подтверждён]
Оплачен --> Собран : собрать [товар зарезервирован]
Собран --> Доставлен : вручить [получатель подтвердил]
Создан --> Отменён : отменить [не оплачен]
Оплачен --> Отменён : отменить [сборка не начата]\\n/ инициировать возврат
Доставлен --> [*]
Отменён --> [*]'''
D[20]='''state "Дневной режим" as Day {
state "Красный" as Red
state "Жёлтый перед зелёным" as Y1
state "Зелёный" as Green
state "Жёлтый перед красным" as Y2
[*] --> Red
Red --> Y1 : after(40 с)
Y1 --> Green : after(5 с)
Green --> Y2 : after(40 с)
Y2 --> Red : after(5 с)
}
state "Мигающий жёлтый" as Night
[*] --> Day
Day --> Night : ночнойРежим
Night --> Day : дневнойРежим
note bottom of Day
Y1 и Y2 имеют одинаковый цвет,
но разные последующие состояния.
end note'''
D[21]='''state Выпущена
state Активна {
state "Обычный режим" as Normal
state "Превышен лимит" as Limit
[*] --> Normal
Normal --> Limit : операция\\n[достигнут лимит]
Limit --> Normal : новыйПериод\\n/ обнулитьСчётчик
}
state Заблокирована
state Просрочена
state Закрыта
[*] --> Выпущена
Выпущена --> Активна : активировать [личность подтверждена]
Выпущена --> Просрочена : срокИстёк
Активна --> Заблокирована : заблокировать
Заблокирована --> Активна : разблокировать [проверка пройдена]
Активна --> Просрочена : срокИстёк
Заблокирована --> Просрочена : срокИстёк
Выпущена --> Закрыта : закрыть
Активна --> Закрыта : закрыть [нет обязательств]
Заблокирована --> Закрыта : закрыть [нет обязательств]
Просрочена --> Закрыта : закрыть [нет обязательств]
Закрыта --> [*]'''
D[22]='''state Ожидание
state "Движение вверх" as Up
state "Движение вниз" as Down
state "Двери открыты" as Open
Open : entry / открытьДвери(); запуститьТаймер()
Open : exit / закрытьДвери()
[*] --> Ожидание
Ожидание --> Up : вызов [цель > этаж && двери закрыты]
Ожидание --> Down : вызов [цель < этаж && двери закрыты]
Ожидание --> Open : вызов [цель == этаж]
Up --> Open : прибытие [этаж == цель] / остановить
Down --> Open : прибытие [этаж == цель] / остановить
Open --> Ожидание : таймер [проём свободен]
Open : препятствие / перезапуститьТаймер()'''
D[23]='''actor Пользователь as U
boundary ФормаВхода as F
control СерверАвторизации as A
database БазаДанных as DB
U -> F : ввести логин и пароль
F -> A : войти(логин, пароль)
activate A
A -> DB : получитьХеш(логин)
DB --> A : хеш / пользователь не найден
A -> A : проверить пароль стойким хешированием
alt пароль верный
A --> F : токен сессии
F --> U : успешный вход
else пароль неверный или пользователь не найден
A --> F : отказ
F --> U : неверные учётные данные
end
deactivate A'''
D[24]='''actor Клиент as C
participant Банкомат as ATM
participant Банк as B
participant Счёт as A
C -> ATM : снять(сумма)
ATM -> B : запроситьСнятие(сумма)
activate B
B -> A : проверитьИЗарезервировать(сумма)
alt достаточно средств
A --> B : резерв создан
B --> ATM : разрешить выдачу
ATM -> C : выдать наличные
ATM -> B : выдача подтверждена
B -> A : списать резерв
opt клиент запросил чек
ATM -> C : напечатать чек
end
else недостаточно средств
A --> B : отказ
B --> ATM : недостаточно средств
ATM --> C : показать отказ
end
deactivate B'''
D[25]='''actor Покупатель as C
participant Корзина as Cart
participant Склад as W
participant Оплата as P
C -> Cart : оформить()
create participant Заказ as O
Cart -> O : <<create>>(клиент)
loop для каждой позиции корзины
Cart -> O : добавитьПозицию(товар, количество)
O -> W : резервировать(товар, количество)
W --> O : резерв подтверждён
end
O -> P : оплатить(итог)
P --> O : платёж подтверждён
O -> O : статус = оплачен
O --> Cart : номер заказа
Cart --> C : подтверждение'''
D[26]='''top to bottom direction
object "пользователь:Пользователь" as U
object "форма:ФормаВхода" as F
object "авторизация:СерверАвторизации" as A
object "бд:БазаДанных" as DB
U --> F : 1: ввести(логин, пароль)
F --> A : 1.1: войти(логин, пароль)
A --> DB : 1.1.1: получитьХеш(логин)
DB --> A : 1.1.2: вернутьХеш()
A --> A : 1.1.3: проверитьПароль()
A --> F : 1.1.4 [верно]: токен\\n1.1.4 [иначе]: отказ
F --> U : 1.2: показатьРезультат()'''
D[27]='''actor Отправитель as S
participant Клиент as C
participant Сервер as V
actor Получатель as R
S -> C : отправить текст
C ->> V : сообщение(id, текст)
par доставка
V ->> R : новое сообщение(id, текст)
R ->> V : подтверждение доставки(id)
else сохранение
V -> V : сохранитьВИстории(id, текст)
end
V ->> C : статус(id, доставлено)
note over C,V
Открытые наконечники: асинхронные сообщения.
id позволяет распознавать повторы.
end note'''
D[28]='''robust "Светофор для машин" as C
robust "Светофор для пешеходов" as P
@0
C is Зелёный
P is Красный
@40
C is Жёлтый
@45
C is Красный
P is Зелёный
@90
C is Зелёный
P is Красный
@0 <-> @40 : 40 с
@40 <-> @45 : 5 с
@45 <-> @90 : 45 с'''
D[29]='''robust "Дверца" as D
robust "Магнетрон" as M
robust "Таймер" as T
scale 5 as 60 pixels
@0
D is Открыта
M is Выключен
T is Ожидание
@1
D is Закрыта
@2
M is Включён
T is Отсчёт
@62
M is Выключен
T is Сигнал
@63
T is Ожидание
@2 <-> @62 : {60 с}
'''
D[30]='''robust "Кнопка вызова" as B
robust "Лифт" as L
robust "Двери" as D
scale 5 as 100 pixels
@0
B is Нажата
L is Движение
D is Закрыты
B -> L : вызов
@1
B is Отпущена
@20
L is НаЭтаже
D is Открыты
@25
D is Закрыты
@30
L is Ожидание
@0 <-> @20 : {не более 30 с}
@20 <-> @25 : {не менее 5 с}'''
for n,body in D.items():
    content='@startuml\n!pragma layout smetana\nskinparam backgroundColor white\nskinparam defaultFontName Arial\nskinparam defaultFontSize 16\nskinparam classAttributeIconSize 0\nskinparam shadowing false\nskinparam dpi 150\nskinparam ArrowColor #334155\nskinparam classBackgroundColor #EFF6FF\nskinparam stateBackgroundColor #EFF6FF\nskinparam activityBackgroundColor #EFF6FF\nhide empty members\ntitle Билет '+str(n)+'\n'+body+'\n@enduml\n'
    (P/f'{n:02d}.puml').write_text(content,encoding='utf-8')
print('30 исходников диаграмм созданы')
