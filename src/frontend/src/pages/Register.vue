<template>
    <div>
      <h1>Register</h1>
      <form @submit.prevent="register" >

        <div>
          <label for="email">Email:</label>
          <input v-model="email" id="email" type="email" required>
        </div>

        <div>
          <label for="username">Username:</label>
          <input v-model="username" id="username" type="username" required>
        </div>

        <div>
          <label for="password">Password:</label>
          <input v-model="password" id="password" type="password" required>
        </div>

        <br>

        User Role:
        <input type="radio" name="user_role" v-model="role" value="PAR" checked="checked">
        <label for="PAR">Participant</label>
        <input type="radio" name="user_role" v-model="role" value="ORG">
        <label for="ORG">Organizer</label>

        <br><br>
        <button type="submit">Register</button>

      </form>
      <p v-if="error">{{ error }}</p>
      <p v-if="success">{{ success }}</p>
    </div>
  </template>
  

  
  <script>
  import { getCSRFToken } from '../store/auth'
  
  export default {
    data() {
      return {
        email: '',
        username: '',
        password: '',
        role: 'PAR',
        error: '',
        success: ''
      }
    },
    methods: {
      async register() {
        try {
          const response = await fetch('http://localhost:8000/auth/api/register', {
            method: 'POST',
             headers: {
                      'Content-Type': 'application/json',
                      'X-CSRFToken': getCSRFToken()
                  },
            body: JSON.stringify({
              email: this.email,
              username: this.username,
              password: this.password,
              role: this.role
            }),
            credentials: 'include'
          })
          const data = await response.json()
          if (response.ok) {
            this.success = 'Registration successful! Please log in.'
            setTimeout(() => {
              this.$router.push('/login')
            }, 1000)
          } else {
            this.error = data.error || 'Registration failed'
          }
        } catch (err) {
          this.error = 'An error occurred during registration: ' + err
        }
      }
    }
  }

  </script>
  
