$(document).ready(function () {
    alert("Cheating is bad!");

    function to_city() {
        var optionSelected = $('#subject').find("option:selected");
        var subject = optionSelected.text();

        var words = $('#search').val();

        sub_words = { 'subject': subject, 'words': words };

        $.ajax('/filter_ques', { method: 'GET', data: sub_words }).done(function (result) {
            console.log(result);
            $("#table>tbody").empty();
            if (result.length > 0) {
                for (var i = 0; i < result.length; i++) {
                    $("#table>tbody").append('<tr><td style="width: 2%;" rowspan="2">' + (i + 1) + '</td><td class="question">' + result[i].question + '</td></tr>');
                    $("#table>tbody").append('<tr><td class="answer">' + result[i].answer + '</td></tr >');
                };
            }
            else {
                $("#table>tbody").append('<tr><td class="answer"> No such question </td ></tr > ');
            }

        }).fail(function () {
            alert('Subject not available');
        });
    }

    $('#search').change(to_city);

    $('#search').click(to_city);

});
