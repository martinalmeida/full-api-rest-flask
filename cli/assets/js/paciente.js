
const API_URL = 'http://127.0.0.1:5000/pacientes';
const API_URL_ID = 'http://127.0.0.1:5000/pacientes/    ';
let listar_pacientes = [];

// Inicializar las fucniones
$(() => {
    listar_pacinetes();
});

// Listar
const listar_pacinetes = () => {
    fetch(API_URL)
        .then(response => response.json())
        .then(pacientes => {
            allpacientes = pacientes.pacientes;
            pintar_pacientes(allpacientes);
        })
}


const tabla_paciente = document.querySelector('#tabla_paciente');

const pintar_pacientes = (allpacientes) => {
    let list_pacienteHTML = "";
    allpacientes.forEach(paciente => {
        list_pacienteHTML += `<tr> 
        <td> ${paciente.id} </td>
        <td> ${paciente.nombres} </td>
        <td> ${paciente.apellidos} </td>
        <td> ${paciente.tipoDocumento} </td>
        <td> ${paciente.documento} </td>
        <td> ${paciente.fechaNacimiento} </td>
        <td> ${paciente.celular} </td>
        <td> ${paciente.whatsapp} </td>
        <td> ${paciente.usuario} </td>
        <td> ${paciente.estado} </td>
        <td><button id=${paciente.id} class='btneditar btn btn-warning fa fa-pencil'></button></td>
        <td><button id=${paciente.id} class='btnborrar btn btn-danger fa fa-trash'></button></td><tr>`;
    })
    tabla_paciente.innerHTML = list_pacienteHTML;
}

const modal_paciente = $('#modal_paciente').modal('hide')
const form_paciente = document.querySelector('formulario_paciente')
const nombre_paciente = document.getElementById('nombre_paciente')
const apellido_paciente = document.getElementById('apellido_paciente')
const tipo_documento_paciente = document.getElementById('tipo_documento_paciente')
const numero_documento_paciente = document.getElementById('numero_documento_paciente')
const fecha_nacimiento_paciente = document.getElementById('fecha_nacimiento_paciente')
const telefono_paciente = document.getElementById('telefono_paciente')
const usuario_paciente = document.getElementById('usuario_paciente')
const estado_paciente = document.getElementById('estado_paciente')
let = opcion_paciente = ''

btnmodal_paciente.addEventListener('click', () => {
    nombre_paciente.value = ''
    apellido_paciente.value = ''
    tipo_documento_paciente.value = ''
    numero_documento_paciente.value = ''
    fecha_nacimiento_paciente.value = ''
    telefono_paciente.value = ''
    usuario_paciente.value = ''
    estado_paciente.value = ''
    $('#modal_paciente').modal('show')
    opcion_paciente = 'insertar_paciente'
})


// Eliminar
const on = (element, event, selector, handler) => {
    element.addEventListener(event, e => {
        if (e.target.closest(selector)) {
            handler(e)
        }
    })
}

on(document, 'click', '.btnborrar', e => {
    const fila = e.target.parentNode.parentNode
    const id = fila.firstElementChild.innerHTML
    console.log(`id`)
    console.log(API_URL_ID + id)
    Swal.fire({
        title: '¿Estás seguro?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar!'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(API_URL_ID + id, {
                method: 'DELETE'
            })
                .then(res => res.json())
                .then(response => {
                    listar_pacinetes()
                })
            Swal.fire(
                '¡Eliminado!',
                'Tu registro ha sido eliminado.',
                'success'
            )
        }
    })
})







