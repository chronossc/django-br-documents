jQuery(document).ready(function($) {
    mask = $("input[data-cpf-mask]").data('cpf-mask');
    $("input[data-cpf-mask]").mask(mask);
});
