function addTratamento(){
    var nome = document.getElementByName("nome").value;
    var user = document.getElementByName("username").value;
    var senha = document.getElementByName("senha").value;
    var confSenha = document.getElementByName("confSenha").value;
    if (nome.length > 0){
        if (user.length > 0){
            if (senha.length > 0){
                if (confSenha.length >0){
                    if (senha == confSenha){
                        alert ("Cadastro realizado com sucesso");
                    }else{
                        alert ("Confirmar senha e Senha são diferentes");
                    }
                }else{
                    alert ("Falta prencher o campo confirmar Senha");
                }
            }else{
                alert ("Falta prencher o campo Senha");
            }
        }else{
            alert ("Falta prencher o campo Uusername");
        }
    }else{
        alert ("Falta prencher o campo Nome");
    }
}