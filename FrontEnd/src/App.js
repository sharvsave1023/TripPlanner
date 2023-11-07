import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  constructor() {
    super();
    this.state = {
      departure_airport1: '',
      destination_airport1: '',
      departure_airport2: '',
      destination_airport2: '',
      carbon_emissions1: null,
      carbon_emissions2: null,
    };
  }

  handleSubmit = (e) => {
    e.preventDefault();

    const api_key = 'fXEzJ1nKIxwyo9y2PBVAoQ'
    url = 'https://www.carboninterface.com/api/v1/estimates'

    axios
      .post('http://localhost:5000', {
        departure_airport1: this.state.departure_airport1,
        destination_airport1: this.state.destination_airport1,
        departure_airport2: this.state.departure_airport2,
        destination_airport2: this.state.destination_airport2,
      }, {
        headers: {
          Authorization: `Bearer ${api_key}`,
          'Content-Type': 'application/json',
        },
      })
      .then((response) => {
        const { carbon_emissions1, carbon_emissions2 } = response.data;
        this.setState({ carbon_emissions1, carbon_emissions2 });
      })
      .catch((error) => {
        console.error(error);
      });
  }

  render() {
    return (
      <div className="App">
        <h1>Calculate Carbon Emissions</h1>
        <form onSubmit={this.handleSubmit}>
          <label>
            Departure Airport 1:
            <input
              type="text"
              name="departure_airport1"
              value={this.state.departure_airport1}
              onChange={(e) => this.setState({ departure_airport1: e.target.value })}
            />
          </label>
          <label>
            Destination Airport 1:
            <input
              type="text"
              name="destination_airport1"
              value={this.state.destination_airport1}
              onChange={(e) => this.setState({ destination_airport1: e.target.value })}
            />
          </label>
          <label>
            Departure Airport 2:
            <input
              type="text"
              name="departure_airport2"
              value={this.state.departure_airport2}
              onChange={(e) => this.setState({ departure_airport2: e.target.value })}
            />
          </label>
          <label>
            Destination Airport 2:
            <input
              type="text"
              name="destination_airport2"
              value={this.state.destination_airport2}
              onChange={(e) => this.setState({ destination_airport2: e.target.value })}
            />
          </label>
          <button type="submit">Calculate</button>
        </form>
        {this.state.carbon_emissions1 !== null && this.state.carbon_emissions2 !== null && (
          <div>
            <p>Carbon Emissions 1: {this.state.carbon_emissions1}</p>
            <p>Carbon Emissions 2: {this.state.carbon_emissions2}</p>
          </div>
        )}
      </div>
    );
  }
}

export default App;
