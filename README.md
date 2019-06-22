# segmentation_and_quantification_angiogenesis

Foram feitos 3 algoritmos. 1 para pegar o valor de RGB onde o mouse percorre a imagem (pegarcor.py);
Um para segmentação dos vasos sanguíneos (segmentacao.py) disponibilizado originalmente em http://github.com/getsanjeev/retina-features   ;
Um para quantificação dos pixels pretos, correspondentes à área que os vasos sanguíneos ocupam (contando.py).

Todas as imagens de entrada e saída encontram-se aqui.

Temos as imagens originais de entrada (retinas_normais) - disponibilizadas em https://www5.cs.fau.de/research/data/fundus-images/
Temos as imagens modificadas - simulando um banco de dados sintéticos de imagens após o processo de angiogênese (retinas_apos_angiogenese)
Temos as imagens de saída referentes às segmentações ao extrair o canal verde (saida_normais  &   saida_apos_angiogenese)
Por sim, temos as imagens de saída referente às segmentações ao extrair o canal azul e vermelho (segmentacao_canal_azul & segmentacao_canal_vermelho)
como forma de concluir que nesses dois canais a segmentação não é eficiente.
 
