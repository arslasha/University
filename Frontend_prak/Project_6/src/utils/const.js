/** Объект настроек для работы с API
 * @type {{headers: {authorization: string, "Content-Type": string}, serverURL: string}}
 */
export const apiSettings = {
  // Базовый URL сервера, куда будут отправляться запросы
  serverURL: 'https://mesto.nomoreparties.co/v1/apf-cohort-202',
  headers: {
    // Токен авторизации для идентификации пользователя
    authorization: 'e6ad1120-aac6-4dfc-b513-df0ce9d53be0',
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
