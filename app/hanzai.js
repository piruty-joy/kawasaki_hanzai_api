$(function () {
    function drawGraph(data) {
        var date = ['日付'];
        var akisu = ['空き巣'];
        var rojou = ['路上強盗'];
        var hittakuri = ['ひったくり'];
        var shajou = ['車上ねらい'];
        var jitensha = ['自転車盗'];
        $.each(data, function (i, val) {
            date.push(val.date);
            akisu.push(val.akisu);
            rojou.push(val.rojou);
            hittakuri.push(val.hittakuri);
            shajou.push(val.shajou);
            jitensha.push(val.jitensha);
        });
        var chart = c3.generate({
            bindto: '#chart',
            data: {
                x: '日付',
                columns: [
                    date,
                    akisu,
                    rojou,
                    hittakuri,
                    shajou,
                    jitensha
                ]
            },
            axis: {
                x: {
                    type: 'category',
                    tick: {
                        rotate: 75,
                        multiline: false
                    },
                    height: 130,
                    show: false
                },
                y: {
                    min: 0
                }
            }
        });
    }
    $('#update-graph').click(function () {
        var from = $('#from').val().replace(/-/g, '');
        var to = $('#to').val().replace(/-/g, '');
        $.ajax({
            url: 'http://localhost:5000/hanzai_between_dates',
            type: 'get',
            dataType: 'json',
            data: {
                from: from,
                to: to
            }
        })

            .done(function (data) {
                drawGraph(data);
            })
    });
    $('#graph-monthly').click(function () {
        $.ajax({
            url: 'http://localhost:5000/hanzai_monthly',
            type: 'get',
            dataType: 'json'
        })
            .done(function (data) {
                drawGraph(data);
            })
    });
    $.ajax({
        url: 'http://localhost:5000/hanzai',
        type: 'get',
        dataType: 'json'
    })
        .done(function (data) {
            drawGraph(data);
        })
});