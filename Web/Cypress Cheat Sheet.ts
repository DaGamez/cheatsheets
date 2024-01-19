
#instalar del programa
npm install cypress --save-dev


#abrir cypress
npx cypress open

cypress open

#
npm run dev

describe("empty spec", () => {
  it("passes", () => {
    cy.visit("https://example.cypress.io")
  })
})


#cypress equipo recomienda usar el atributo data test para pruebas menos fragiles
cy.get("[data-test='hero-heading']")

#correr solamente un test
it.only("the features on the homepage are correct", () => {
    cy.visit("http://localhost:3000")
  })
  
cy.get("dt").eq(0)

cy.get().type("tom@aol.com")
