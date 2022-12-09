import React, { Component } from "react";
import PkmnWeight from "./PkmnWeight";
import PkmnGrass from "./PkmnGrass";
import PkmnFlying10 from "./PkmnFlying10";
import PkmnInverted from "./PkmnInverted";
import { Button } from "@mui/material/";
import DataTable from "react-data-table-component"
import { BrowserRouter as Router, 
  Routes, 
  Route, 
  Link, 
  Redirect
} from "react-router-dom";



export default class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pokemons: [],
      columns : [
          {
            name: "ID",
            selector: (row) => row.pkm_id,
          },
          {
            name: "Nombre",
            selector: (row) => row.name,
          },
          {
            name: "Tipo",
            selector: (row) => row.type,
          },
          {
            name: "Peso",
            selector: (row) => row.weight,
          },
          {
            name: "Altura",
            selector: (row) => row.height,
          },
        ]
      
    };
    this.getPkmnDetials();
  }

  // Se obtienen los pokemones que cumplen con la 
  // condicion desde la api
  getPkmnDetials(){
    fetch("/api/home")
    .then((response) => response.json())
    .then((data) => {
      this.setState({
        pokemons : data
      });
    });
    
  }
  
  // Aqui se utiliza el router y se muestra la primera vista con los 50 pokemon
  render() {
    return (
      
      <Router>
        <Routes>
          <Route path="/" exact element= {

            <div style={{ margin: "20px" }}>
              <h1>Bienvenidos, a continuacion se muestran los primeros 50 pokemon de la pokeApi.</h1>
              <h1>Para cambiar de filtro, por favor utilizar el menu de navegación.</h1>
              {/* Se muestran los pokemon en una tabla */}
              <DataTable
                title="Primeros 50 Pokemon"
                columns={this.state.columns}
                data={this.state.pokemons}
                dense
                direction="auto"
                fixedHeader
                fixedHeaderScrollHeight="500px"
                highlightOnHover
                pagination
                responsive
                striped
                subHeaderAlign="right"
                subHeaderWrap
              />

              {/* Menu de navegación */}
      
              <Button color="primary" variant="contained" to="/grass" component={Link}> 
                  Grass
                </Button>
      
              <Button color="primary" variant="contained" to="/weight" component={Link}> 
                  30 {'<'} Peso {'<'} 80
              </Button>
            
              <Button color="primary" variant="contained" to="/flying_10" component={Link}> 
                Flying/Altura {'>'} 10
              </Button>

              <Button color="primary" variant="contained" to="/inverted_name" component={Link}> 
                Nombre Invertido
              </Button>
            </div>
          } />
          <Route path="/weight" element = {<PkmnWeight />} />
          <Route path="/grass" element = {<PkmnGrass />} />
          <Route path="/flying_10" element = {<PkmnFlying10 />} />
          <Route path="/inverted_name" element = {<PkmnInverted />} />
        </Routes>
      </Router>
    );
  }
}