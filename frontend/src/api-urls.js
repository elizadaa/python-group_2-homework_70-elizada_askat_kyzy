import axios from 'axios'

const BASE_URL = 'http://localhost:8000/api/v1';
const MOVIES_URL = '/movies/';
const CATEGORIES_URL = '/categories/';
const HALLS_URL = '/halls/';
const SHOWS_URL = '/shows/';
const LOGIN_URL = '/login/';
const REGISTER_URL = '/register/';
const USERS_URL = '/users/';
const REGISTER_ACTIVATE_URL = '/register/activate/';
const TOKEN_LOGIN_URL = '/token-login/';

const instance = axios.create({
    baseURL: BASE_URL
});

export {MOVIES_URL, HALLS_URL, CATEGORIES_URL, SHOWS_URL, BASE_URL, LOGIN_URL, REGISTER_URL, USERS_URL,
    REGISTER_ACTIVATE_URL, TOKEN_LOGIN_URL}

export default instance;