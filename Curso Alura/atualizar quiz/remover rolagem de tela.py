import pyautogui
import clipboard
"""
para este programa funcionar corretamente o usuario deve estar com o blog aberto
na area esquerda do pc e a um zoom de 100% e o editor do blog no modo edicao script
e na caixa de pesquisa deve estar o nome quizz... a referencia de entrada para o arquivo -e o traco no exemplo do quiz de matematica
"""
SCRIPT_ANTIGO = 'function rolarTelaResultado(){var e=window.document.querySelector("a#ancora-para-mostrar").offsetTop;window.scroll({top:e,behavior:"smooth"})}function rolarTelaFinal(){let e=0;0==window.document.querySelector("div#questao-1 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-1A").offsetTop:0==window.document.querySelector("div#questao-2 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-2A").offsetTop:0==window.document.querySelector("div#questao-3 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-3A").offsetTop:0==window.document.querySelector("div#questao-4 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-4A").offsetTop:0==window.document.querySelector("div#questao-5 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-5A").offsetTop:0==window.document.querySelector("div#questao-6 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-6A").offsetTop:0==window.document.querySelector("div#questao-7 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-7A").offsetTop:0==window.document.querySelector("div#questao-8 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-8A").offsetTop:0==window.document.querySelector("div#questao-9 button.botoes-questoes-quiz").disabled?e=window.document.querySelector("a#questao-9A").offsetTop:0==window.document.querySelector("div#questao-10 button.botoes-questoes-quiz").disabled&&(e=window.document.querySelector("a#questao-10A").offsetTop),window.scroll({top:e,behavior:"smooth"})}function rolarTela(e){let o=0,t="";switch(e){case"questao-1":o=window.document.querySelector("a#questao-2A").offsetTop,t="questao-2";break;case"questao-2":o=window.document.querySelector("a#questao-3A").offsetTop,t="questao-3";break;case"questao-3":o=window.document.querySelector("a#questao-4A").offsetTop,t="questao-4";break;case"questao-4":o=window.document.querySelector("a#questao-5A").offsetTop,t="questao-5";break;case"questao-5":o=window.document.querySelector("a#questao-6A").offsetTop,t="questao-6";break;case"questao-6":o=window.document.querySelector("a#questao-7A").offsetTop,t="questao-7";break;case"questao-7":o=window.document.querySelector("a#questao-8A").offsetTop,t="questao-8";break;case"questao-8":o=window.document.querySelector("a#questao-9A").offsetTop,t="questao-9";break;case"questao-9":o=window.document.querySelector("a#questao-10A").offsetTop,t="questao-10"}0==window.document.querySelector("div#"+t+" button.botoes-questoes-quiz").disabled&&window.scroll({top:o,behavior:"smooth"})}function marcado(e,o){let t=window.document.querySelectorAll("div#"+e+" button.botoes-questoes-quiz");for(i=0;i<4;i++){var u;1==t[i].value?(t[i].style.background="rgba(16, 221, 50, 0.849)",t[i].disabled="true",o==i&&(u=window.document.querySelector("button#nume-acertos").value,u=Number(u),++u,window.document.querySelector("button#nume-acertos").value=u)):(i==o?t[i].style.background=" rgba(240, 12, 12, 0.68)":(t[i].classList.remove("botoes-questoes-quiz"),t[i].classList.add("botoes-questoes-quiz-desab")),t[i].disabled="true")}var a=window.document.querySelector("button#quest-resp").value+="a";if("aaaaaaaaa"==a)setTimeout(function(){rolarTelaFinal()},190);else if("aaaaaaaaaa"==a){a=window.document.querySelector("button#nume-acertos").value,a=Number(a);let e=window.document.querySelectorAll("div#exibir-resultados div");e[a].classList.add("ativo"),setTimeout(function(){rolarTelaResultado()},190)}else"questao-10"!=e&&setTimeout(function(){rolarTela(e)},190)}'
SCRIPT_ATUALIZADO = 'function rolarTelaResultado(){var e=window.document.querySelector("a#ancora-para-mostrar").offsetTop;window.scroll({top:e,behavior:"smooth"})}function marcado(o,e){let t=window.document.querySelectorAll("div#"+o+" button.botoes-questoes-quiz");for(i=0;i<4;i++){var a;1==t[i].value?(t[i].style.background="rgba(16, 221, 50, 0.849)",t[i].disabled="true",e==i&&(a=window.document.querySelector("button#nume-acertos").value,a=Number(a),++a,window.document.querySelector("button#nume-acertos").value=a)):(i==e?t[i].style.background=" rgba(240, 12, 12, 0.68)":(t[i].classList.remove("botoes-questoes-quiz"),t[i].classList.add("botoes-questoes-quiz-desab")),t[i].disabled="true")}if("aaaaaaaaaa"==(window.document.querySelector("button#quest-resp").value+="a")){o=window.document.querySelector("button#nume-acertos").value,o=Number(o);let e=window.document.querySelectorAll("div#exibir-resultados div");e[o].classList.add("ativo"),setTimeout(function(){rolarTelaResultado()},190)}}'
#id_entrar_quiz = (x=376, y=218)
# id_entrar_texto = (x=364, y=422)
# id_confirmar = (x=682, y=238)
# id_sair = (x=107, y=171)
def confirmar_entrada_no_blog():
    """
    :return: boolean
    """
    if (pyautogui.locateCenterOnScreen('CONFIRMACAO_BLOG.png') != None or pyautogui.locateCenterOnScreen('CONFIRMACAO_BLOG2.png') != None) or pyautogui.locateCenterOnScreen('CONFIRMACAO_BLOG3.png') == None:
        return True
    else:
        return False

def confirmar_saida_blog():
    """
    :return:boolean
    """
    if pyautogui.locateOnScreen('CONFIRMACAO_BLOG_SAIDA.png') != None:
        return True

    else:
        return False

def confirmar_edicao_salva():
    """
    :return:boolean
    """
    if pyautogui.locateOnScreen('CONFIRMACAO_SALVO.png') != None:
        return True

    else:
        return False

def atualizar_script_para_area_de_transferencia():
    pagina = clipboard.paste()
    #atualiza script e erro de estado no div
    pagina = pagina.replace('<span class="estado-aluno">Muito crítico</span>','<span class="estado-aluno" face="Arial,Helvetica,sans-serif" style="color: red; font-size: 15pt; font-weight: 700; margin-left: 55px;">Muito crítico</span>')
    clipboard.copy(pagina.replace(SCRIPT_ANTIGO, SCRIPT_ATUALIZADO))


if pyautogui.confirm('O programa esta pronto para iniciar!') != 'OK':
    exit()

pyautogui.sleep(1)

while True:
    #entrar no post
    while not confirmar_saida_blog():
        print('Aguardando confirmacao de entrada no menu do blog')
    # pyautogui.scroll(-2, x=360, y=284)
    # pyautogui.sleep(0.3)
    # pyautogui.click(x=350, y=218)
    print('CLIQUE')

    #editar post
    pyautogui.sleep(4)
    while not confirmar_entrada_no_blog():
        print('Aguardando confirmação de entrada no post')
    #entrando no texto e passando para o programa editar
    pyautogui.click(x=364, y=422)
    pyautogui.sleep(0.1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.sleep(1)
    pyautogui.hotkey('ctrl','c')
    pyautogui.sleep(1)
    a = clipboard.paste()
    print(a[75:150])
    pyautogui.sleep(1)
    atualizar_script_para_area_de_transferencia()
    pyautogui.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.1)
    #salvar
    pyautogui.click(x=682, y=238)

    while not confirmar_edicao_salva():
        print('Aguardando confirmacao de edição salva')
    #sair do post
    pyautogui.click(x=107, y=171)




