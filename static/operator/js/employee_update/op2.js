$(function () {
    function readURL(avatar, input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            var avatar_item = '.' + avatar;
            reader.onload = function(e) {
                $(`${avatar_item} #passportPreview`).css('background-image', 'url('+e.target.result +')');
                $(`${avatar_item} #passportPreview`).hide();
                $(`${avatar_item} #passportPreview`).fadeIn(650);
                $(`${avatar_item} .avatar-upload__button`).fadeOut(650);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#photo_1ID").change(function() {
        readURL('photo_1ID', this);
    });
    $("#photo_2ID").change(function() {
        readURL('photo_2ID', this);
    });
    $("#photo_3ID").change(function() {
        readURL('photo_3ID', this);
    });
    $("#photo_4ID").change(function() {
        readURL('photo_4ID', this);
    });

    $("#root-employee-update2-submit").click(function (event) {
       event.preventDefault();
       let $formData = new FormData();
       let url = $(this).data("url");

       var appearance = $("input[name='appearance']:checked").val() || null
       var neatness = $("input[name='neatness']:checked").val() || null
       var skin = $("input[name='skin']:checked").val() || null
       var height = $("input[name='height']").val() || null
       var weight = $("input[name='weight']").val() || null
       var fatness = $("input[name='fatness']").val() || null
       var blood_group = $("input[name='blood_group']:checked").val() || null
       var blood_resus = $("input[name='blood_resus']:checked").val() || null
       var vision_l = $("input[name='vision_l']").val().replace(',', '.') || null
       var vision_r = $("input[name='vision_r']").val().replace(',', '.') || null
       var photo_1 = $("input[name='photo_1']")[0].files[0] || null
       var photo_2 = $("input[name='photo_2']")[0].files[0] || null
       var photo_3 = $("input[name='photo_3']")[0].files[0] || null
       var photo_4 = $("input[name='photo_4']")[0].files[0] || null


       $formData.append("appearance", appearance);
       
       $formData.append("neatness", neatness);
       $formData.append("skin", skin);
       $formData.append("height", height);
       $formData.append("weight", weight);
       $formData.append("fatness", fatness);
       $formData.append("blood_group", blood_group);
       $formData.append("blood_resus", blood_resus);
       $formData.append("vision_l", vision_l);
       $formData.append("vision_r", vision_r);
       $formData.append("photo_1", photo_1);
       $formData.append("photo_2", photo_2);
       $formData.append("photo_3", photo_3);
       $formData.append("photo_4", photo_4);

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
       });
   })
});
