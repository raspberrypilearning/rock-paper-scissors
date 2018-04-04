## Turno do Computador

Agora é a vez do computador. You can use the `randint` function to generate a random number to decide between rock, paper and scissors.

+ Use `randint` para gerar um número aleatório para decidir se o computador escolheu rocha, papel ou tesoura.
    
    ![captura de tela](images/rps-randint.png)

+ Execute o seu script muitas vezes (você precisará digitar 'r', 'p' ou 's' a cada vez).
    
    Você deve ver que 'escolhido' é aleatoriamente definido como 1, 2 ou 3.

+ Digamos:
    
    + 1 = rock (r)
    + 2 = papel (p)
    + 3 = tesoura (s)
    
    Use `se` para verificar se o número escolhido é `1` (`==` é usado para ver se 2 coisas são iguais).
    
    ![captura de tela](images/rps-if-1.png)

+ O Python usa **recuo** (movendo o código para a direita) para mostrar qual código está dentro do `se`. You can either use two spaces (tap the spacebar twice) or tap the **tab key** (usually above CAPSLOCK on the keyboard.)
    
    Defina `computador` para 'r' dentro do `se` usando recuo:
    
    ![captura de tela](images/rps-indent.png)

+ Você pode adicionar uma verificação alternativa usando `elif` (abreviação de *else if*):
    
    ![captura de tela](images/rps-elif-2.png)
    
    Esta condição só será verificada se a primeira condição falhar (se o computador não tiver escolhido `1`)

+ E, finalmente, se o computador não escolheu `1` ou `2` , então ele deve ter escolhido `3`.
    
    Desta vez podemos usar `senão` , o que significa o contrário.
    
    ![captura de tela](images/rps-else-3.png)

+ Agora, em vez de imprimir o número aleatório que o computador escolheu, você pode imprimir a carta.
    
    ![captura de tela](images/rps-print-computer.png)
    
    Você pode excluir a linha `print (escolhida)`ou fazer com que o computador a ignore, adicionando um `#` no início da linha.

+ Teste seu código clicando em Executar e escolhendo sua opção.

+ Hmm, a escolha do computador é impressa em uma nova linha. Você pode corrigir isso adicionando `end = ''` após `vs`, que diz ao Python para terminar com um espaço em vez de uma nova linha.
    
    ![captura de tela](images/rps-same-line.png)

+ Jogue o jogo algumas vezes clicando em Executar e fazendo uma escolha.
    
    Por enquanto, você terá que descobrir quem ganhou a si mesmo. Em seguida, você adicionará o código Python para resolver isso.