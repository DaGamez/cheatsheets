
// a nivel de consola
tsc main.ts //para compilar
tsc -p .\tsconfig.json //para compilar con el archivo de configuracion



//esto es un comentario

let miTexto: string = "Hola mundo de nuevo"; //este es un string
console.log(miTexto);
console.log("Esta es una linea \n y esta es otra linea");
console.log(`El valor de mi variable es ${miTexto}`);



let opt1: number = 10; // este es un numero

opt1++; //asi le sumamos dos
opt1+=4 //asi le sumamos 4


//asi imprimimos en consola
// a la hora de imprimir en consola es importante las comillas q se usan
console.log(`Mis variables son ${opt1} y ${opt2}`);
console.log(`Mis variables son ${opt1.toPrecision(2)}`); //ajustar la precision



let varDesconocida: any; //variable de tipo desconocido, puede tomar cualquier tipo de variable

let varTipoIndefinido:undefined; // solamente puede tomar valores indefinido o null

let varVoid:void //solamente permite undefined o null

typeof(opt1); //da el tipo de variable

//funciones en typescript

function imprimirMensaje(): void { 
	console.log("Mensaje genérico");
}

function imprimirMensaje2(msj:string): void { 
	console.log(msj);
}

function sumar(op1:number, op2:number):number{
	return op1+op2;
}

var fSumar=sumar //podemos crear una funcion copiando otra en variable

