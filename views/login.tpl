<link rel="stylesheet" href="static/css/login.css">
%rebase('base.tpl', title = 'Login')
<div class="login-page">
  <div class="form">
    <form class="login-form">
      <input type="text" placeholder="username"/>
      <input type="password" placeholder="password"/>
      <button>login</button>
      <p class="message">Not registered? <a href="/createAccount">Create an account</a></p>
    </form>
  </div>
</div>
