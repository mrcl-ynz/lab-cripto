// ==UserScript==
// @name         Lab 4 Cripto
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Script para el laboratorio 4 de Criptografía y Seguridad en Redes
// @author       You
// @match        https://cripto.tiiny.site
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// ==/UserScript==

'use strict';

const retrieve_key = () => document.querySelector("p").innerText
         .split(". ")
         .map((x) => x[0])
         .join("");

const retrieve_messages = () => Array
    .from(document.querySelectorAll("[class^=M]"))
    .map(e => e.id);

const decrypt_message = (message, key) => CryptoJS.TripleDES.decrypt(
        { ciphertext: CryptoJS.enc.Base64.parse(message) },
        CryptoJS.enc.Utf8.parse(key),
        { mode: CryptoJS.mode.ECB }
    ).toString(CryptoJS.enc.Utf8);

(() => {
    let key = retrieve_key();

    let messages = retrieve_messages();

    console.log(`La llave es: ${key}`)
    console.log(`Los mensajes cifrados son: ${messages.length}`);

     messages.forEach((m) => {
            let decrypted = decrypt_message(m, key);

            console.log(`${m} ${decrypted}`);
            document.getElementById(m).innerText = decrypted;
        });
})();
