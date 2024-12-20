/** Объект настроек для работы с API
 * @type {{headers: {authorization: string, "Content-Type": string}, serverURL: string}}
 */
export const apiSettings = {
  // Базовый URL сервера, куда будут отправляться запросы
  serverURL: 'https://mesto.nomoreparties.co/v1/frontend-st-cohort-201',
  headers: {
    // Токен авторизации для идентификации пользователя
    authorization: '44e0a939-1df4-4135-82f7-f4c1f6e4b2f3',
    // Указывает, что данные передаются в формате JSON
    'Content-Type': 'application/json'
  }
};

/**
 * Настройки валидации
 * @param {string} formSelector - класс формы
 * @param {string} inputSelector - класс инпута
 * @param {string} submitButtonSelector - класс кнопки отправки формы
 * @param {string} inactiveButtonClass - класс, к-рый делает кнопку отправки формы заблокированной
 * @param {string} inputErrorClass - класс, подсвечивающий поле с ошибками
 * @param {string} errorClass - класс, делающий ошибку видимой
 */
/** @type {Object} */
export const validationSettings = {
  // CSS-селектор формы, которую нужно валидировать
  formSelector: '.popup__form',
  // CSS-селектор для инпутов в форме
  inputSelector: '.popup__input',
  // CSS-селектор для кнопки отправки формы
  submitButtonSelector: '.popup__submit',
  // Класс, применяемый к кнопке отправки, чтобы сделать её неактивной
  inactiveButtonClass: 'popup__submit_disabled',
  // Класс, добавляемый инпутам при возникновении ошибки
  inputErrorClass: 'popup__input_type_error',
  // Класс, который делает текст ошибки видимым для пользователя
  errorClass: 'popup__error_visible'
};
