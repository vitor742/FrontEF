function changeDivAdd() {
    let divDefault = document.getElementById("defaultDivProdutos");
    let divAddProduto = document.getElementById("addDivProdutos");
    let divSearchProduto = document.getElementById("searchDivProdutos");
    let addButton = document.getElementById("addProduto");
    let searchButton = document.getElementById("searchProduto");

    
        divDefault.style.display = "none";
        divAddProduto.style.display = "flex";
        divSearchProduto.style.display = "none";
        addButton.style.backgroundColor = "#597cf9";
        searchButton.style.backgroundColor = "#e1deff"

}

function changeDivSearch() {
    let divDefault = document.getElementById("defaultDivProdutos");
    let divAddProduto = document.getElementById("addDivProdutos");
    let divSearchProduto = document.getElementById("searchDivProdutos");
    let searchButton = document.getElementById("searchProduto");
    let addButton = document.getElementById("addProduto");

        divDefault.style.display = "none";
        divAddProduto.style.display = "none";
        divSearchProduto.style.display = "flex";
        searchButton.style.backgroundColor = "#597cf9";
        addButton.style.backgroundColor = "#e1deff"
        
}