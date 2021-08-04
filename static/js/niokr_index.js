const coverTemplate = `<div class="card-custom-img"
style="background-image: url(<%-cover%>)"
></div>`;
const coverHexTemplate = `<div class="card-custom-img"
style="background-color: <%-hexcolor%>"
></div>`;
const logoTemplate = `<img class="img-fluid" src="<%-photo%>"/>`;
const logoDefaultTemplate = `<img class="img-fluid"
src="http://res.cloudinary.com/d3/image/upload/c_pad,g_center,h_200,q_auto:eco,w_200/bootstrap-logo_u3c8dx.jpg"
/>`;
const template = `
<div class="col-md-6 col-lg-4 pb-3 col-10 ms-5 ms-md-0">
<div
  class="card card-custom bg-white border-white border-0"
  style="height: 450px"
>
   <%=cover%>
  <div class="card-custom-avatar">
    <%=photo%>
  </div>
  <div class="card-body" style="overflow-y: auto">
    <h4 class="card-title"><%-theme%></h4>
    <small>от <a href="#"><%-user%></h4></a></small>
    <p class="card-text"><%-annotation%></p>
  </div>
  <div
    class="card-footer"
    style="background: inherit; border-color: inherit"
  >
    <div class="d-flex justify-content-between mb-2">
      <div class="p-2 flex-grow-1"><span class="fa fa-star checked"></span> <%-rating%></div>
      <div class="p-2"><a href="/niokr_projects/<%-pk%>" class="btn btn-outline-dark">Подробнее</a></div>
      <div class="p-2"><a href="<%-site%>" target="_blank" class="btn btn-outline-dark ">Сайт проекта</a></div>
    </div>
  </div>
</div>
</div>`;

const projectDates = [];

const url = "/api/niokr";
function getQuery(date = null) {
  const theme = $("#theme").val();
  const user = $("#user").val();
  const rating = $("#rating").val();
  axios
    .get(url, {
      params: {
        search: theme,
        user: user,
        date: date,
        ordering: rating
      },
    })
    .then(function (response) {
      $(".row.pt-5").html("");
      response.data.forEach((el) => {
        if (el.cover) {
          el.cover = _.template(coverTemplate)({ cover: el.cover });
        } else {
          el.cover = _.template(coverHexTemplate)({ hexcolor: el.hex_color });
        }
        if (el.responsible) {
            el.photo = _.template(logoTemplate)({
              photo: el.responsible,
            });
        } else {
            el.photo = logoDefaultTemplate;
          }
        const html = _.template(template)({
          cover: el.cover,
          pk: el.pk,
          photo: el.photo,
          site: el.site,
          theme: el.theme,
          user: el.user,
          annotation: el.annotation,
          rating: el.rating,
        });
        $(".row.pt-5").html($(".row.pt-5").html() + html);
      });
    })
    .catch(function (error) {
      console.log(error);
    });
    $(".pagination.justify-content-center").remove()
}

$("#theme").keyup(function () {
  getQuery();
});

$("#user").change(function () {
  getQuery();
});

$("#rating").change(function () {
  getQuery();
});

$(document).ready(async function () {
  const urlP = "/api/niokr_project-dates";
  await axios.get(urlP).then((res) => {
    res.data.dates.forEach((element) => {
      projectDates.push(element);
    });
  });

  $("#datepicker").datepicker({
    onRenderCell: function (date, cellType) {
      const year = String(date.getFullYear());
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");
      const currentDate = year + "-" + month + "-" + day;
      if (projectDates.indexOf(currentDate) != -1) {
        return {
          html: `<span style="color: #4EB5E6;">${date.getDate()}</span>`,
        };
      }
    },
    onSelect: function onSelect(fd, date) {
      const year = String(date.getFullYear());
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");
      const currentDate = year + "-" + month + "-" + day;
      getQuery(currentDate)
    },
  });
});
