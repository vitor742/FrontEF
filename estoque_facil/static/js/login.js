import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.18.0/firebase-app.js';
import { getFirestore, collection, query, where, getDocs } from 'https://www.gstatic.com/firebasejs/9.18.0/firebase-firestore.js';
import { getAuth} from 'https://www.gstatic.com/firebasejs/9.18.0/firebase-auth.js';

const firebaseConfig = {
    apiKey: "AIzaSyB-gb6WNxu7_stWtEmKPEcO17jr_h3C1cM",
    authDomain: "estoquefacil-7b03b.firebaseapp.com",
    projectId: "estoquefacil-7b03b",
    storageBucket: "estoquefacil-7b03b.firebasestorage.app",
    messagingSenderId: "201462826581",
    appId: "1:201462826581:web:d10a08a1380073fdcfb6dc"
  };

// Inicializa o Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

document.getElementById('loginForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    const username = document.getElementById('username').value;
    const accessKey = document.getElementById('access_key').value;

    try {
        // Consulta ao Firestore para verificar as credenciais
        const usersRef = collection(db, 'clients');
        const q = query(usersRef, where('username', '==', username), where('access_key', '==', accessKey));
        const querySnapshot = await getDocs(q);

        if (!querySnapshot.empty) {
            console.log("Login bem-sucedido!");
            alert("Login bem-sucedido!");
            window.location.href = "/dashboard";  // Exemplo de redirecionamento
        } else {
            console.log("Credenciais inválidas.");
            alert("Credenciais inválidas.");
        }
    } catch (error) {
        console.log("Erro ao tentar autenticar:", error);
        alert("Erro ao tentar fazer login.");
    }
});