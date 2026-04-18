var copy_btn = document.getElementById('copy_btn');
      var output_text = document.getElementById('output_text');
      
      copy_btn.addEventListener('click', copy_button_click);

      function copy_button_click(){
          navigator.clipboard.writeText(output_text.innerText);
          copy_btn.classList.remove("fa-copy" ,"fa-regular");       
          copy_btn.classList.add("fa-check", "fa-solid");
          setTimeout(() => {
            copy_btn.classList.remove("fa-check", "fa-solid");
            copy_btn.classList.add("fa-copy" ,"fa-regular");  
          }, 2500);
          

      }