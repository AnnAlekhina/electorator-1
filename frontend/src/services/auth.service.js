import axios from 'axios'

const API_URL = 'http://localhost:8000/api/account/'

class AuthService {
  login(account) {
    return axios
      .post(API_URL + 'login', {
        snils: account.snils,
        password: account.password
      })
      .then(response => {
        console.log(response.data)
        if (response.data.jwt) {
          localStorage.setItem('account', JSON.stringify(response.data))
        }

        return response.data
      })
  }

  logout() {
    localStorage.removeItem('account')
  }
}

export default new AuthService()