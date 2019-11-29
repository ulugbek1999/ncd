function dateMyFormat(date) {
    var elem = date.split('.');
    var newMyDate = elem[2] + '-' + elem[1] + '-' + elem[0];
    //console.log(newMyDate);
    if(date){
        return newMyDate;
    }else{
        return '';
    }
}
$(function () {

    $("#root-employee-update4").click(function (event) {
        event.preventDefault();

        function b64toBlob(b64Data, contentType, sliceSize) {
            contentType = contentType || '';
            sliceSize = sliceSize || 512;

            var byteCharacters = atob(b64Data);
            var byteArrays = [];

            for (var offset = 0; offset < byteCharacters.length; offset += sliceSize) {
                var slice = byteCharacters.slice(offset, offset + sliceSize);

                var byteNumbers = new Array(slice.length);
                for (var i = 0; i < slice.length; i++) {
                    byteNumbers[i] = slice.charCodeAt(i);
                }

                var byteArray = new Uint8Array(byteNumbers);

                byteArrays.push(byteArray);
            }

            var blob = new Blob(byteArrays, {type: contentType});
            return blob;
        }

        let $formData = new FormData();
        let url = $(this).data("url");

        $formData.append("is_ready_for_university", $("input[name='to_university']:checked").val() == "true");  
        $formData.append("hobby_ru", $("input[name='hobby']").val());
        $formData.append("other_ru", $("textarea[name='other']").val());
        $formData.append("country", $("select[name='des_countries']").val());

        var level = $("input[name='level']:checked").val()

        switch (level) {
            case 'is_employee':
                $formData.append("is_employee", true);
                $formData.append("is_young_talent", false);
                $formData.append("is_student", false);
                break;
            case 'is_young_talent':
                $formData.append("is_employee", false);
                $formData.append("is_young_talent", true);
                $formData.append("is_student", false);
                break;
            case 'is_student':
                $formData.append("is_student", true);
                $formData.append("is_employee", false);
                $formData.append("is_young_talent", false);
                break;
            default:
                break;
        }
        // let countries = $("input[name='des_countries']:checked");
        //
        // for (let i = 0; i < countries.length; i++) {
        //     $formData.append("country", countries[i].value);
        // }
        if(scanCheck){
           var ImageURL  = $("#fingerPrint").attr('value');
           var block = ImageURL.split(";");
           // Get the content type
           var contentType = 'image/jpg';// In this case "image/gif"
           // get the real base64 content of the file
           var realData = block[1].split(",")[1];// In this case "iVBORw0KGg...."

           // Convert to blob
           var blob = b64toBlob(realData, contentType);
           var fingerPrint = new File([blob], 'fingerPrint.jpg', {type: contentType});

           formData.append("fingerprint", fingerPrint);
        }

        $.ajax({
            url: url,
            data: $formData,
            type: "PUT",
            processData: false,
            contentType: false,
            success: function (data) {
                // $(".holder").removeClass("active");
                var x = document.getElementById("mainSuccess");
                x.className = "show";
                setTimeout(function(){
                    x.className = x.className.replace("show", "");
                    location.reload();
                }, 1500);
            },
            error: function (data) {
                // $(".holder").removeClass("active");
                var x = document.getElementById("mainError");

                x.className = "show";
                setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
            },
        })
    });

});
