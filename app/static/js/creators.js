function create_sidenav_link(name, icon_file_path, route_name=null) {            
    if (route_name == null) {
        route_name = name
    }

    route_name = `/${route_name}`

    let div = document.createElement("div")
    div.classList.add("link-nav")
    div.onclick = () => window.location = route_name
    if (route_name == window.location.pathname) {
        div.classList.add("macro-target-active")
    }

    let img = document.createElement("img")
    img.src = icon_file_path
    img.classList.add("icon-nav")

    let text = document.createTextNode(name)

    div.appendChild(img)
    div.appendChild(text)

    let link_container = document.querySelector("#sidenav_link_container")
    link_container.appendChild(div)
}


function create_navtab(name, target_name=null) {
    if (target_name == null) {
        target_name = name
    }
    target_name = "#" + target_name

    let div = document.createElement("div")
    div.classList.add("nav-tabs-item")
    
    div.onclick = () => {
        window.location = window.location.pathname + target_name
        try {
            document.querySelector(".nav-tab-item-selected").classList.remove("nav-tab-item-selected")
        } catch {}
        div.classList.add("nav-tab-item-selected")
    }

    url = window.location.href
    if (url.indexOf(target_name) != -1) {
        div.classList.add("nav-tab-item-selected")
    }

    let text = document.createTextNode(name)

    div.appendChild(text)

    let tabs_container = document.querySelector("#tabs_container")
    tabs_container.appendChild(div)
}


function create_filter(parent_id, specifications, selector_id) {

    specifications = specifications.replace(/'/gi, '"')
    specifications = JSON.parse(specifications)

    drop_id = parent_id + "_drop"
    btn_id = parent_id + "_btn"
    
    let filter_btn = document.createElement("div")
    filter_btn.id = btn_id
    filter_btn.classList.add("row", "dropdown-btn", "my-4")
    filter_btn.onclick = () => active_dropdown(btn_id, drop_id)

    let btn_title = document.createElement("h4")
    btn_title.classList.add("col-2")
    btn_title.innerText = "Filtros:"

    let arrow_img = document.createElement("img")
    arrow_img.src = "static/img/icons/seta_filtro.png"
    arrow_img.classList.add("arrow-dropdown")

    let btn_arrow = document.createElement("div")
    btn_arrow.classList.add("col-1", "offset-9")

    btn_arrow.appendChild(arrow_img)
    filter_btn.appendChild(btn_title)
    filter_btn.appendChild(btn_arrow)

    let filter_drop = document.createElement("div")
    filter_drop.id = drop_id
    filter_drop.classList.add("to-dropdown")
    

    for (let form_attr of specifications) {

        if (form_attr["element"].toLowerCase() == "input") {
            let input = create_input(form_attr)
            filter_drop.appendChild(input)
        } else if (form_attr["element"].toLowerCase() == "select") {
            let select = create_select(form_attr)
            select.id = selector_id
            filter_drop.appendChild(select)
        }

    }


    let complete_filter = document.createElement("div")
    complete_filter.appendChild(filter_btn)
    complete_filter.appendChild(filter_drop)

    document.querySelector("#filtro1").append(complete_filter)

}

function filter_table(table_id) {

    $(document).ready(function() {

        if ( $.fn.dataTable.isDataTable('#'+table_id ) ) {
            table = $('#'+table_id).DataTable();
        }
        else {
            table = $('#'+table_id).DataTable( {
                paging: false
            } );
        }

        $('#'+ table_id + " tfoot th").each(function ( i ) {
            var select = $('<select><option value=""></option></select>')
                .appendTo( $(this).empty() )
                .on( 'change', function () {
                    var val = $(this).val();
     
                    table.column( i )
                        .search( val ? '^'+$(this).val()+'$' : val, true, false )
                        .draw();
                } );
     
            table.column( i ).data().unique().sort().each( function ( d, j ) {
                select.append( '<option value="'+d+'">'+d+'</option>' )
            } );
        } );
    } );

}

function create_input(form_attr) {

    let input = document.createElement("input")

    for (let attr in form_attr) {

        if (attr == "classes") {
            for (let input_class of form_attr[attr]) {
                input.classList.add(input_class)
            }
        } else {
            input[attr] = form_attr[attr]
        }

    }
    
    return(input)
}


function create_select(form_attr) {

    let select = document.createElement("select")

    for (let attr in form_attr) {

        if (attr == "classes") {
            for (let select_class of form_attr[attr]) {
                select.classList.add(select_class)
            }  
        } else {
            select[attr] = form_attr[attr]
        }

    }

    for (let value of form_attr["option"]) {
        let option = document.createElement("option")
        option.value = value
        option.innerText = value
        select.appendChild(option)
    }

    return(select)

}


function create_datatable(id_parent, json_data) {

    json_data = JSON.parse(`${json_data}`)

    let thead = document.createElement("thead")
    let tr_head = document.createElement("tr")
    
    thead.appendChild(tr_head)    


    let columns = Object.keys(json_data)

    for (let col of columns) {
        let th = document.createElement("th")
        th.innerText = col
        tr_head.appendChild(th)
    }

    /*
    let tfoot = document.createElement("tfoot")
    let tr_tfoot = document.createElement("tr")

    tfoot.appendChild(tr_tfoot)
    
    for (let col of columns) {
        let th = document.createElement("th")
        th.innerText = col
        tr_tfoot.appendChild(th)
    }
    */



    let tbody = document.createElement("tbody")
    
    let rows_length = Object.keys(json_data[columns[0]]).length

    for (let row = 0; row < rows_length; row++) {
        let tr_body = document.createElement("tr")

        for (let col = 0; col < columns.length; col++) {
            let td = document.createElement("td")
            td.innerText = json_data[columns[col]][row]
            tr_body.appendChild(td)
        }

        tbody.appendChild(tr_body)
    }


    let table = document.createElement("table")
    table.classList.add("table")
    table.id = id_parent + "_table"

    table.appendChild(thead)
    table.appendChild(tbody)
    //table.appendChild(tfoot)

    document.querySelector("#" + id_parent).appendChild(table)

    $("#" + table.id).DataTable()

}
