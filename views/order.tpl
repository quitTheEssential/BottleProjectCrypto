<link rel="stylesheet" href="static/css/login.css">
% rebase('base.tpl', title = 'Order')
<div class="order-page">
  <div class="form">
    <form action="/order" method="post">
      <input type="text" placeholder="Quantity (like 0.05)" onkeyup="calc()" name="quantity" id="quantity" formmethod="post" required />
      <p>Cryptocurrency: {{!crypto}}</p>
      <input type="text" id="price" value="{{!prize}}" disabled>
      <select class="orderType" name="orderType" style="margin-bottom: 20px">
        <option value="buy">Buy</option>
        <option value="sell">Sell</option>
      </select>
      <input type="text" name="output" id="output" value="" placeholder="Amount" disabled>
      <button>Submit</button>
    </form>
  </div>
</div>
<script type="text/javascript">
  function calc() {
    var textValue1 = document.getElementById('quantity').value;
    var textValue2 = document.getElementById('price').value;

    document.getElementById('output').value = textValue1 * textValue2;
  }
</script>
