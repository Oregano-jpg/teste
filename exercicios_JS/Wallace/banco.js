let saldo = 1000;

function consultarSaldo (){
    document.getElementById('mensagem').textContent= `Seu saldo é R$${saldo.toFixed(2)}`;
}
function sacar(){
    let valorDoSaque = parseFloat(document.getElementById('valorSaque').value);
    if( isNaN(valorDoSaque) || valorDoSaque <= 0){
        document.getElementById('mensagem').textContent= `Valor de saque invalido`;
        return;
    }
    if (saldo > valorDoSaque) {
        saldo-=valorDoSaque;
        document.getElementById('mensagem').textContent= `Saque realizado de R$${valorDoSaque.toFixed(2)} Novo Valor do saldo é R$${saldo.toFixed(2)} `;
    
    } else {
        document.getElementById('mensagem').textContent= `Saldo insuficiente para esse saque de R$${valorDoSaque.toFixed(2)} Novo Valor do saldo é R$${saldo.toFixed(2)}`;
    }
    document.getElementById('valorSaque').value = 0;

}
function depositar(){
    let valorDeposito = parseFloat(document.getElementById('valorDeposito').value);
    if( isNaN(valorDeposito) || valorDeposito <= 0){
        document.getElementById('mensagem').textContent= `Valor de Deposito invalido`;
        return;
    }else{
        saldo+= valorDeposito;
        document.getElementById('mensagem').textContent= `Deposito realizado de R$${valorDeposito.toFixed(2)}`;
        
    }
    document.getElementById('valorDeposito').value = 0;
}

function sair(){
    document.getElementById("mensagem").textContent = "Obrigado por utilizar nossos serviços.";
    saldo = 0

}