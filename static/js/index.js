const template = `
<div class="col-md-6 col-lg-4 pb-3">
<div
  class="card card-custom bg-white border-white border-0"
  style="height: 450px"
>
  <div class="card-custom-img" style="background-color: <%-hexcolor%>;"></div>
  <div class="card-custom-avatar">
    <img
      class="img-fluid"
      src="http://res.cloudinary.com/d3/image/upload/c_pad,g_center,h_200,q_auto:eco,w_200/bootstrap-logo_u3c8dx.jpg"
    />
  </div>
  <div class="card-body" style="overflow-y: auto">
    <h4 class="card-title"><%-name%></h4>
    <small>от <a href="#"><%-user%></h4></a></small>
    <p class="card-text"><%-note%></p>
  </div>
  <div
    class="card-footer"
    style="background: inherit; border-color: inherit"
  >
    <div class="d-flex justify-content-between mb-2">
      <div class="p-2 flex-grow-1"><span class="fa fa-star checked"></span> <%-rating%></div>
      <div class="p-2"><a href="/projects/<%-pk%>" class="btn btn-outline-dark">Подробнее</a></div>
      <div class="p-2"><a href="<%-site%>" target="_blank" class="btn btn-outline-dark ">Сайт проекта</a></div>
    </div>
  </div>
</div>
</div>`

const url = "/api/projects";
function getQuery() {
    const name = $("#name").val();
    const user = $("#user").val();
    const responsible = $("#responsible").val();
    axios.get(url, { params: { search: name, user: user, responsible: responsible } })
        .then(function (response) {
            $(".row.pt-5").html("")
            response.data.forEach(el => {
                const html = _.template(template)({
                    hexcolor: el.hex_color,
                    pk: el.pk,
                    site: el.site,
                    name: el.name,
                    user: el.user,
                    note: el.note,
                    rating: el.rating,
                })
                $(".row.pt-5").html($(".row.pt-5").html() + html)
            });
        })
        .catch(function (error) {
            console.log(error);
        })
}
$('#name').keyup(function () {
    getQuery()
});
$('#user').change(function () {
    getQuery()
});
$('#responsible').change(function () {
    getQuery()
});