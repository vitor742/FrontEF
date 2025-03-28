function changeDivAdd() {
    let divDefault = document.getElementById("defaultDivProdutos");
    let divAddProduto = document.getElementById("addDivProdutos");
    let divSearchProduto = document.getElementById("searchDivProdutos");
    
        divDefault.style.display = "none";
        divAddProduto.style.display = "flex";
        divSearchProduto.style.display = "none";

}

function changeDivSearch() {
    let divDefault = document.getElementById("defaultDivProdutos");
    let divAddProduto = document.getElementById("addDivProdutos");
    let divSearchProduto = document.getElementById("searchDivProdutos");

        divDefault.style.display = "none";
        divAddProduto.style.display = "none";
        divSearchProduto.style.display = "flex";
        
}