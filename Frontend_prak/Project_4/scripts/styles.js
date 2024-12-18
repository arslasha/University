// Получаем элемент иконки редактирования профиля
const editProfileIcon = document.querySelector('.profile__editor');
// Получаем элемент иконки добавления места
const addCardIcon = document.querySelector('.profile__add-mesto');
// Получаем popup редактирования профиля
const popupProfile = document.querySelector('#profile-popup');
// Получаем popup добавления карточки
const popupCards = document.querySelector('#cards-popup');
// Получаем popup увеличения картинки
const popupImageZoom = document.querySelector('#image-popup');
// Получаем элемент иконки закрытия popup редактирования профиля
const popupProfileCloseIcon = popupProfile.querySelector('.popup__close');
// Получаем элемент иконки закрытия popup добавления карточки
const popupCardsCloseIcon = popupCards.querySelector('.popup__close');
// Получаем элемент иконки закрытия popup увеличения картинки
const popupImageZoomCloseIcon = popupImageZoom.querySelector('.popup__close');
// Получаем имя профиля
const profileName = document.querySelector('.profile__name');
// Получаем описание профиля
const profileDescription = document.querySelector('.profile__description');
// Получаем input имени
const nameInput = popupProfile.querySelector('.popup__input_item_name');
// Получаем input названия карточки
const nameCardInput = popupCards.querySelector('.popup__input_item_name');
// Получаем input описания
const descriptionInput = popupProfile.querySelector('.popup__input_item_description');
// Получаем input ссылки на изображение карточки
const linkCardInput = popupCards.querySelector('.popup__input_item_description');
// Получаем секцию хранения карточек
const cardsArea = document.querySelector('.cards');

// Функция открытия popup
const popupOpen = function (popupName) {
  popupName.classList.add('popup_opened');  // Добавляет класс 'popup_opened' для отображения попапа
  nameInput.value = profileName.textContent;  // Заполняет поле ввода с именем значением из профиля
  descriptionInput.value = profileDescription.textContent;  // Заполняет поле ввода с описанием значением из профиля
}

// Функция закрытия popup
const popupClose = function (popupName) {
  popupName.classList.remove('popup_opened');  // Убирает класс 'popup_opened', скрывая попап
}

// Функция добавления карточки
const addCards = function (name, link) {
  const contentCardTemplate = document.querySelector('#card-template').content;  // Находим шаблон карточки в HTML
  const copyCardTemplate = contentCardTemplate.querySelector('.cards__item').cloneNode(true);  // Клонируем шаблон карточки

  copyCardTemplate.querySelector('.cards__description').textContent = name;  // Заполняем описание карточки
  copyCardTemplate.querySelector('.cards__image').src = link;  // Заполняем ссылку на изображение

  // Добавляем возможность лайкать карточку
  copyCardTemplate.querySelector('.cards__like').addEventListener('click', function (evt) {
    evt.target.classList.toggle('cards__like_active');  // Переключаем класс активности лайка при клике
  });
  
  // Добавляем возможность удалять карточку по клику
  copyCardTemplate.querySelector('.cards__delete').addEventListener('click', function (evt) {
    evt.target.closest('.cards__item').remove();  // Удаляет карточку, кликнув по кнопке удаления
  });
  
  // Добавляем возможность увеличения картинки при клике
  const getZoomImages = function () {
    popupImageZoom.querySelector('.popup__description').textContent = name;  // Заполняем описание в попапе увеличенной картинки
    popupImageZoom.querySelector('.popup__image').src = link;  // Заполняем изображение в попапе увеличенной картинки
    popupOpen(popupImageZoom);  // Открываем попап с увеличенной картинкой
  }

  copyCardTemplate.querySelector('.cards__image').addEventListener('click', getZoomImages);  // При клике на изображение открывается увеличенная версия

  return copyCardTemplate;  // Возвращаем готовую карточку
}

// Функция сохранения карточек
const integrationCard = function (evt) {
  evt.preventDefault();  // Предотвращает стандартное поведение формы (перезагрузку страницы)
  cardsArea.prepend(addCards(nameCardInput.value, linkCardInput.value));  // Добавляем новую карточку в начало списка
  popupClose(popupCards);  // Закрываем попап добавления карточки
}

// Функция наполнения страницы начальными карточками
const integrationInitialCards = function () {
  initialCards.forEach(function (card) {
    cardsArea.append(addCards(card.name, card.link));  // Для каждой начальной карточки добавляем её на страницу
  });
}

// Вызываем функцию для добавления начальных карточек при загрузке страницы
integrationInitialCards();  // Заполняем страницу карточками, переданными в initialCards

// Функция сохранения введённых в форму данных (имени и описания)
const formSubmitHandler = function (evt) {
  evt.preventDefault();  // Предотвращаем перезагрузку страницы при отправке формы
  profileName.textContent = nameInput.value;  // Обновляем имя в профиле значением из поля ввода
  profileDescription.textContent = descriptionInput.value;  // Обновляем описание в профиле значением из поля ввода
  popupClose(popupProfile);  // Закрываем попап редактирования профиля
}

// Открываем popup редактирования профиля
editProfileIcon.addEventListener('click', () => popupOpen(popupProfile));  // При клике на иконку редактирования профиля открывается попап редактирования

// Открываем popup добавления карточки
addCardIcon.addEventListener('click', () => popupOpen(popupCards));  // При клике на иконку добавления карточки открывается попап для добавления

// Закрываем popup редактирования профиля
popupProfileCloseIcon.addEventListener('click', () => popupClose(popupProfile));  // При клике на иконку закрытия попапа редактирования профиля закрывается попап

// Закрываем popup добавления карточки
popupCardsCloseIcon.addEventListener('click', () => popupClose(popupCards));  // При клике на иконку закрытия попапа добавления карточки закрывается попап

// Закрываем popup увеличения изображения
popupImageZoomCloseIcon.addEventListener('click', () => popupClose(popupImageZoom));  // При клике на иконку закрытия попапа увеличенной картинки закрывается попап

// Обновляем данные формы при нажатии кнопки сохранения
popupProfile.addEventListener('submit', formSubmitHandler);  // При отправке формы профиля сохраняются данные и попап закрывается

// Обновляем данные формы при нажатии кнопки добавления карточки
popupCards.addEventListener('submit', integrationCard);  // При отправке формы добавления карточки добавляется новая карточка и попап закрывается
