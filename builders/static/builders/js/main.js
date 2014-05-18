$(function () {
    // Activate the raty widget
    $('[data-raty]').raty({
        numberMax: 5,
        path: '/static/builders/vendor/raty/img',
        hints: [null] * 5,
        score: function() {
            return $(this).attr('data-raty-score');
        },
        readOnly: function() {
            return !$(this).is('[data-raty-rw]');
        },
        scoreName: function() {
            return $(this).attr('data-raty-name');
        },
    });
});
